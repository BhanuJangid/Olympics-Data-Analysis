import pandas as pd

df = pd.read_csv('athlete_events.csv')
df_region = pd.read_csv('noc_regions.csv')


def preprocess():
    global df, df_region
    df = pd.read_csv('athlete_events.csv')
    df_region = pd.read_csv('noc_regions.csv')

    # Filter for Summer Olympics only
    df = df[df['Season'] == 'Summer']

    # Merge with region data
    df = df.merge(df_region, on='NOC', how='left').copy()

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # Create dummy variables for medals and drop the original Medal column
    df = pd.concat([df, pd.get_dummies(df['Medal']).astype(int)], axis=1)

    return df