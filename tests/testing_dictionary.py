import myDictionary
from myDictionary import riddlesExt


user_list = {
"name": "",
"number": "",
"score": ""
}

def new_user():
    print('this function needs to insert the name in a list')
    user = input('this is my name: ')
    user_list["name"] = user
    print(user_list)

new_user()
