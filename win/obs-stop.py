"""Example shows how to send requests and get responses."""

import asyncio

from obswsrc import OBSWS
from obswsrc.requests import ResponseStatus, StopRecordingRequest


async def main():

    async with OBSWS('localhost', 4444, "password") as obsws:

        response = await obsws.require(StopRecordingRequest())

        # Check if everything is OK
        if response.status == ResponseStatus.OK:
            print("Recording has stopped")
        else:
            print("Couldn't stop recording! Reason:", response.error)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
