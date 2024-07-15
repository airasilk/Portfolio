# Importing Libraries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# flo_df = sns.load_dataset('iris')
# # Calculate the correlation matrix
# # Convert the 'species' column to numerical values
# flo_df['species'] = pd.factorize(flo_df['species'])[0]
# correlation_matrix = flo_df.corr()
# # Create a heatmap
# sns.heatmap(correlation_matrix, annot=True)
# # Display the heatmap
# plt.show()

# flo_df = sns.load_dataset('iris')
# sns.pairplot(flo_df, hue='species')
# plt.show()

# flo_df = sns.load_dataset('iris')
# print(flo_df)
# plt.title('Iris Dataset Histogram')
# plt.hist(flo_df.sepal_width, bins=5)
# plt.show()

# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
# apples = [0.89, 0.72, 0.82, 0.49, 0.3, 0.79, 1.08]
# oranges = [0.5, 0.6, 0.34, 0.89, 0.63, 0.55, 0.98]
# width = 1.2  # Width of the bars
# plt.bar(years, apples, width, label='apples')
# plt.bar([x + width for x in years], oranges, width, label='oranges')  # Offset x-axis for oranges
# plt.xlabel('Years')
# plt.ylabel('Production')
# plt.title('Apples and Oranges Production Over Years')
# plt.legend()
# plt.show()

# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
# apples = [0.89, 0.72, 0.82, 0.49, 0.3, 0.79, 1.08]
# Apply style before plotting
#sns.set_style('whitegrid') 
#sns.lineplot(x=years, y=apples, marker='o')  # Pass lists directly
#plt.xlabel('Years', color='blue')
#plt.ylabel('Apples', color='blue')
# plt.title('Apples Production Over Years')
# plt.legend(['apples'])
# plt.show()


# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
# apples = [0.89, 0.72, 0.82, 0.49, 0.3, 0.79, 1.08]
# oranges = [0.5, 0.6, 0.34, 0.89, 0.63, 0.55, 0.98]
# plt.plot( years, apples)
# plt.plot(years, oranges)
# plt.xlabel('Years')
# plt.ylabel('Apples')
# plt.title('Apples Production Over Years')
# plt.legend(['apples'])
# plt.show()

# tips_f = sns.load_dataset("tips")
# print(tips_f)
# sns.barplot(x="day", y="total_bill", hue = 'sex', data=tips_f)