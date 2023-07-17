import time


def npi(practice_item, duration_minutes) -> dict:
    """Returns dict containing new practice item"""
    return {'practice_item': practice_item, 'duration': duration_minutes}


routine = [
    npi('stretching', 10),
    npi('vocal warmup', 5),
    npi('solfege', 5),
    npi('transcribing', 10),
    npi('sizzle', 5),
    npi('wya', 10),
    npi('lost', 10)
]