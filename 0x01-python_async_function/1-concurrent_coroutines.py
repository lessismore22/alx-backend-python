#!/usr/bin/env python3
""" Task 1's module
"""

import asyncio
from typing imprt List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Executes wait_random n times.
    """
    tasks = []
    delays = []

    for i in range(n):
        task = wait_random(max_delay)
        tasks.append(task)

    for task un asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
