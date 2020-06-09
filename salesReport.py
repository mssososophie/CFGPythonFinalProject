import csv

# with open('Copy of sales.csv', 'r') as csv_file:
#     spreadsheet = csv.DictReader(csv_file)
#     print(spreadsheet)
#     for row in spreadsheet:
#         print(dict(row))

#  OPTION 1 V

# sales = csv.DictReader(open("Copy of sales.csv"))
#
# for col in input_file:
#     sales = col['sales']
#
# totalSales = sum(sales)
# Print(totalSales)

# OPTION 2 V

def sumSales():
    with open('Copy of sales.csv', 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)

        totalSales = 0

        for row in spreadsheet:
            # totalSales = totalSales + int(row['sales'])
            totalSales += int(row['sales'])
    print(f'The total number of sales is {totalSales}')

sumSales()

def monthlySales():
    with open('Copy of sales.csv', newline='') as csv_file:
        data = csv.DictReader(csv_file)

        for row in data:
            print(row['month'], row['sales'])

monthlySales()






# ******** Printing rows and cols ********

# for row in input_file:
#     print (row)

# for col in input_file:
#     print (dict(col))