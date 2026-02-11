

stro = input() # Количество доливов воды



def voda(input_str):
    lines = [line.strip() for line in input_str.strip().splitlines() if line.strip()]
    
    if not lines:
        return 0
    
    # Первая строка - количество событий
    N = int(lines[0])
    
    if N == 0:
        return 0

    V_0 = 0  # Изначальное количество воды в увлажнителе
    dt = []
    dv = []
    
    # Читаем N строк из lines, начиная с индекса 1
    for i in range(1, N + 1):
        stroka = lines[i].split()
        dt.append(int(stroka[0]))
        dv.append(int(stroka[1]))

    V_0 = 0 # Изначальный количество воды в увлажнителе
    dt = []
    dv = []
    count = N
    while count != 0:
        dt.append(int(stroka[0]))
        dv.append(int(stroka[1]))
        count -= 1
    
    V_0 += dv[0]

    for i in range(1, N):
        ddt = dt[i] - dt[i-1]
        V_0 -= ddt
        if V_0 < 0:
            V_0 = 0
        V_0 += dv[i]
    
    return V_0

print(voda(stro))

    
    