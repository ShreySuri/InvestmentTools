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

# principal is a
# deposit is b
# interval is c
# rate is d
# end is e

def invest(a, b, c, d, e):
    total = a
    list_1 = []
    for i in range (0, c * e + 1):
        if i % c == 0:
            year = int(i / c)
            tuple_1 = (year, total)
            list_1.append(tuple_1)
        else:
            toggle = True

        additional = d * 0.01 / c * total + b
        total = total + additional
    return(list_1)
        
def read_inv(list_1, format_1):
    if format_1 == "table":
        length = len(list_1)
        for i in range (0, length):
            tuple_1 = list_1[i] 
            year = tuple_1[0]
            amount = tuple_1[1]
            amount = amount * 100
            amount = round(amount)
            amount = amount / 100
            print("Year %s -- %s" % (year, amount))
    else:
        print(None)

    return(None)
