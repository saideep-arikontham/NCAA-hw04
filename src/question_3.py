from readit import read_data, create_gender_column
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
 

fig, ax = plt.subplots(figsize=(15, 10),nrows=1,ncols=2)
 

df = read_data('data/APR_tidy.csv')

plot_df = df[['SPORT_NAME','APR_RATE_YEAR','APR_RATE']].groupby(['SPORT_NAME','APR_RATE_YEAR']).mean().reset_index()

gender_df = create_gender_column(plot_df)

gender_df['Gender'] = gender_df['Gender'].apply(lambda x: 'Men' if x == 'Unknown' else x)

men_plot = gender_df[gender_df['Gender'] == 'Men']
women_plot = gender_df[gender_df['Gender'] == 'Women']

sns.set_style('darkgrid')
axis1 = sns.boxplot(data=men_plot, x="SPORT_NAME", y="APR_RATE", ax = ax[0])
ax[0].set_title('Distribution of APR Rate for each Men sports averaged over all time')
ax[0].tick_params(axis='x', rotation=90)


axis2 = sns.boxplot(data=women_plot, x="SPORT_NAME", y="APR_RATE", ax = ax[1])
axis2.set(title = 'APR_RATE distribution over years')
ax[1].tick_params(axis='x', rotation=90)
ax[1].set_title('Distribution of APR Rate for each Men sports averaged over all time')
plt.savefig('figs/for_men_for_women.png')
plt.show()
