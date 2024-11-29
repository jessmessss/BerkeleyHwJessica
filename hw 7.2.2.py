import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 

planets = sns.load_dataset('planets')

method_counts =  planets.groupby (['year', 'method']).size().unstack(fill_value=0)

method_counts.plot(
kind='bar',
stacked=True, 
figsize=(12, 8),
colormap= 'coolwarm',
width=1
)
plt.title('total number of exoplanets by year', fontsize=12)
plt.xlabel('Year', fontsize=12)
plt.ylabel('# of exoplanets')
plt.legend(title='Discovery of planets', bbox_to_anchor=(1,1), loc='upper left')
plt.tight_layout()
plt.show()
