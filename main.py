import csv

def save_tinkergarten_data():
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
                # correct data contains Tinkergarden url in landing_page column
                writer.writerow(row)
                classes = classes + 1
            
        print('Saving {} correct classes'.format(classes))

def save_tinkergarten_bad_data():
    with open('winnie_leaders.csv') as csv_file, open('bad_data.csv', 'w') as out:
        bad_data_rows = 0

        fieldnames = ["primary_name", "secondary_name", "city", "state", "latitude", "longitude", "leader_name", "bio", "landing_page"]
        writer = csv.DictWriter(out, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()

        csv_reader = csv.DictReader(
            csv_file,
            restval='',
            quoting=csv.QUOTE_MINIMAL,
        )

        for row in csv_reader:
            landing_page = row.get('landing_page').strip()
            if landing_page.startswith('http'):
                # correct data contains Tinkergarden url in landing_page column
                continue
            else:
                writer.writerow(row)
                bad_data_rows = bad_data_rows + 1
            
        print('Saving {} invalid rows'.format(bad_data_rows))

def main():
    save_tinkergarten_data()
    save_tinkergarten_bad_data()

if __name__== "__main__":
    main()