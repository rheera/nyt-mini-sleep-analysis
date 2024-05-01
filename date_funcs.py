def daterange(start_date, end_date):
    import pandas as pd

    return pd.date_range(start=start_date, end=end_date).to_list()


def add_days(date, num_of_days):
    import datetime

    start_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    end_date = start_date + datetime.timedelta(days=num_of_days)
    return end_date.strftime("%Y-%m-%d")


def get_date_diff(start_date, end_date):
    from datetime import datetime

    delta = (
        datetime.strptime(end_date, "%Y-%m-%d").date()
        - datetime.strptime(start_date, "%Y-%m-%d").date()
    )
    return delta.days
