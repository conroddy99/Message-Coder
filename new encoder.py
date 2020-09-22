def splt(text):
    return [char for char in text]
def org(num,o,cryptororiginal):
    if o ==1:
        num = num + cryptororiginal
        if num > 57:
            num = num-58
    if o == 2:
        num = num - cryptororiginal
        if num < 0:
            num = num + 58
    return num
def tocode(text,cryptororiginal):
    codedtext = []
    alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '.', ',', '?', '!']
    x = splt(text)
    cusing = cryptororiginal
    for i in x:
        cusing += 1
        if cusing == (cryptororiginal+3):
            cusing = cryptororiginal
            cusing += 1

        cryptor = cusing
        print(cusing)
        if i == alph[0]:
            codedtext.append(alph[org(0,1,cryptor)])
        elif i == alph[1]:
            codedtext.append(alph[org(1,1,cryptor)])
        elif i == alph[2]:
            codedtext.append(alph[org(2,1,cryptor)])
        elif i == alph[3]:
            codedtext.append(alph[org(3,1,cryptor)])
        elif i == alph[4]:
            codedtext.append(alph[org(4,1,cryptor)])
        elif i == alph[5]:
            codedtext.append(alph[org(5,1,cryptor)])
        elif i == alph[6]:
            codedtext.append(alph[org(6,1,cryptor)])
        elif i == alph[7]:
            codedtext.append(alph[org(7,1,cryptor)])
        elif i == alph[8]:
            codedtext.append(alph[org(8,1,cryptor)])
        elif i == alph[9]:
            codedtext.append(alph[org(9,1,cryptor)])
        elif i == alph[10]:
            codedtext.append(alph[org(10,1,cryptor)])
        elif i == alph[11]:
            codedtext.append(alph[org(11,1,cryptor)])
        elif i == alph[12]:
            codedtext.append(alph[org(12,1,cryptor)])
        elif i == alph[13]:
            codedtext.append(alph[org(13,1,cryptor)])
        elif i == alph[14]:
            codedtext.append(alph[org(14,1,cryptor)])
        elif i == alph[15]:
            codedtext.append(alph[org(15,1,cryptor)])
        elif i == alph[16]:
            codedtext.append(alph[org(16,1,cryptor)])
        elif i == alph[17]:
            codedtext.append(alph[org(17,1,cryptor)])
        elif i == alph[18]:
            codedtext.append(alph[org(18,1,cryptor)])
        elif i == alph[19]:
            codedtext.append(alph[org(19,1,cryptor)])
        elif i == alph[20]:
            codedtext.append(alph[org(20,1,cryptor)])
        elif i == alph[21]:
            codedtext.append(alph[org(21,1,cryptor)])
        elif i == alph[22]:
            codedtext.append(alph[org(22,1,cryptor)])
        elif i == alph[23]:
            codedtext.append(alph[org(23,1,cryptor)])
        elif i == alph[24]:
            codedtext.append(alph[org(24,1,cryptor)])
        elif i == alph[25]:
            codedtext.append(alph[org(25,1,cryptor)])
        elif i == alph[26]:
            codedtext.append(alph[org(26,1,cryptor)])
        elif i == alph[27]:
            codedtext.append(alph[org(27,1,cryptor)])
        elif i == alph[28]:
            codedtext.append(alph[org(28,1,cryptor)])
        elif i == alph[29]:
            codedtext.append(alph[org(29,1,cryptor)])
        elif i == alph[30]:
            codedtext.append(alph[org(30,1,cryptor)])
        elif i == alph[31]:
            codedtext.append(alph[org(31,1,cryptor)])
        elif i == alph[32]:
            codedtext.append(alph[org(32,1,cryptor)])
        elif i == alph[33]:
            codedtext.append(alph[org(33,1,cryptor)])
        elif i == alph[34]:
            codedtext.append(alph[org(34,1,cryptor)])
        elif i == alph[35]:
            codedtext.append(alph[org(35,1,cryptor)])
        elif i == alph[36]:
            codedtext.append(alph[org(36,1,cryptor)])
        elif i == alph[37]:
            codedtext.append(alph[org(37,1,cryptor)])
        elif i == alph[38]:
            codedtext.append(alph[org(38,1,cryptor)])
        elif i == alph[39]:
            codedtext.append(alph[org(39,1,cryptor)])
        elif i == alph[40]:
            codedtext.append(alph[org(40,1,cryptor)])
        elif i == alph[41]:
            codedtext.append(alph[org(41,1,cryptor)])
        elif i == alph[42]:
            codedtext.append(alph[org(42,1,cryptor)])
        elif i == alph[43]:
            codedtext.append(alph[org(43,1,cryptor)])
        elif i == alph[44]:
            codedtext.append(alph[org(44,1,cryptor)])
        elif i == alph[45]:
            codedtext.append(alph[org(45,1,cryptor)])
        elif i == alph[46]:
            codedtext.append(alph[org(46,1,cryptor)])
        elif i == alph[47]:
            codedtext.append(alph[org(47,1,cryptor)])
        elif i == alph[48]:
            codedtext.append(alph[org(48,1,cryptor)])
        elif i == alph[49]:
            codedtext.append(alph[org(49,1,cryptor)])
        elif i == alph[50]:
            codedtext.append(alph[org(50,1,cryptor)])
        elif i == alph[51]:
            codedtext.append(alph[org(51,1,cryptor)])
        elif i == alph[52]:
            codedtext.append(alph[org(52,1,cryptor)])
        elif i == alph[53]:
            codedtext.append(alph[org(53,1,cryptor)])
        elif i == alph[54]:
            codedtext.append(alph[org(54,1,cryptor)])
        elif i == alph[55]:
            codedtext.append(alph[org(55,1,cryptor)])
        elif i == alph[56]:
            codedtext.append(alph[org(56,1,cryptor)])
    ct = ''.join(codedtext)
    return ct
def decode(text,cryptororiginal):
    codedtext = []
    alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','.',',','?','!']
    x = splt(text)
    cusing = cryptororiginal
    for i in x:
        
        if cusing == (cryptororiginal + 3):
            cusing = cryptororiginal


        cryptor = cusing
        if i == alph[0]:
            codedtext.append(alph[org(0,2,cryptor)])
        elif i == alph[1]:
            codedtext.append(alph[org(1,2,cryptor)])
        elif i == alph[2]:
            codedtext.append(alph[org(2,2,cryptor)])
        elif i == alph[3]:
            codedtext.append(alph[org(3,2,cryptor)])
        elif i == alph[4]:
            codedtext.append(alph[org(4,2,cryptor)])
        elif i == alph[5]:
            codedtext.append(alph[org(5,2,cryptor)])
        elif i == alph[6]:
            codedtext.append(alph[org(6,2,cryptor)])
        elif i == alph[7]:
            codedtext.append(alph[org(7,2,cryptor)])
        elif i == alph[8]:
            codedtext.append(alph[org(8,2,cryptor)])
        elif i == alph[9]:
            codedtext.append(alph[org(9,2,cryptor)])
        elif i == alph[10]:
            codedtext.append(alph[org(10,2,cryptor)])
        elif i == alph[11]:
            codedtext.append(alph[org(11,2,cryptor)])
        elif i == alph[12]:
            codedtext.append(alph[org(12,2,cryptor)])
        elif i == alph[13]:
            codedtext.append(alph[org(13,2,cryptor)])
        elif i == alph[14]:
            codedtext.append(alph[org(14,2,cryptor)])
        elif i == alph[15]:
            codedtext.append(alph[org(15,2,cryptor)])
        elif i == alph[16]:
            codedtext.append(alph[org(16,2,cryptor)])
        elif i == alph[17]:
            codedtext.append(alph[org(17,2,cryptor)])
        elif i == alph[18]:
            codedtext.append(alph[org(18,2,cryptor)])
        elif i == alph[19]:
            codedtext.append(alph[org(19,2,cryptor)])
        elif i == alph[20]:
            codedtext.append(alph[org(20,2,cryptor)])
        elif i == alph[21]:
            codedtext.append(alph[org(21,2,cryptor)])
        elif i == alph[22]:
            codedtext.append(alph[org(22,2,cryptor)])
        elif i == alph[23]:
            codedtext.append(alph[org(23,2,cryptor)])
        elif i == alph[24]:
            codedtext.append(alph[org(24,2,cryptor)])
        elif i == alph[25]:
            codedtext.append(alph[org(25,2,cryptor)])
        elif i == alph[26]:
            codedtext.append(alph[org(26,2,cryptor)])
        elif i == alph[27]:
            codedtext.append(alph[org(27,2,cryptor)])
        elif i == alph[28]:
            codedtext.append(alph[org(28,2,cryptor)])
        elif i == alph[29]:
            codedtext.append(alph[org(29,2,cryptor)])
        elif i == alph[30]:
            codedtext.append(alph[org(30,2,cryptor)])
        elif i == alph[31]:
            codedtext.append(alph[org(31,2,cryptor)])
        elif i == alph[32]:
            codedtext.append(alph[org(32,2,cryptor)])
        elif i == alph[33]:
            codedtext.append(alph[org(33,2,cryptor)])
        elif i == alph[34]:
            codedtext.append(alph[org(34,2,cryptor)])
        elif i == alph[35]:
            codedtext.append(alph[org(35,2,cryptor)])
        elif i == alph[36]:
            codedtext.append(alph[org(36,2,cryptor)])
        elif i == alph[37]:
            codedtext.append(alph[org(37,2,cryptor)])
        elif i == alph[38]:
            codedtext.append(alph[org(38,2,cryptor)])
        elif i == alph[39]:
            codedtext.append(alph[org(39,2,cryptor)])
        elif i == alph[40]:
            codedtext.append(alph[org(40,2,cryptor)])
        elif i == alph[41]:
            codedtext.append(alph[org(41,2,cryptor)])
        elif i == alph[42]:
            codedtext.append(alph[org(42,2,cryptor)])
        elif i == alph[43]:
            codedtext.append(alph[org(43,2,cryptor)])
        elif i == alph[44]:
            codedtext.append(alph[org(44,2,cryptor)])
        elif i == alph[45]:
            codedtext.append(alph[org(45,2,cryptor)])
        elif i == alph[46]:
            codedtext.append(alph[org(46,2,cryptor)])
        elif i == alph[47]:
            codedtext.append(alph[org(47,2,cryptor)])
        elif i == alph[48]:
            codedtext.append(alph[org(48,2,cryptor)])
        elif i == alph[49]:
            codedtext.append(alph[org(49,2,cryptor)])
        elif i == alph[50]:
            codedtext.append(alph[org(50,2,cryptor)])
        elif i == alph[51]:
            codedtext.append(alph[org(51,2,cryptor)])
        elif i == alph[52]:
            codedtext.append(alph[org(52,2,cryptor)])
        elif i == alph[53]:
            codedtext.append(alph[org(53,2,cryptor)])
        elif i == alph[54]:
            codedtext.append(alph[org(54,2,cryptor)])
        elif i == alph[55]:
            codedtext.append(alph[org(55,2,cryptor)])
        elif i == alph[56]:
            codedtext.append(alph[org(56,2,cryptor)])
    ct = ''.join(codedtext)
    return ct
run = 1
while run == 1:
    option = int(input('Enter 1 to code a message or 2 do decode a message:'))
    text = input('Enter the text to be translated:')
    cryptororiginal = int(input('Please enter your encryption number:'))
    print ('\n')
    if option ==1:
        print(tocode(text,cryptororiginal))
    elif option ==2:
        print(decode(text,cryptororiginal))
    run = int(input('Enter \"1\" to run again:'))