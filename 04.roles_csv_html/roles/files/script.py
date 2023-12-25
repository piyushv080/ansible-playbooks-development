import pandas as pd

csvFile = pd.read_csv (r'/root/ansible_roles/sample.csv')

csvFile.to_html(r'/root/ansible_roles/main.html')
 
# assign it to a variable (string)
html_file = csvFile.to_html()
