p = int(input(""))
s = str(p)

def orderOfTenModP():
    global p
    pMod = p
    while pMod % 2 == 0:
        pMod = pMod / 2
    while pMod % 5 == 0:
        pMod = pMod / 5
    if pMod == 1:
        return 0
    n = 1
    while pow(10, n) % pMod != 1:
        n += 1
    return n

def findRepetend():
    global p
    global s
    remainder = 0
    quotient = ""
    parts = dict()
    dividend = 1
    
    while True:
        if dividend in parts:
            break
        parts[dividend] = True
        quotient += str(dividend // p)
        remainder = dividend % p
        dividend = remainder * 10

    print(quotient[1:])

print(orderOfTenModP())
findRepetend()
