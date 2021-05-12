#Temporary Upload, still needs to be checked, this is old code
#lesson12
#Lucy Murphy
#Feb 25th 

def change_end(string):#changes ending to ing. If already ing change to "ly"
    if len(string) < 3:
        print(string)
    else:
        if string[-3]=="ing":
            print (string[0:-3] + "ly")
        else:
            print(string + "ing")

            
def change_char(string):
    ans = string[0]
    for x in range (1, len(string)):
        if string[x] == sting[0]:
            ans += '$'
            continue
        return ans
    #test
    print(change_char("ananananan"))
    print(change_char("bababababa"))

#REPLACE EXAMPLE:
    def change_char(string):
        char = string[0]
        newstring = char +
    string[1:].replace(char, '$')  #replace
        return newstring
    #test
    print(change_char('anananana'))
    print(change_char("bababababba"))
#COUNT
    print('Abracadabra'.count('a'))
    #4
    print('aaaaaaaaaa'.count('aa'))

#Find
>>> s = 'hello'
>>> print(s.find('e'))
#1

def even_let(string): #returns the even letters
    print(string[::2])
#test
even_let(qwerty)
 #qet
even_let(asdfg)
 #adg

def findChar(string):
    for index in range(len(string)):
        print ("current Character", string[index], "at position", index)
