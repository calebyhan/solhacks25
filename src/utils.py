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
    return datetime.now().strftime("%Y-%m-%d %H:%M")

@dispatch(str)
def dates(date: str) -> datetime:
    """
    Convert a date string to a datetime object.
    
    Args:
        date (str): The date string to convert.
        
    Returns:
        datetime: The converted datetime object.
    """
    return datetime.strptime(date, "%Y-%m-%d %H:%M")

@dispatch(datetime)
def dates(date: datetime) -> str:
    """
    Convert a datetime object to a string.
    
    Args:
        date (datetime): The datetime object to convert.
        
    Returns:
        str: The converted date string.
    """
    return date.strftime("%Y-%m-%d %H:%M")

def report_date(reportdate: str) -> datetime:
    """
    Converts a report date string to a datetime object.

    Args:
        reportdate (str): The report date string.

    Returns:
        datetime: The converted datetime object.
    """
    # format is 2025-03-29T12:05
    return datetime.strptime(reportdate, "%Y-%m-%dT%H:%M")

def report(reportdate: str, location: list[float, float], details: str, status: str) -> dict:
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
        "report_date": dates(report_date(reportdate)),
        "location": "{}, {}".format(location[0], location[1]),
        "details": details,
        "status": status
    }

def add_data(data: dict) -> None:
    """
    Adds data to the JSON file.

    Args:
        data (dict): The data to add.
    """
    with open('data.json', 'r') as f:
        d = json.load(f)
    d["n"] += 1
    print(dates())
    d["last_update"] = dates()
    d["data"].append(data)
    print(d)
    with open('data.json', 'w') as f:
        json.dump(d, f, indent=4)

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


