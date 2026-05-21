import pandas as pd

product = ["Apples","Bannas","Oranges","Grapes","Pineapples"]

sales = [150,200,180,90,60]

sales_serie = pd.Series(sales,index=product)

print(sales_serie)

print(sales_series['Grapes'])

total