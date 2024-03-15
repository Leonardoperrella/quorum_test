import pandas as pd
from quorum.services.bill_result_service import bill_result_context


def test_bill_context(mocker):

    bills_data = {
        'id': ['2952375', '2900994'],
        'title': ['Better Act', 'Infrastructure'],
        'sponsor_id': ['412211', '400100']
    }

    df_bills_data = pd.DataFrame(bills_data)

    legislators_data = {
        'id': ['412211', '400100'],
        'name': ['Lorem', "Ipsum"],

    }

    df_legislators_data = pd.DataFrame(legislators_data)

    votes_data = {
        'id': ['3314452', '3321166'],
        'bill_id': ['2900994', "2952375"],

    }

    df_votes_data = pd.DataFrame(votes_data)

    assert bill_result_context()[0] == {
        "id": 1,
        "name": "Bill 1",
        "supporters": 10,
        "opposers": 1,
        "primary_sponsor": "Rep. Lorem"
    }
