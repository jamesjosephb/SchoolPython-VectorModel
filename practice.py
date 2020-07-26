def validateSSN(SSN):
    SSN=list(SSN)
    print(SSN)
    try:
        SSN=eval(SSN[0]+SSN[1]+SSN[2]+SSN[4]+SSN[5]+SSN[7]+SSN[8]+SSN[9]+SSN[10])
    except SyntaxError:
        return print("Invalid SSN Number")
    if isinstance(SSN,int) == True:
        return print("This is a valid SSN number ")



if __name__ =='__main__':
    SSN=("234-23-2333")
    validateSSN(SSN)
    SSN=("3fr-3322344")
    validateSSN(SSN)






