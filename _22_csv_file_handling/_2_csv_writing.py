import csv

fieldnames = ["rno","name"]
rows = [[1,"Bharati"],[2,"Shruti"]]

with open(r"C:\Users\vashi\OneDrive\Documents\GitHub\DS140823\_22_csv_file_handling\test.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(fieldnames)
    writer.writerows(rows)