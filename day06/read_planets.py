import csv

filename = "planets.csv"



with open(filename) as csvfile:
    planet_reader = csv.DictReader(csvfile)
    for row in planet_reader:
        print(row)
        print(row['Planet name'], row['Distance (AU)'])



# with open(filename) as csvfile:
#     planet_reader = csv.reader(csvfile, delimiter=',')
#     title = planet_reader.__next__()
#     print(f"title: {title}")
#     for row in planet_reader:
#         #print(', '.join(row))
#         print(row[0])



# with open(filename) as csvfile:
#     planet_reader = csv.reader(csvfile, delimiter=',')
#     for row in planet_reader:
#         #print(', '.join(row))
#         print(row[0])        