import csv

with open('winnie_leaders.csv') as csv_file, open('tinkergarden.csv', 'w') as out:
    classes = 0

    fieldnames = ["primary_name", "secondary_name", "city", "state", "latitude", "longitude", "leader_name", "bio", "landing_page"]
    writer = csv.DictWriter(out, fieldnames=fieldnames)
    writer.writeheader()

    csv_reader = csv.DictReader(
        csv_file,
        restval='',
        quoting=csv.QUOTE_MINIMAL,
    )
    for row in csv_reader:
        landing_page = row.get('landing_page').strip()
        if landing_page.startswith('http'):
            writer.writerow(row)
            classes = classes + 1
        else:
            park_name = row.get('primary_name').strip()
            print(park_name)
        
    print(classes)