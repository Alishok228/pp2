import json

# Чтение данных из файла JSON
with open("C:/Users/ПК/Desktop/python/pp2/tsis4", 'r') as file:
    data = json.load(file)

# Форматированный вывод данных
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)
for item in data['imdata']:
    dn = item['fabricPathEp']['attributes']['dn']
    description = item['fabricPathEp']['attributes'].get('descr', '')
    speed = item['fabricPathEp']['attributes'].get('speed', 'inherit')
    mtu = item['fabricPathEp']['attributes'].get('mtu', '')
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))
