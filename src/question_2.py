from readit import read_data, create_gender_column
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
  

df = create_gender_column(read_data('data/APR_tidy.csv'))


#print(df['Gender'].unique()) - Unknown indicate that gender is not specified for that sport

#Lets consider Unknown to be a particular gender using a variale, so that no data is left out 
#unknown_gender = 'Men'
#df['Gender'] = df['Gender'].apply(lambda x: 'Men' if x == 'Unknown' else x)

fig, ax1 = plt.subplots(figsize=(15, 10))
sns.set_style('darkgrid')
print(f"Sports of type mixed = {df[df['Gender'] == 'Mixed']['SPORT_NAME'].unique()}")
print(f"Sports with no gender specified = {df[df['Gender'] == 'Unknown']['SPORT_NAME'].unique()}")
print('Ignoring the above we boxplot the following on rest of the data:')
axis = sns.boxplot(data=df[df.Gender.isin(['Men','Women'])], x="APR_RATE_YEAR", y="APR_RATE", hue="Gender", ax = ax1)
axis.set(title = 'APR_RATE Box plot distribution over years across all sports for Men and Women')
plt.savefig('figs/men_women_apr_distribution_box.png')
plt.show()

fig, ax2 = plt.subplots(figsize=(15, 10))
sns.set_style('darkgrid')
print('Using violinplot on rest of the data gives:')
axis = sns.violinplot(data=df[df.Gender.isin(['Men','Women'])], x="APR_RATE_YEAR", y="APR_RATE", hue="Gender", split=True, ax = ax2)
axis.set(title = 'APR_RATE Violin plot distribution over years across all sports for Men and Women')
plt.savefig('figs/men_women_apr_distribution_violin.png')
plt.show()
