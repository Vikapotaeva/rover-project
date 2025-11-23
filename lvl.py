
def lvl1(n: int, text1: str):
    if n == 1 : return text1.upper()
    if n == 2: return text1.lower()
    if n == 3: return text1.capitalize()


def lvl2(n: int, text1: str):
    if n == 1:
        i = input("string: ")
        return text1.find(i)
    if n == 2:
        i = input("string: ")
        j = int(input(""))
        return text1.replace("круто", i, j)
    if n == 3:
        return text1.count("о") + text1.count("О")


def lvl3(n: int, text1: str):
    if n == 1:
        i = input("")
        return text1.split(i)
    if n == 2:
        i = input()
        return i.join(text1)


def lvl4(n: int, text1: str):
    if n == 1: return text1.isdigit()
    if n == 2: return text1.isalpha()
    if n == 3: return text1.strip()
    if n == 4: return text1.format()
    

lvl = int(input("lvl: "))
if lvl == 1:
    n = int(input("Choose a number (1 - upper, 2 - lower, 3 - capitalize): "))
    text1 = input("text: ")
    print(lvl1())
if lvl == 2:
    n = int(input("number (1 - find, 2 - replace, 3 - count): "))    
    text1 = input("text: ")
    print(lvl2(n, text1))
    
if lvl == 3:
    n = int(input("number (1 - split, 2 - join): "))    
    text1 = input("text: ")
    print(lvl3(n, text1))

if lvl == 4:
    n = int(input("number (1 - isdigit, 2 - isalpha, 3 - strip, 4 - format): "))    
    text1 = input("text: ")
    print(lvl4(n, text1))
