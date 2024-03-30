from readit import read_data
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
 


df = read_data('data/APR_tidy.csv')
plot_df = df[['SPORT_NAME','APR_RATE_YEAR','APR_RATE']].groupby(['SPORT_NAME','APR_RATE_YEAR']).mean().reset_index()
#plot_df = df[['SPORT_NAME','APR_RATE_YEAR',]]

sns.set_style('darkgrid')
fig, ax = plt.subplots(figsize=(15, 10))
axis = sns.boxplot(data=plot_df, x="APR_RATE_YEAR", y="APR_RATE", ax = ax)
axis.set(title = 'APR_RATE distribution over years')
plt.savefig('figs/apr_distribution.png')
plt.show()
