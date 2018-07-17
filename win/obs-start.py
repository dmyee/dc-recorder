"""Example shows how to send requests and get responses."""

import asyncio

from obswsrc import OBSWS
from obswsrc.requests import ResponseStatus, StartRecordingRequest


async def main():

    async with OBSWS('localhost', 4444, "password") as obsws:

        response = await obsws.require(StartRecordingRequest())

        # Check if everything is OK
        if response.status == ResponseStatus.OK:
            print("Recording has started")
        else:
            print("Couldn't start recording! Reason:", response.error)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
