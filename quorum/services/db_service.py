import pandas as pd


def load_bills() -> pd.DataFrame:
    return csv_to_df('quorum/db/csv/bills.csv')


def load_legislators() -> pd.DataFrame:
    return csv_to_df('quorum/db/csv/legislators.csv')


def load_vote_result() -> pd.DataFrame:
    return csv_to_df('quorum/db/csv/vote_results.csv')


def load_votes() -> pd.DataFrame:
    return csv_to_df('quorum/db/csv/votes.csv')


def csv_to_df(path: str) -> pd.DataFrame:
    return pd.read_csv(path)
