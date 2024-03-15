from typing import Dict, List
import pandas as pd
from quorum.services.db_service import (
    load_bills,
    load_legislators,
    load_vote_result,
    load_votes)


def bill_result_context():

    df_bills = load_bills()
    df_legislators = load_legislators()
    df_vote_results = load_vote_result()
    df_votes = load_votes()

    df_merged = pd.merge(df_bills, df_legislators, how='inner',
                         left_on='sponsor_id', right_on='id', validate=None,
                         suffixes=('_bill', '_legislators'))

    df_merged = pd.merge(df_merged, df_votes, how='inner',
                         left_on='id_bill', right_on='bill_id', validate=None)

    df_merged = pd.merge(df_merged, df_vote_results, how='inner',
                         left_on='id', right_on='vote_id', validate=None)

    result = mount_base_structure(df_merged)

    resolve_votes(df_merged, result)

    return result


def mount_base_structure(df: pd.DataFrame) -> List[Dict]:
    df_bills_unified = df[[
        'id_bill', 'title', 'name']].drop_duplicates()

    base_structure = []
    for _, row in df_bills_unified.iterrows():
        base_structure.append({

            "id": row['id_bill'],
            "title": row['title'],
            "supporters": 0,
            "opposers": 0,
            "primary_sponsor": row['name']

        })

    return base_structure


def resolve_votes(df: pd.DataFrame, result: List) -> None:
    # import ipdb
    # ipdb.set_trace()
    for _, row in df.iterrows():
        if d := next((item for item in result if item['id'] == row['id_bill']), None):
            if row['vote_type'] == 1:
                d['supporters'] += 1

            elif row['vote_type'] == 2:
                d['opposers'] += 1
