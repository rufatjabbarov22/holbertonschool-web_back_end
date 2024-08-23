#!/usr/bin/env python3
"""Module for simple helper function."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function returns range of pages."""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
  
