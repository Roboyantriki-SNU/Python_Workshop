print('Hello world')
print('what is your name')
myName = input()
print('It is good to meet you'+myName)
print('The length of your name is:')
print(len(myName))
print('what is your age')
myAge = input()
if myName == 'Alice':
    print('hi '+myName)
elif (int(myAge) < 18):
    print('you are kid')
else:
    print('You are not alice and not a kid')

print('you will be' +str(int(myAge)+1)+'in a year')
