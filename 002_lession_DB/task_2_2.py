import lxml.etree as ET
import os

# API KEY:  7a4bda9ee0e5cb5fd7dbccb9f78b6613
data_path = os.path.join(os.getcwd(), 'data')
# path =os.path.join(data_path, 'data-25433-2020-03-27.xml')
path =os.path.join('data', 'data-25433-2020-03-27.xml')
tree = ET.parse(path)
# получаем корневой DOM элемент
root = tree.getroot()

# выбираем все дочерние элементы
children = root.getchildren()

for i, obj in enumerate(children):
    print('{i} place'.format(i = i+1))
    print('{} - {}, is located at '.format(obj.find('./Address').text, obj.find('./ObjectName').text))
    for coord in obj.findall('./geoData/coordinates'): print(coord.text)