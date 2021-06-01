"""

This needs some love, big time.

"""
from velocloud.models import error
import logging

logger = logging.getLogger('velocloud.orchestrator.error_handlers')


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
            logger.info('Warnings received.')
            for warn in data["error"]["data"]["warning"]:
                WARNINGS.append(error.ValidationErrorDetails(
                    code=warn.get('code'),
                    message=warn.get('message'),
                    path=warn.get('path')
                ))
        elif 'error' in data["error"]["data"].keys():
            # Errors
            logger.info('Errors received.')
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
