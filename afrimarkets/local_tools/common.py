from datetime import datetime
from datetime import timedelta

date_format = "%Y-%m-%d"

def period2interval(start_date = "2026-01-01", end_date = "2026-12-31",by = 60):
    """
    Convert start and end dates to an interval string.
    start_date and end_date should be in the format 'YYYY-MM-DD'.
    The 'by' parameter specifies the interval in seconds (default is 60 seconds).
    """

    interval = []
    try:
        start = datetime.strptime(start_date, date_format)
        end = datetime.strptime(end_date, date_format)
    except ValueError:
        raise ValueError(
            "Invalid date format. Please use 'YYYY-MM-DD'."
        )

    if start > end:
        raise ValueError(
            "Start date must be earlier than or equal to end date."
        )

    _date = start

    while _date < end:
        next_date = min(_date + timedelta(days=by), end)

        interval.append([
            _date.strftime(date_format),
            next_date.strftime(date_format)
        ])

        _date = next_date


    return interval


def datefr2dateiso(data_list, date_field = "Date"):

    for row in data_list:
        row[date_field] = datetime.strptime(row[date_field], "%d/%m/%Y").date().strftime(date_format)

    return data_list

def datalist2structure(data_list, structure = "row", date_field = "Date"):

    if structure == "row":
        return data_list

    elif structure == "column":

        column_data = {}
        for row in data_list:
            for key, value in row.items():
                if key not in column_data:
                    column_data[key] = []
                column_data[key].append(value)

        return column_data

    else:
        raise ValueError(
            "Invalid structure. Please use 'row' or 'column'."
        )