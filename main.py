import csv

# Quick and Dirty Python script to convert the exported csv data from the SQL commands I copied to
# csv data that's usable by Health Importer by Paradox Customs
#
# Processed will be a 2d array representing the final csv to be exported.
# It would be more memory-efficient if I didn't store the whole thing, but I was lazy.
# It's initialized with the header row.
processed = [[
    'start',
    'end',
    'weight (kg)',
    'weight (lbs)',
    'heart rate (weird)',
    'heart rate (count/min)',
    'steps','distance (m)',
    'resting energy',
    'active energy',
    'flights climbed',
    'stand']]

# Open the samples file that was exported from the SQLite database
with open('data/samples_better.csv', 'rb') as f:
    reader = csv.reader(f)

    # Transform a row with a datatype
    # to a larger row
    for row in reader:
        # 3 - Weight
        if row[3] == '3' and row[4] != '':
            processed.append([row[0], row[1], row[4], row[5], '', ''])
        # 5 - Heart Rate
        if row[3] == '5':
            processed.append([row[0], row[1], '', '', row[4], row[5]])
        # 7 - Steps
        if row[3] == '7':
            processed.append([row[0], row[1], '', '', '', '', row[4]])
        # 8 - Distance meters
        if row[3] == '8':
            processed.append([row[0], row[1], '', '', '', '', '',row[4]])
        # 9 - Resting energy
        if row[3] == '9':
            processed.append([row[0], row[1], '', '', '', '', '','',row[4]])
        # 10 - Active energy
        if row[3] == '10':
            processed.append([row[0], row[1], '', '', '', '', '','','',row[4]])
        # 12 - Flights climbed
        if row[3] == '12':
            processed.append([row[0], row[1], '', '', '', '', '','','','',row[4]])
        # 75 - Stand
        if row[3] == '75':
            processed.append([row[0], row[1], '', '', '', '', '','','','','',row[4]])

# Export the processed 2d array as a csv with unix newlines
with open('data/samples_processed.csv', 'w') as f:
    for row in processed:
        f.write(','.join(row))
        f.write('\n')