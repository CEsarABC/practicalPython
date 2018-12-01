import myDictionary
from myDictionary import riddles

index = 0
addingNumber = [1,2,3,4,5,6,7]

create_dict = 'cesar'
print(create_dict)

if create_dict != '':
    index +=1
    newDict = create_dict + str(index)
    print(newDict)
else:
    print('not passing')

dictionaries = []
def addingDict():
    for x in addingNumber:
        index +=1
        newDict = create_dict + str(index)
        print(newDict)
        newDict ={
        'brand': 'ford',
        'model': '',
        'year': 1966
        }
        dictionaries.append(newDict)
        print(newDict)
print(dictionaries)
print('this is the dictionary numer 3 ' + str(dictionaries[3]))
print(riddles[1])

save_user = []
def user_Information(turn):
    newDict = user_info + string(turn)
    newDict = {
    'userName': '',
    'score': '',
    'number': ''
    }
    save_user.append(newDict)
