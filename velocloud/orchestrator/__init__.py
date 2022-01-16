"""


1/2/22 - THIS NEEDS TO BE REWRITTEN!! (see roadmap.md)


Orchestrator

This module is used to retrieve information from the VCO API.

Modules
  edge:  Used for edge specific functionality.
  enterprise:  Used for enterprise specific functionality.
"""
import aiohttp
import logging
from velocloud.models import error
from velocloud.models.session import VCO
__all__ = ['api', 'edge', 'enterprise', 'error_handlers']


LOGGER = logging.getLogger('velocloud.orchestrator.error_handlers')


async def format_error(status: int, data: dict) -> error.Error:
    """Format API Errors

    - error["data"] is not always included
    """
    WARNINGS = []
    ERRORS = []

    # e = Error()
    e = error.Error(
        code=data["error"].get('code'),
        message=data["error"].get('message')
    )
    if 'data' in data["error"].keys():
        if 'warning' in data["error"]["data"].keys():
            # Warnings
            LOGGER.info('Warnings received.')
            for warn in data["error"]["data"]["warning"]:
                WARNINGS.append(error.ValidationErrorDetails(
                    code=warn.get('code'),
                    message=warn.get('message'),
                    path=warn.get('path')
                ))
        elif 'error' in data["error"]["data"].keys():
            # Errors
            LOGGER.info('Errors received.')
            for err in data["error"]["data"]["error"]:
                ERRORS.append(error.ValidationErrorDetails(
                    code=err.get('code'),
                    message=err.get('message'),
                    path=err.get('path')
                ))

        # Apply ErrorData if there is any
        if WARNINGS:
            e.data = error.ErrorData(
                valid=data["error"]["data"].get('validity'),
                warning=WARNINGS
            )
        if ERRORS:
            e.data = error.ErrorData(
                valid=data["error"]["data"].get('validity'),
                error=ERRORS
            )

    return e


async def send(session: VCO, endpoint: str, body: dict = None) -> dict:
    """Get Edge

    A general purpose API caller.

    Args:
        SESSION (VCO): A Velocloud Orchestrator Session object
        ENDPOINT (str): The specified endpoint
        BODY (dict): The HTTP POST Body

    Returns:
        (dict): API results
    """
    URL = f'{session.API_URL}{endpoint}'

    async with aiohttp.request('POST', URL, headers=session.get_headers(), json=body) as api_request:
        if api_request.status != 200:
            status = api_request.status
            error_data = await api_request.json()
            formatted_error = await format_error(status, error_data)
            LOGGER.error(formatted_error)
            raise Exception(f'{formatted_error.code}: {formatted_error.message}')

        data = await api_request.json()

        LOGGER.debug(data)

    return data
