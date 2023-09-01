import pandas as pd
from data_transformation import transform_dataframe


def test_transform_dataframe():
    # Given a sample input dataframe
    input_data = {
        'Unnamed: 0': ['site 1', None, None],
        'Unnamed: 1': ['Page Views', '2021-01-01', 6],
        'Unnamed: 2': ['Page Views', '2021-01-02', 4]
    }
    df = pd.DataFrame(input_data)

    # When the transformation function is called
    result = transform_dataframe(df)

    # Then the output should match the expected dataframe
    expected_data = {
        'Day of Month': [1, 2],
        'Date': ['2021/01/01', '2021/01/02'],
        'Site ID': ['site 1', 'site 1'],
        'Page Views': [6, 4],
        'Unique Visitors': [None, None],
        'Total Time Spent': [None, None],
        'Visits': [None, None],
        'Average Time Spent on Site': [None, None]
    }
    expected_df = pd.DataFrame(expected_data)

    pd.testing.assert_frame_equal(result, expected_df)
