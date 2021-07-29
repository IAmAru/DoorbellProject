attackFlag = False

def validKey(keyPayload):
    """"Good ol' intrusion detection system. Not particularly the best, but it discriminates
    anything that might not be a password / attack elegantly. Any attack will be logged in console."""
    global attackFlag
    #Filters through anything that is not a length of 10.
    if len(keyPayload)!= 10:
        if(attackFlag == False):
            print(f"1. Key failed authentication. Possible attack. Key: {keyPayload}")
            attackFlag = True
            return False
        elif(attackFlag == True):
            return False
    elif len(keyPayload) == 10:
        keyPayload = keyPayload
    
    containsDigit = any(map(str.isdigit, keyPayload)) 
    #Filters through anything that has a digit (should be all characters)
    if containsDigit:
        if(attackFlag == False):
            print(f"2. Key failed authentication. Possible attack. Key: {keyPayload}")
            attackFlag = True
            return False
        elif(attackFlag == True):
            return False
    elif ~containsDigit: #Sets the key.
        keyPayload = keyPayload

    containsUpper = any(ele.isupper() for ele in keyPayload)
    if containsUpper:
        return True
    elif ~containsUpper:
        if(attackFlag == False):
            print(f"3. Key failed authentication. Possible attack. Key: {keyPayload}")
            attackFlag = True
            return False
        elif(attackFlag == True):
            return False
