import json


def insert_student():
    user_input = input("enter students name")
    file_obj = open('stud.txt','r')
    file_line = file_obj.readline()
    file_obj.close()

    json_obj = json.loads(file_line)
    json_obj["student"].append(user_input)
    json_str = json.dumps(json_obj)

    file_obj = open('stud.txt','w')
    file_obj.write(json_str)
    file_obj.close()
insert_student()
    

