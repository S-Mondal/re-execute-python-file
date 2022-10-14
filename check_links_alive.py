import csv
import requests

# opening output file to write
f = open("output.csv",'w+')
output_writer = csv.writer(f)

# adding headers
output_writer.writerow(['status_code','link'])

# reading file containing links
with open("open-images-dataset-train0.tsv") as file:
    tsv_file = csv.reader(file, delimiter="\t")

    # getting columns
    columns = next(tsv_file)[0]

    for row in tsv_file:
        # adding http:// if not added to the link
        if "http" not in row[0]:
            row[0] = "http://"+str(row[0]).strip()

        # getting url response
        response = requests.get(row[0], timeout=10, verify=False)
        print(response.status_code)

        # storing the status_code along with links
        output_writer.writerow([response.status_code, row[0]])
    
# closing io reader
f.close()
