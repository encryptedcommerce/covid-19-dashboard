from typing import List

from models import item_data


def get_account_codes(start_date: str, end_date: str ) -> List[str]:
    """Fetches data and filters it to get list of unique account IDs.

    Arguments:
        start_date: Start of date range.
        end_date: End of date range.

    Returns:
        DataFrame with table data, daily or cumulative.
    """
    df = item_data.fetch_data(start_date, end_date)
    account_code = list(df['account_code'].unique())
    return account_code


