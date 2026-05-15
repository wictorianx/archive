def convert_to_binary(num)
    points = [128,64,32,16,8,4,2,1]
    num = 200
    i = -1
    create = ""
    while(i<(len(points)-1)):
        i+=1
        if num >= points[i]:
            num-=points[i]
            create += "1"
        else:
            create += "0"
    return(create)
