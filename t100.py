number = 1
door=[]
for each in range(100):
    door.append(False)

def ajtonyitas(number) :
    if number == 101:
        output()
    else:
        for each in range(100) :
            if (each+1) % number == 0:
                if door[each] == False:
                    door[each]=True
                else :
                    door[each]=False
            number = number + 1
        ajtonyitas(number)


def output() :
    result=[]
    for each in range(100): 
        if door[each] == True :
            result.append(int(door)+1)
    print (result)

ajtonyitas(number)