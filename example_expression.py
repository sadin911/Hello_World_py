for x in range(2):
    for y in range(2):
        for z in range(2):
            result = 1-(((x^z)&y))
            print(x,y,z,result)