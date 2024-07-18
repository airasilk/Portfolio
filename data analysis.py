# Importing Libraries
import matplotlib.pyplot as plt
import tabulate
import seaborn as sns
import numpy as np
import pandas as pd

data = [['Date',  'Mood',	 'Weather', 	'Enough water?',  	   'Bedtime', 	'Pages read'],
        ['06/25',	3,	'Rainy',	'Yes',	'Late',	3],
        ['06/26',	2,	'Cloudy',	'Yes',	'Late',	0],
        ['06/27',	2,	'Sunny',	'No',	'Late',	0],
        ['06/28',	4,	'Sunny',	'Yes',	'Early',	2],
        ['06/29',	3,	'Rainy',	'Yes',	'Late',	4],
        ['06/30',	4,	'Rainy',	'Yes',	'Early',	0],
        ['07/01',	3,	'Rainy',	'Yes',	'On time',	2],
        ['07/02',	5,	'Sunny',	'Yes',	'On time',	4],
        ['07/03',	3,	'Sunny',	'Yes',	'Late',	5],
        ['07/04',	3,	'Sunny',	'Yes',	'Late',	8],
        ['07/05',	4,	'Rainy',	'Yes',	'Early',	3],
        ['07/06',	3,	'Rainy',	'Yes',	'On time',	3],
        ['07/07',	2,	'Cloudy',	'No',	'Late',	1],
        ['07/08',	2,	'Sunny',	'No',	'Late',	0],
        ['07/09',	4,	'Sunny',	'Yes',	'On time',	6],
        ['07/10',	4,	'Sunny',	'No',	'Late',	8],
        ['07/11',	3,	'Sunny',	'Yes',	'On time',	3],
        ['07/12',	2,	'Cloudy',	'No',	'Late',	0],
        ['07/13',	2,	'Rainy',	'No',	'Late',	5],
        ['07/14',	3,	'Cloudy',	'No',	'Late',	3],
        ['07/15',	3,	'Rainy',	'Yes',	'On time',	2],
        ['07/16',	5,	'Sunny',	'Yes',	'Early',	9]]

# Add the data in a DataFrame since we are using pandas
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

# Map mood vs bedtime
# mood_vs_bedtime = {}
# for row in data[1:]:
#     mood = float(row[1])
#     bedtime = row[4]
#     if bedtime in mood_vs_bedtime:
#         mood_vs_bedtime[bedtime].append(mood)
#     else:
#         mood_vs_bedtime[bedtime] = [mood]

# print("\nMood vs Bedtime:")

# for bedtime, mood in mood_vs_bedtime.items():
#  print(f"Bedtime: {bedtime}, Mood: {mood}")
# # Now let's plot a bargraph of average mood vs average bedtime
# # This is to understand how my bedtime affects my mood
# plt.bar(mood_vs_bedtime.keys(), [sum(times) / len(times)  for times in mood_vs_bedtime.values()])
# plt.xlabel("Bedtime")
# plt.ylabel("Mood")
# plt.title("Mood vs Bedtime")
# plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
# plt.tight_layout()  # Adjust layout to prevent labels from overlapping
# plt.show()



# mood_vs_weather = {}
# for row in data[1:]:
#     mood = float(row[1])
#     weather = row[2]
#     if weather in mood_vs_weather:
#         mood_vs_weather[weather].append(mood)
#     else:
#         mood_vs_weather[weather] = [mood]

# print("\nMood vs Weather:")

# for weather, mood in mood_vs_weather.items():
#  print(f"Weather: {weather}, Mood: {mood}")
# # Now let's plot a bargraph of average mood vs average bedtime
# # This is to understand how my bedtime affects my mood
# plt.bar(mood_vs_weather.keys(), [sum(times) / len(times)  for times in mood_vs_weather.values()])
# plt.xlabel("Weather")
# plt.ylabel("Mood")
# plt.title("Mood vs Weather")
# plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
# plt.tight_layout()  # Adjust layout to prevent labels from overlapping
# plt.show()


# mood_vs_bedtime = {}
# for row in data[1:]:
#     mood = float(row[1])
#     bedtime = row[4]
#     if bedtime in mood_vs_bedtime:
#         mood_vs_bedtime[bedtime].append(mood)
#     else:
#         mood_vs_bedtime[bedtime] = [mood]
# print("\nMood vs Bedtime:")
# for bedtime, mood in mood_vs_bedtime.items():
#  print(f"Bedtime: {bedtime}, Mood: {mood}")
# # Now let's plot a bargraph of average sleep time vs average wake up time
# #This is purely to understand how many hours ia a good sleep for me
# plt.figure(figsize=(8, 6))  # Adjust figure size if needed
# plt.boxplot([mood_vs_bedtime[bedtime] for bedtime in mood_vs_bedtime], labels=mood_vs_bedtime.keys(), patch_artist=True,
#             boxprops=dict(facecolor='lightblue', edgecolor='blue'),
#             capprops=dict(color='blue'),
#             whiskerprops=dict(color='blue'),
#             flierprops=dict(marker='o', markerfacecolor='blue', markersize=8))
# plt.xlabel("Bedtime")
# plt.ylabel("Mood")
# plt.title("Mood vs Bedtime (Boxplot)")
# plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels
# plt.tight_layout()
# plt.show()