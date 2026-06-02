import csv

sales = {}

def calc_total_sales(sales):
    total = sum(sales.values())
    print(f"総売上: {total:,}円")

def calc_average_sales(sales):
    ave = sum(sales.values()) / len(sales)
    print(f"平均売上: {ave:,.0f}円")

def get_max_sale(sales):
    name, sale = max(sales.items(), key=lambda x: x[1])
    print(f"最高売上: {name} {sale:,}円")
    return name, sale

def show_high_sales(sales, target):
    print(f"売上{target:,}円以上")

    for name, amount in sales.items():
        if amount >= target:
            print(name)

with open("sales.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader: sales[row["名前"]] = int(row["売上"])

calc_total_sales(sales)

calc_average_sales(sales)

get_max_sale(sales)

show_high_sales(sales, 100000)
