'''
heroGame beta-0.1
vitamin
2017-09-06

'''
hp = 100
print('welcome heroGame world!')
print("|the world like this :####, 'a' for left, 'd' for right")
name = input('input your name: ')
if  name :
    pass
else :
    name = 'player02'
usermsg = [name, hp]
print("your hero's name is:", usermsg[0], ", your hero's hp is:", usermsg[1])
print("and now you are here: *#### |'a' for left, 'b' for right|")
userinput = input()
if userinput == 'd':
    print("you are here #*###")
if userinput == 'a':
    print("you are here *####")
