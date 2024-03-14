import pandas as pd
from quorum.services.legislator_result_service import legislator_result_context


def test_vote_result_context(mocker):

    volte_results_data = {
        'id': [1, 2, 3, 4, 5],
        'legislator_id': [1, 1, 1, 2, 2],
        'vote_id': [1, 2, 1, 1, 2],
        'vote_type': [1, 2, 2, 1, 2]
    }

    df_volte_results = pd.DataFrame(volte_results_data)

    mocker.patch(
        "quorum.services.legislator_result_service.load_vote_result",
        return_value=df_volte_results
    )

    legislators_data = {
        'id': [1, 2],
        'name': ['Lorem', "Ipsum"],

    }

    df_legislators_data = pd.DataFrame(legislators_data)

    mocker.patch(
        "quorum.services.legislator_result_service.load_legislators",
        return_value=df_legislators_data
    )

    assert legislator_result_context()[0] == {
        "id": 1,
        "name": "Lorem",
        "suported_bills": 1,
        "opposed_bills": 2
    }
