import myDictionary
from myDictionary import riddlesExt

index = 0
addingNumber = [1,2,3,4,5,6,7]

create_dict = 'cesar'
# print(create_dict)
#
# if create_dict != '':
#     index +=1
#     newDict = create_dict + str(index)
#     print(newDict)
# else:
#     print('not passing')

dictionaries = []

def addingDict():

    index = 0
    while index >= 0 and index < 4:
        writeName = input('write your name: ')
        #index +=1
        #newDict = writeName + str(index)
        # newDict = writeName
        newDict ={
        'name': writeName,
        'score': score,
        'player': number
        }
        dictionaries.append(newDict)
        print(newDict)
        index +=1

addingDict()

print("dictionaries[1]['name'] " + dictionaries[1]['name'])

# print(dictionaries)
# ##print('this is the dictionary numer 3 ' + str(dictionaries[3]))
# print(riddlesExt[1]['riddle'])
#
# save_user = []
# def user_Information(turn):
#     newDict = user_info + string(turn)
#     newDict = {
#     'userName': '',
#     'score': '',
#     'number': ''
#     }
#     save_user.append(newDict)
