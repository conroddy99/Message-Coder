
alph = ['e','q','A','V','s','u','y','?',' ','E','W','M','!','k','B','h','Q','R','G','p','m','f','w',',','b','n','T','l','D','C','X','Y','F','v','r','K','H','Z','t','z','x','O','I','.','a','N','j','g','o','c','d','i','J','L','P','S','U']

def splt(text):
    return [char for char in text]

def org(num,o,cryptororiginal):
    if o == 1:
        num = num + cryptororiginal
        if num > 56:
            num = num-57
    if o == 2:
        num = num - cryptororiginal
        if num < 0:
            num = num + 57
    return num

def tocode(text,cryptororiginal):
    codedtext = []
    x = splt(text)
    cusing = cryptororiginal
    for i in x:
        cusing += 1
        if cusing == (cryptororiginal+10):
            cusing = cryptororiginal

        # Find what index character to be encoded is in alph
        index = 0
        for j in range(len(alph)):
            if alph[j] == i:
                index = j
        
        # Use index to then encode character
        codedtext.append(alph[org(index,1,cusing)])
        
    ct = ''.join(codedtext)
    return ct

def decode(text,cryptororiginal):
    codedtext = []
    x = splt(text)
    cusing = cryptororiginal
    for i in x:
        cusing += 1
        if cusing == (cryptororiginal + 10):
            cusing = cryptororiginal

        # Find what index character to be decoded is in alph
        index = 0
        for j in range(len(alph)):
            if alph[j] == i:
                index = j
        
        codedtext.append(alph[org(index,2,cusing)])

    ct = ''.join(codedtext)
    return ct

run = 1
while run == 1:
    option = int(input('Enter 1 to code a message or 2 do decode a message:'))
    text = input("Enter text to be translated:")
    cryptororiginal = int(input('Please enter your encryption number:'))
    print ('\n')
    if option ==1:
        print(tocode(text,cryptororiginal))
    elif option ==2:
        print(decode(text,cryptororiginal))
    run = int(input('Enter \"1\" to run again:'))