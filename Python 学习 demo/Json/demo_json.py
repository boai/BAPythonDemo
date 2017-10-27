
import json

# Python 字典类型转换为 JSON 对象

data = {
    'no' : 1,
    'name' : 'boai',
    'url' : 'http://www.boaihome.com'
}

jsonString = json.dumps(data)
print('Python 原始数据：', repr(data))
print('Python 字典转 json：', jsonString)

# 将 JSON 对象转换为 Python 字典

data2 = json.loads(jsonString)
print("data2['name'] = ", data2['name'])

# 写入 JSON 数据
with open('data.json', 'w') as f:
    json.dump(data, f)

# 读取数据
with open('data.json', 'r') as f:
    data = json.load(f)
    print('json 文件读取：', data)

