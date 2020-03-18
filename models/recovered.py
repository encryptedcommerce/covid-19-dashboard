from typing import List

import numpy as np
import pandas as pd
from pandas.core.base import DataError

from models import common, fetch_data


def get_table_data(include_coords: bool = False) -> pd.DataFrame:
    """Fetches data and manipulates it for use in a DataTable.

    Returns:
        DataFrame with confirmed cases per country.
    """
    data = fetch_data.load_data()
    recovered = pd.DataFrame()
    if 'recovered' in data:
        recovered = data['recovered']

        #  Get average lat/lon of country across all records, for future use in map
        recovered = common.country_group(recovered)

    recovered = recovered.sort_values(by=recovered.columns[-3], ascending=False)

    if not include_coords:
        recovered = recovered.iloc[:, 0:-2]
    return recovered


def get_chart_data() -> List[dict]:
    """Fetches Deaths data and manipulates it for use in a Graph.

    Arguments:

    Returns:
        list of data objects for items and responses.
    """
    data = get_table_data()
    data = data.sort_values(by=data.columns[-3], ascending=False)
    dates = data.columns[1:]
    chart_data = []
    for _, row in data.iterrows():
        series = {
            'type': 'scatter',
            'name': row[0],
            'x': dates,
            'y': row[1:],
        }
        chart_data.append(series)

    return chart_data


def get_user_country() -> str:
    """Get the country from the user's IP adddress."""
    return common.get_user_country()
