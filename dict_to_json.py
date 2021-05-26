#import json module
import json

dict = {"name": "omkar", "lname": "patil"}
#dumps converts dictionary to json string
json_st = json.dumps(dict)
print(json_st)
