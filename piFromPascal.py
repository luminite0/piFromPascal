'''
num = 1
thing = 2
mylist = [1]
# get all the third terms
for i in range(100000):
    num += thing
    mylist.append(num)
    thing += 1

# take the reciprocal of each term
for i in range(len(mylist)):
    mylist[i] = 1 / mylist[i]
# set up a counter that makes the signs of the terms ++--++--++--++--etc.
thing = 0
for k in range(len(mylist)):

    if thing == 0:
        thing += 1
       
    elif thing == 1:
        thing += 1
        
    elif thing == 2:
        mylist[k] *= -1
        thing += 1
        
    elif thing == 3:
        mylist[k] *= -1
        thing = 0
        
    else:
        pass
# print the terms
print(mylist)
answer = 0
# add the terms
for item in range(len(mylist)):
    answer += mylist[item]
# display the terms
closeToPi = answer + 2
print('\n\n\n\n\n\n\n', 'Here is the number (very close to pi):')
print(closeToPi, '\n\n\n')


# the other way to do it
'''


num = 0
addNum = 1
mylist = []
i = 0
count = 0
endSum = 0
for i in range(10000000000):
    # get third term
    num += addNum
    mylist.append(num)
    addNum += 1
    # take reciprocal of each number
    mylist[0] = 1 / mylist[0]
    # ++--++-- etc.
    if count == 0:
        mylist[0] *= 1
        endSum += mylist[0]
        del(mylist[0])
        count += 1
    elif count == 1:
        mylist[0] *= 1
        endSum += mylist[0]
        del(mylist[0])
        count += 1
    elif count == 2:
        mylist[0] *= -1
        endSum += mylist[0]
        del(mylist[0])
        count += 1
    elif count == 3:
        mylist[0] *= -1
        endSum += mylist[0]
        del(mylist[0])
        count = 0
    else:
        print("ERROR")
print(endSum + 2)
