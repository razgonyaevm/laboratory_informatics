import pandas as pd
import xmltodict

with open('main_directory/main.xml') as file:
    dict_data = xmltodict.parse(file.read())


for i in range(len(dict_data['site']['date'])):
    df = pd.DataFrame(dict_data['site']['date'][i]['Sheet'])
    df.to_csv(f'main_directory/csv/output_{dict_data["site"]["date"][i]["date_short"]}.csv', index=False)
