

from dataclasses import dataclass
from enum import Enum

import asyncio
import random


class EventType(Enum):
    NEWNUMBER = "newnumber"
    DIRECTION = "direction"


@dataclass
class ServerSentEvent:
    event: EventType
    data: str

    def encode(self) -> bytes:
        lines = [
            "event: %s" % self.event.value,
            "data: %s" % self.data,
            "", "",
        ]
        return "\n".join(lines).encode("utf-8")


async def event_producer():
    while True:
        await asyncio.sleep(2)
        eventtype = random.choice(list(EventType))
        if eventtype is EventType.NEWNUMBER:
            number = random.randrange(0, 99)
            if number < 10:
                raise Exception("Silly Error")
            yield ServerSentEvent(eventtype, str(number)).encode()
        elif eventtype is EventType.DIRECTION:
            direction = random.choice(("north", "east", "south", "west"))
            yield ServerSentEvent(eventtype, direction).encode()
        else:
            raise NotImplementedError("Unknown event type: %r" % eventtype)
