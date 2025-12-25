import time
from fastapi import HTTPException
from functools import wraps

REQUESTS = {}

def rate_limit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = "global"
        now = time.time()

        REQUESTS.setdefault(user, [])
        REQUESTS[user] = [t for t in REQUESTS[user] if now - t < 60]

        if len(REQUESTS[user]) >= 5:
            raise HTTPException(status_code=429, detail="Too many requests")

        REQUESTS[user].append(now)
        return func(*args, **kwargs)

    return wrapper
