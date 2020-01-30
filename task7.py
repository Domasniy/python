import json

try:
    with open('company.txt',encoding='utf-8') as f:
        companies = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f}
except IOError:
    print('Ошибка чтения файла')

prib_companies = [x for x in companies.values() if x > 0]
average_profit = {'average_profit': round(sum(prib_companies) / len(prib_companies), 2)}
try:
    with open('result.json','w',encoding='utf-8') as f:
        json.dump([companies, average_profit], f, ensure_ascii=False, indent=4)
except IOError:
    print('Ошибка записи файла')