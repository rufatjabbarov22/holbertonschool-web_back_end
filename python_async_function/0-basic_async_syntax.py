#!/usr/bin/env python3
"""
Random and asyncio modules are imported
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Function waits until random float time between 0 and max_delay
    """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
    
