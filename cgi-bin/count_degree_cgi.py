def count_degree(parameters, psa):
    glison = parameters[0]
    t = parameters[1]
    n = parameters[2]
    m = parameters[3]
    # ---------------
    if t == '1' and n == 0 and m == 0 and psa < 10 and glison <= 6:
        degree = '|'
    elif t == '2a' and n == 0 and m == 0 and psa < 10 and glison <= 6:
        degree = '|'
    # ---------------
    elif t == '1' and n == 0 and m == 0 and psa < 20 and glison == 7:
        degree = '||A'
    elif t == '1' and n == 0 and m == 0 and (psa < 20 and psa >=10) and glison <= 6:
        degree = '||A'
    elif t == '2a' and n == 0 and m == 0 and psa < 20 and glison <= 7:
        degree = '||A'
    elif t == '2b' and n == 0 and m == 0 and psa < 20 and glison <= 7:
        degree = '||A'
    elif t == '2' and n == 0 and m == 0 and psa < 20 and glison <= 7:
        degree = '||A'
    # ---------------
    elif t == '2c' and n == 0 and m == 0:
        degree = '||B'
    elif (t == '1' or t == '2' or t == '2a' or t == '2b' or t == '2c') and n == 0 and m == 0 and psa >= 20:
        degree = '||B'
    elif (t == '1' or t == '2' or t == '2a' or t == '2b' or t == '2c') and n == 0 and m == 0 and glison >= 8:
        degree = '||B'
    # ---------------
    elif t == '3' or t == '3a' or t == '3b' or t == '3c':
        degree = '|||'
    # ---------------
    elif t == '4':
        degree = '|V'
    elif n == 1 and m == 0:
        degree = '|V'
    elif m == 1:
        degree = '|V'
    else:
        degree = 'hs'
    return degree

# print(count_degree([7,'3',0,0],100))