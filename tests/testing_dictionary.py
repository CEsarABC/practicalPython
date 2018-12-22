import myDictionary
from myDictionary import riddlesExt


user_list = {
"name": "",
"number": "",
"score": ""
}
new_dict = {}
def new_user():
    print('this function needs to insert the name in a list')
    user_list["name"] = input('this is my name: ')
    # new_dict.append(user_list["name"])
    user_list["number"] = input('this is my number: ')
    user_list["score"] = input('this is my score: ')
    riddlesExt.append(user_list)
    print(user_list)

new_user()

print(riddlesExt)
