import pandas as pd
from quorum.services.bill_result_service import bill_result_context


def test_bill_context(mocker):

    bills_data = {
        'id': [1, 2],
        'title': ['Bill 1', 'Bill 2'],
        'sponsor_id': [1, 2]
    }

    df_bills_data = pd.DataFrame(bills_data)

    mocker.patch(
        "quorum.services.bill_result_service.load_bills",
        return_value=df_bills_data
    )

    legislators_data = {
        'id': [1, 2],
        'name': ['Lorem', "Ipsum"],

    }

    df_legislators_data = pd.DataFrame(legislators_data)

    mocker.patch(
        "quorum.services.bill_result_service.load_legislators",
        return_value=df_legislators_data
    )

    vote_results_data = {
        'id': [1, 2, 3, 4, 5],
        'legislator_id': [1, 1, 1, 2, 2],
        'vote_id': [1, 1, 2, 1, 2],
        'vote_type': [1, 2, 2, 1, 2]
    }

    df_vote_results = pd.DataFrame(vote_results_data)

    mocker.patch(
        "quorum.services.bill_result_service.load_vote_result",
        return_value=df_vote_results
    )

    votes_data = {
        'id': [1, 2],
        'bill_id': [1, 2],

    }

    df_votes_data = pd.DataFrame(votes_data)

    mocker.patch(
        "quorum.services.bill_result_service.load_votes",
        return_value=df_votes_data
    )

    assert bill_result_context()[0] == {
        "id": 1,
        "title": "Bill 1",
        "supporters": 2,
        "opposers": 1,
        "primary_sponsor": "Lorem"
    }
