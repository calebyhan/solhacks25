from multipledispatch import dispatch
from datetime import datetime

@dispatch()
def dates() -> str:
    """
    Returns the current date and time in datetime format.

    Returns:
        str: The current date and time.
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

@dispatch(datetime)
def dates(date: datetime) -> str:
    """
    Convert a datetime object to a string.
    
    Args:
        date (datetime): The datetime object to convert.
        
    Returns:
        str: The converted date string.
    """
    return date.strftime("%Y-%m-%d %H:%M:%S")

def get_data(i: int, startDate: str, endDate: str) -> str:
    """
    Returns all api data in JSON format.

    Returns:
        str: The JSON data.
    """
    with open('data.json', 'r') as f:
        data = f.read()
    return data