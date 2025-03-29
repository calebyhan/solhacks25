from multipledispatch import dispatch
from datetime import datetime
import json

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

def report(reportdate: str, location: float[2], details: str, tactics: str, verification: int, status: str) -> dict:
    """
    Generates a report dictionary.

    Args:
        reportdate (str): The date of the report.
        details (str): The details of the report.
        tactics (str): The tactics used in the report.
        verification (int): The verification status.
        status (str): The status of the report.

    Returns:
        dict: The generated report dictionary.
    """
    return {
        "date": dates(),
        "report_date": dates(reportdate),
        "location": "{}, {}".format(location[0], location[1]),
        "details": details,
        "tactics": tactics,
        "verification": verification,
        "status": status
    }

def add_data(data: dict) -> None:
    """
    Adds data to the JSON file.

    Args:
        data (dict): The data to add.
    """
    with open('data.json', 'a') as f:
        d = json.load(f)
        d["n"] += 1
        d["last_update"] = dates()
        d["data"].append(data)

def get_data(i: int, startDate: str, endDate: str) -> str:
    """
    Returns all api data in JSON format.

    Returns:
        str: The JSON data.
    """
    with open('data.json', 'r') as f:
        data = json.load(f)
    if startDate:
        startDate = dates(startDate)
    if endDate:
        endDate = dates(endDate)
    if startDate and endDate:
        data["data"] = [d for d in data["data"] if startDate <= dates(d["timestamp"]) <= endDate]
    if i:
        data["data"] = data["data"][-i:]
    return data
