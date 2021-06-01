"""Velocloud - example.py

This is an example script showing how to utilize this package.  You should use this as a reference to do what you want.

What is this package?
    TL;DR - An async python API wrapper for interacting with a Velocloud Orchestrator.

Why?
    Nothing really exists today.
"""
import asyncio
from velocloud.models import edge, enterprise, session
import logging


# Logger for your scripts
LOGGER = logging.getLogger(__name__)

# Logger for Velocloud (Optional)(Default: INFO)
# VC_LOGGER = logging.getLogger('velocloud')
# VC_LOGGER.handlers[0].setLevel(logging.DEBUG)
# VC_LOGGER.setLevel(logging.DEBUG)


async def main():
    """Main"""

    """Session"""
    # API_URL="https://vco-###.velocloud.net" - Replace ###'s
    VCO = session.VCO(TOKEN="", API_URL="")  # INPUT REQUIRED
    LOGGER.info('VCO Session Created.')

    """Edge Model"""
    # Retrieve an Edge
    LOGGER.info('Retrieving Edge')
    e = await edge.Edge.getEdge(session=VCO, name='Edge Hostname')  # INPUT REQUIRED
    LOGGER.info('Edge Retrieved')
    print(f'Name: {e.name}\nID: {e.edge_id}')
    await asyncio.sleep(2)

    """Enterprise Model"""
    # Retrieve Enterprise
    ent = await enterprise.Enterprise.getEnterprise(VCO)
    LOGGER.info(ent)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
