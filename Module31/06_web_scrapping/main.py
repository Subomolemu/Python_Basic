import requests
import re

my_request = requests.get('http://www.columbia.edu/~fdc/sample.html')

date_list = re.findall(r'>\b.+\b<.h3>', my_request.text)

new_list = list(map(lambda string: ''.join(re.findall(r'.', string))[1:-5], date_list))
print(new_list)