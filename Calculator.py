def isFloat(x):
    accepted_list = ["."]
    for i in range (0, 10):
        i = str(i)
        accepted_list.append(i)
    period_count = 0
    x = list(x)
    length = len(x)
    count = 0
    for i in range (0, length):
        for j in range (0, 11):
            if x[i] == accepted_list[j]:
                count = count + 1
                if j == 0:
                    period_count = period_count + 1
                else:
                    toggle = True
            else:
                toggle = False

    if count == length and period_count < 2:
        return(True)
    else:
        return(False)

def isInt(x):
    accepted_list = []
    for i in range (0, 10):
        i = str(i)
        accepted_list.append(i)
    x = list(x)
    length = len(x)
    count = 0
    for i in range (0, length):
        for j in range (0, 10):
            if x[i] == accepted_list[j]:
                count = count + 1
            else:
                toggle = True
    if count == length:
        return(True)
    else:
        return(False)
