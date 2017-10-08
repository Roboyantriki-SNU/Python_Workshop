while True:
    print('Enter the username')
    username = input()
    if (username != 'Alex'):
        continue
    print('Enter the password')
    pws = input()
    if (pws == 'dog'):
        break;
    else:
        print('Access not granted')
print('Access granted')
