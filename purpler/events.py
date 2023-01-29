

from dataclasses import dataclass

import asyncio
import random


@dataclass
class ServerSentEvent:
    number: int

    def encode(self) -> bytes:
        lines = [
            "event: newnumber",
            "data: %i" % self.number,
            "", "",
        ]
        return "\n".join(lines).encode("utf-8")


async def event_producer():
    while True:
        await asyncio.sleep(2)
        number = random.randrange(0, 99)
        if number < 10:
            raise Exception("Silly Error")
        yield ServerSentEvent(number).encode()
