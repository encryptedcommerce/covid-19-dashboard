from datetime import datetime, timedelta
from typing import Dict

import pandas as pd


# data cache to avoid re-fetching data for the same date range multiple times
DATA_CACHE: pd.DataFrame = pd.DataFrame({})
DATA_CACHE_END_DATE: str = ''


def format_date_column(s: str) -> str:
    s_month, s_day, s_year = s.split('/')
    if int(s_day) < 10:
        s_day = f'0{s_day}'  # zero-pad day
    if int(s_month) < 10:
        s_month = f'0{s_month}'  # zero-pad month
    s_year = f'20{s_year}'  # four-digit year
    fixed_date = f'{s_year}-{s_month}-{s_day}'

    return fixed_date


def load_data() -> Dict[str, pd.DataFrame]:
    """Load data from CSV files or return from module-global cache.

    The CSV files are provided by Johns Hopkins CSSE: https://github.com/CSSEGISandData/COVID-19
    with daily updates at 23:59 UTC.

    A cron job will be set up to download the latest version each day.

    This function will check to see if its cache contains data for the present day (UTC);
    if not, it will reload the file from disk.
    """
    global DATA_CACHE, DATA_CACHE_END_DATE

    utc_yesterday = datetime.utcnow().date() - timedelta(days=1)

    if (
            len(DATA_CACHE) == 0
            or DATA_CACHE_END_DATE != utc_yesterday
    ):
        # Cache miss: fetch new data
        covid19_confirmed = pd.read_csv('data/time_series_19-covid-Confirmed.csv')
        covid19_recovered = pd.read_csv('data/time_series_19-covid-Recovered.csv')
        covid19_deaths = pd.read_csv('data/time_series_19-covid-Deaths.csv')

        non_date_cols = list(covid19_confirmed.columns[0:4])
        date_cols = list(covid19_confirmed.columns[4:])

        for df in [covid19_confirmed, covid19_recovered, covid19_deaths]:
            df.columns = non_date_cols + [
                format_date_column(col) for col in date_cols
            ]

        # Due to changes in reporting methodology in China prior to Feb 12, and low prevalence
        # in most other countries, left-trimming data to start on Feb 12
        # FIXME: DRY
        covid19_confirmed = covid19_confirmed.drop(
            covid19_confirmed.columns[list(range(4, 25))], axis=1
        )
        covid19_recovered = covid19_recovered.drop(
            covid19_recovered.columns[list(range(4, 25))], axis=1
        )
        covid19_deaths = covid19_deaths.drop(
            covid19_deaths.columns[list(range(4, 25))], axis=1
        )

        # Rename Country name columns to match GeoIP names.
        covid19_confirmed.rename(
            index={
                'US': 'United States',
                'Colombia': 'Locombia',
            },
            inplace=True
        )
        covid19_deaths = covid19_deaths.rename(index={'US': 'United States'})
        covid19_recovered = covid19_recovered.rename(index={'US': 'United States'})

        most_recent_col = covid19_confirmed.columns[-1]
        most_recent_date = datetime.strptime(most_recent_col, '%Y-%m-%d').date()

        print(f'yesterday (UTC): {utc_yesterday}')
        print(f'most recent data: {most_recent_date}')

        if utc_yesterday > most_recent_date:
            print('Out of date:')
            print(f'    most recent data is from {most_recent_col} instead of {utc_yesterday}')
        else:
            print(f'Loaded up-to-date data from CSV as of {most_recent_col}')

        data = {
            'confirmed': covid19_confirmed,
            'recovered': covid19_recovered,
            'deaths': covid19_deaths,
        }

        DATA_CACHE = data
        DATA_CACHE_END_DATE = utc_yesterday

        return data

    else:
        # Cache hit
        return DATA_CACHE
