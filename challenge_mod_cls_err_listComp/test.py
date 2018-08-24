import csv
with open('nfl_suspensions.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    data = list(spamreader)
    for row in data[0:5]:
        print(row)
    # data = list(spamreader)
    # data_row = data[1]
    # print(data_row[0:3])