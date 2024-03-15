from typing import Dict, List
import pandas as pd

from quorum.services.db_service import load_legislators, load_vote_result


def legislator_result_context():
    df_vote_result = load_vote_result()
    df_legislators = load_legislators()

    df_grouped_vote_result = df_vote_result.groupby(
        ['legislator_id', 'vote_type'], as_index=False).count()

    df_merged = pd.merge(df_grouped_vote_result, df_legislators, how='inner',
                         left_on='legislator_id', right_on='id', validate=None)

    df_legislator_unified = df_merged[[
        'legislator_id', 'name']].drop_duplicates()
    result = mount_base_structure(df_legislator_unified)

    resolve_votes(df_merged, result)

    return result


def mount_base_structure(df: pd.DataFrame) -> List[Dict]:
    base_structure = []
    for _, row in df.iterrows():
        base_structure.append({

            "id": row['legislator_id'],
            "name": row['name'],
            "suported_bills": 0,
            "opposed_bills": 0

        })

    return base_structure


def resolve_votes(df: pd.DataFrame, result: List) -> None:
    for _, row in df.iterrows():
        if d := next((item for item in result if item['id'] == row['legislator_id']), None):
            if row['vote_type'] == 1:
                d['suported_bills'] += row['id_x']

            elif row['vote_type'] == 2:
                d['opposed_bills'] += row['id_x']
