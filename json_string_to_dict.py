#import json module
import json

#json String
json_string = '{"name":"xyz", "age":20, "height": 5.7, "hobbies":["football", "cricket", "badminton"]}'
#json.loads methods returns a dictionary.
dict = json.loads(json_string)
print(dict)
print()
print()
print(dict['hobbies'])
print()
print()
#printing json string with indent 4.
print(json.dumps(dict, indent=4))