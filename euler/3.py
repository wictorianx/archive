while('true'):
    (index)= int(input("En büyük asal çarpanını bulmak istediğiniz sayıyı giriniz. \n"))
    count = 2
    while(count * count <= index and index != 1 ):
        while (index%count ==0):
            index /= count
        count+=1
    print(index)

        
            

            






