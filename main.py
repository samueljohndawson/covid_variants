from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile

# downloads the dataset from kaggle
api = KaggleApi()
api.authenticate()
api.dataset_download_files('yamqwe/omicron-covid19-variant-daily-cases')
with zipfile.ZipFile('omicron-covid19-variant-daily-cases.zip') as zf:
    zf.extractall()


# loads the data to df, converts 'date' column into datetimes
df = pd.read_csv("covid-variants.csv", parse_dates=['date'])

# reduces data - one for individual variant numbers, one for total covid numbers
variant_cases = df[['location', 'date', 'variant', 'num_sequences']]
cases_total = df[['location', 'date', 'variant', 'num_sequences_total']]

# plots the data
all_variants = variant_cases.loc[(df['location'] == 'United Kingdom')]
total_covid_numbers = cases_total[(df['location'] == 'United Kingdom')]
sns.lineplot(data=total_covid_numbers, x='date', y='num_sequences_total', color='black', linestyle='--', linewidth=1, label='All Varients')
sns.lineplot(data=all_variants, x="date", y="num_sequences", hue='variant')

# labels the graph
plt.ylabel('Number of cases')
plt.xlabel('Date')
plt.title('UK Covid Case Numbers by Variant')

plt.show()


