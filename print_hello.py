import logging

def print_hi(num=int) -> int:
    logging.info(f"{"Hi"*num}")
    return num*2

