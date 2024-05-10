import pandas as pd

from date_funcs import add_days, daterange, get_date_diff

df = pd.read_csv("output.csv", header=None)
df.columns = ["rank", "name", "userID", "score", "date"]


# check which dates have no scores, so I can double check that they actually have no score and it wasn't just an error
sd = "2023-01-01"
ed = "2024-04-30"

all_dates = daterange(sd, ed)
all_dates[:] = [x.strftime("%Y-%m-%d") for x in all_dates]
dates = df["date"].unique().tolist()
missing_dates = list(set(all_dates) - set(dates))
len(missing_dates)

# check number of crosswords completed by each user
df["name"].value_counts()

# check number of first place and second place finishes
df[["rank", "name"]].value_counts()


def get_compare_users_df(users_list, df):
    """
    Finds the puzzles that each user in the list has completed. Returns a DataFrame with the ranks, names, userIDs, scores, and dates.

    :param list users_list: The list of users you want to compare
    :param DataFrame df: The dataframe you want to use to retrieve the data
    :return: the DataFrame with the puzzle data
    :rtype: Pandas DataFrame
    """
    users_dates = {}
    combined_dates = {}
    for user in users_list:
        users_dates[user] = df[(df["name"] == user)]["date"].to_list()
        if len(combined_dates) == 0:
            combined_dates = set(users_dates[user])
        else:
            combined_dates = set(combined_dates) & set(users_dates[user])
    return df[df["date"].isin(list(combined_dates))]


def check_longest_streak(user, place):
    longest = 0
    longest_end_date = "1990-01-01"
    cur_streak = 0
    cur_date = "1990-01-01"
    user_df = df[df["name"] == user]
    for index, row in user_df.iterrows():
        if row["rank"] == place:
            if len(df[df["date"] == row["date"]]) <= 1:
                cur_date = row["date"]
                continue
            elif row["date"] == add_days(cur_date, 1):
                cur_streak += 1
                cur_date = row["date"]
                if cur_streak > longest:
                    longest = cur_streak
                    longest_end_date = row["date"]
            else:
                if cur_streak > longest:
                    longest = cur_streak
                    longest_end_date = row["date"]
                cur_streak = 1
                cur_date = row["date"]

        else:
            continue
    return {"longest": longest, "end_date": longest_end_date}
