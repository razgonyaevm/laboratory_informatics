import xmltodict
import yaml

with open('main_directory/main.xml') as file:
    dict_data = xmltodict.parse(file.read())

with open('main_directory/file_program_2.yaml', 'w') as file:
    yaml.dump(dict_data, file, allow_unicode=True)

