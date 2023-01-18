# Import CSV 

import csv

# Import Counter

from collections import Counter

# Import MatPlotLib Library and Assign a Name to it for Drawing Graphs

from matplotlib import pyplot as plt

# Import NumPy

import numpy as np

# print(plt.style.available)

# Plot Style

plt.style.use('ggplot')

# Import Data from CSV (comma-separated-value) File

with open('C:/Users/Frank/Documents/Python/5_MatPlotLib/4_Example/data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()

    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

# print(language_counter)

languages = []
popularity = []

for item in language_counter.most_common(5):
    languages.append(item[0])
    popularity.append(item[1])

plt.bar(languages, popularity)

# Plot information

plt.xlabel('Languages')

plt.ylabel('Popularity')

plt.title('Popularity versus Language')

# Padding/Margin

plt.tight_layout()

# Save Graph Programmatically

plt.savefig('C:/Users/Frank/Documents/Python/5_MatPlotLib/4_Example/Plot.svg')

# Make Plot

plt.show()