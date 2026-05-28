# API Retry Mechanism - Simulator
import time

def retry(max_attempts=3, delay=1.0, exceptions=(Exception,)):
    """
        Decorator Function: retries a function on failure
        Usage: @retry(max_attempts=3, delay=2.0)
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f" Attempts: {attempt/max_attempts} failed: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
            
            raise RuntimeError(f"All {max_attempts} attempts failed")
        return wrapper
    return decorator

call_count = 0

@retry(max_attempts=4, delay=0)
def fetch_user_data(user_id: str, fields: list, **options):
    global call_count
    call_count += 1

    if call_count < 3:
        raise ConnectionError("Service Unavailable")
    
    return {"id": user_id, 'fields': fields, 'options': options}

result = fetch_user_data("U001", ["name", "email"], timeout=30, cache=True)
print(result)