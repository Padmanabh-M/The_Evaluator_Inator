import re


# Function to operate on 2 
def Two(pop):
    id_count = 0
#     if pop[0] in ['-','+']:
#         pop = pop[1:]
    for i in pop:
        if i in ['*', '+', '-', '/']:
            idx = i
            break
        id_count += 1
    first = float(pop[:id_count])
#     print('this is first ', first)
    second = float(pop[id_count+1:])
#     print('this is second ', second)
    
    if idx == '*':
        return first * second
    if idx == '+':
        return first + second
    if idx == '-':
        return first - second
    if idx == '/':
        return first / second




# Function to get index interval to squeeze reduced value 
def Squeeze_idx(current, vals):
    
    try:
        res = current.index(vals)
    except:
        print('Some kinda error with :', vals)
        

    return res
    

# Function to reduce the statement to one value 
def Straight(current):
    pratt = re.compile(r"\d*[\*\/\-\+]\d*")
    chris = pratt.findall(current)
    
    plus = 0
    minus = 0
    mult = 0
    div = 0
    for i in current:
        if i == '+':
            plus += 1
        
        if i == '-':
            minus += 1
        
        if i == '*':
            mult += 1
        
        if i == '/':
            div += 1
    
    
    for d in range(div):
        pratt = re.compile(r'[-+]?(\d+|\d+\.[0-9]+)\/([-]?\d+\.[0-9]+|\d+)')
        chris = pratt.findall(current)
#         print('for division')
#         print(chris)
        for i in chris:
            squeeze = round(Two(i[0]+'/'+i[1]), 2)
#             print('sq ', squeeze)
            begins = Squeeze_idx(current, i[0]+'/'+i[1])
#             print('begins ', begins)
            ends = begins+len(i[0]+'/'+i[1])
#             print('ends', ends)
#             print('\n')
#             print(current[:begins] + str(squeeze) + current[ends:])
            current = current[:begins] + str(squeeze) + current[ends:]
            div
    
    for m in range(mult):
        pratt = re.compile(r'[-+]?(\d+|\d+\.[0-9]+)\*([-]?\d+\.[0-9]+|\d+)')
        chris = pratt.findall(current)
#         print('for mult')
#         print(chris)
        for i in chris:
            squeeze = round(Two(i[0]+'*'+i[1]), 2)
#             print('sq ', squeeze)
            begins = Squeeze_idx(current, i[0]+'*'+i[1])
#             print('begins ', begins)
            ends = begins+len(i[0]+'*'+i[1])
#             print('ends', ends)
#             print('\n')
#             print(current[:begins] + str(squeeze) + current[ends:])
            current = current[:begins] + str(squeeze) + current[ends:]
        
    for p in range(plus):
        pratt = re.compile(r'[-+]?(\d+|\d+\.[0-9]+)\+([-]?\d+\.[0-9]+|\d+)')
        chris = pratt.findall(current)
#         print('for addi')
#         print(chris)
        for i in chris:
            squeeze = round(Two(i[0]+'+'+i[1]), 2)
#             print('sq ', squeeze)
            begins = Squeeze_idx(current, i[0]+'+'+i[1])
    #             print('begins ', begins)
            ends = begins+len(i[0]+'+'+i[1])
    #             print('ends', ends)
#             print('\n')
#             print(current[:begins] + str(squeeze) + current[ends:])
            current = current[:begins] + str(squeeze) + current[ends:]
    
    for m in range(minus):
        pratt = re.compile(r'[-+]?(\d+|\d+\.[0-9]+)\-([-]?\d+\.[0-9]+|\d+)')
        chris = pratt.findall(current)
#         print('for sub')
#         print(chris)
        for i in chris:
            squeeze = round(Two(i[0]+'-'+i[1]), 2)
#             print('sq ', squeeze)
            begins = Squeeze_idx(current, i[0]+'-'+i[1])
    #             print('begins ', begins)
            ends = begins+len(i[0]+'-'+i[1])
    #             print('ends', ends)
#             print('\n')
#             print(current[:begins] + str(squeeze) + current[ends:])
            current = current[:begins] + str(squeeze) + current[ends:]
    
    
    
#     print('plus ', plus)
#     print('minus ', minus)
#     print('mult ', mult)
#     print('div ', div)
#     print(chris)
    
    return current




# Function to reduce the stuff inside the brackets
def Wall_Break(str_val,nbr):
#     current = ''
    for i in range(nbr):
        idx1 = 0
        idx2 = 0
        current = ''
        for i in range(idx1, len(str_val)):
            if str_val[i] == '(':
    #             print("First loop x1 ", idx1)
    #             print("First loop x2 ", idx2)

                for j in range(idx1+1,len(str_val)):

    #                 print("Second loop x1 ", idx1)
    #                 print("Second loop x2 ", idx2)

    #                 print(str_val[j])

                    if str_val[j] == '(':
    #                     idx1 = idx1 + 1
                        idx1 = idx1
                        idx2 = 0
                        break

                    if str_val[j] == ')':
    #                     print(str_val[idx1+1 :idx1+idx2+1])
                        current = str_val[idx1+1 :idx1+idx2+1]
                        outer_l = idx1+1
                        outer_r = idx1+idx2+1
                        break
                    idx2 += 1

            idx1 += 1



#         print('OG before', str_val)
#         print('current ',current)
#         print('outer l ',outer_l)
#         print('outer r ',outer_r)

        reduced = Straight(current)

#         print(reduced)
#         print('OG after', str_val)
#         print(str_val[:outer_l-1] + reduced + str_val[outer_r+1:])
        str_val = str_val[:outer_l-1] + reduced + str_val[outer_r+1:]
        
#     print('\n\n\n\n\n')
    
#     print(str_val)
    print('The final answer ',Straight(str_val))
    
# Function to count the number of brackets for reduction...THE_EVALUATOR_INATOR.....Doofenshmirtz Evil Incorporated
def The_Evaluator_Inator(crytek):
    brackets = 0
    for i in crytek:
        if i == '(':
            brackets += 1
    Wall_Break(crytek, brackets)

    
        
crytek = "2*3*5+234-2342+23+(234-456)+43"        
crytek2 = "2*3*5+234-(2342+(23+234+12234/56+345*435-34-342/56)-456)+43"



The_Evaluator_Inator(crytek2)