from multipledispatch import dispatch
from datetime import datetime

@dispatch()
def dates() -> str:
    """
    Returns the current date and time in datetime format.
    """
    return datetime.now()

@dispatch(str)
def dates(date: str) -> datetime:
    """
    Convert a date string to a datetime object.
    
    Args:
        date (str): The date string to convert.
        
    Returns:
        datetime: The converted datetime object.
    """
    return datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

print(dates("2025-03-29 10:56:36"))