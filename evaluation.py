print("Test Eval")
import requests
equation = 'x1 + 2 * x2 + x3'
headers ={}
aio_url = "https://io.adafruit.com/api/v2/binu1206/feeds/equation"
x = requests.get(url=aio_url, headers=headers, verify=False)
data = x.json()
print(data["last_value"])
equation = data["last_value"]

def modify_value(x1, x2, x3):
    result = eval(equation)
    print(result)
    return result

a = 4
b = 3
c = 3
d = modify_value(a,b,c)
print(d)