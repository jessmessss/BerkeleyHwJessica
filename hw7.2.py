import seaborn as sns 
import matplotlib.pyplot as plt 

planets = sns.load_dataset('planets')

plt.figure(figsize=(10, 6))
scatter_plot = sns.scatterplot(
data=planets, 
x= 'orbital_period',
y= 'mass' ,
hue = 'method',
palette='deep',
edgecolor=None 
)
scatter_plot.set(xscale='log', yscale='log')

scatter_plot.set_title('orbital period and mass relation', fontsize=12)
scatter_plot.set_xlabel('Orbital period (days)', fontsize=12)
scatter_plot.set_ylabel('mass', fontsize=12)

plt.legend(title= 'orbital periods and mass')

plt.show()