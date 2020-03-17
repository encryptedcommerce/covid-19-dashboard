import os

from flask import request
import geoip2.database
import pandas as pd


MAXMIND_LICENSE = os.getenv('MAXMIND_LICENSE')
MAXMIND_ACCOUNT = os.getenv('MAXMIND_ACCOUNT')
COUNTRY_DB_PATH = 'data/GeoLite2-Country_20200310/GeoLite2-Country.mmdb'


def get_user_country() -> str:
    reader = geoip2.database.Reader(COUNTRY_DB_PATH)
    user_ip = request.headers.get('X-Real-IP')
    if user_ip is None or user_ip == '127.0.0.1':
        # Local development
        country_name = os.getenv('COUNTRY')
    else:
        if ',' in user_ip:
            user_ip = user_ip.split(',')[0]
        response = reader.country(user_ip)
        country_name = response.country.name

    return country_name


def country_group(df: pd.DataFrame) -> pd.DataFrame:
    """Group by Country, summing counts by date.

    Get average lat/lon of country across all records, for future use in map.
    """
    df = df.copy()
    country_coords = df.groupby('Country/Region').mean().iloc[:, 0:2]
    df = df.groupby('Country/Region').sum().iloc[:, 2:]
    df['avg_lat'] = country_coords['Lat']
    df['avg_lon'] = country_coords['Long']
    # Rename Country name columns to match GeoIP names.
    df.rename(
        index={
            'US': 'United States',
            'Korea, South': 'South Korea',
        },
        inplace=True
    )
    df = df.reset_index()
    return df

