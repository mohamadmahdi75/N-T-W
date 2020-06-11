import re

def number_to_list(number):

    NUMBER=str(number)

    return list(NUMBER)


def meghdar_dehi(number):

    number_list=number_to_list(number)

     
    banklist=[]

    for i,d in enumerate(number_list[::-1]):
        if d!=0:
            if i>=2:
                banklist.append(eval("{}".format(10**i)))
                banklist.append(eval("{}".format(d)))
                


            else:
                banklist.append(eval("{}*{}".format(10**i,d)))
        
        
    return banklist[::-1]
    






def tarjome(number):
    

    my_dict={
        0:"zero",1:"one",2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:"eight",9:"nine",10:"ten",
        11:'eleven', 12:'twelve', 13:'thirteen', 14:'forteen', 15:'fifteen' ,16:'sixteen' ,17:'seventeen' ,18:'eighteen' ,19:'nineteen' ,20:'twenty',
        30:'thirty', 40:'fourty' ,50:'fifty' ,60:'sixty' ,70:'seventy' ,80:'eighty' ,90:'ninety' ,100:'hundred' ,1000:'thousand'
    }

    if len(str(number))>=3:
        is_under_bist=meghdar_dehi(number)[-1] + meghdar_dehi(number)[-2]  <20
        has_hundred=(meghdar_dehi(number)[2])*(meghdar_dehi(number)[3])!=0
        is_upper_bist=meghdar_dehi(number)[-2]>=20

        hezar=my_dict[meghdar_dehi(number)[0]]+" "+ my_dict[meghdar_dehi(number)[1]]+" "
        sad=my_dict[meghdar_dehi(number)[-4]]+ " " +my_dict[meghdar_dehi(number)[-3]]+" "
        

        if is_under_bist:
            zire_bist=my_dict[sum(meghdar_dehi(number)[-1:-3:-1])]


        if meghdar_dehi(number)[-1]==0:
            bist_be_bala=my_dict[meghdar_dehi(number)[-2]]
        else:
            bist_be_bala= my_dict[meghdar_dehi(number)[-2]]+" "+my_dict[meghdar_dehi(number)[-1]]    

    elif len(str(number))==2:
        is_under_bist = meghdar_dehi(number)[-1] + meghdar_dehi(number)[-2]  <20

        if is_under_bist:
            zire_bist=my_dict[sum(meghdar_dehi(number)[-1:-3:-1])]

        if meghdar_dehi(number)[-1]==0:
            bist_be_bala=my_dict[meghdar_dehi(number)[-2]]
        else:
            bist_be_bala= my_dict[meghdar_dehi(number)[-2]]+" "+my_dict[meghdar_dehi(number)[-1]]      
    






    if len(str(number))==4:
        if has_hundred:
            if is_under_bist:
                return hezar+sad+zire_bist
            else:
                return hezar+sad+bist_be_bala
        else:
            if is_under_bist:
                return hezar+zire_bist
            else:
                return hezar+bist_be_bala


    if len(str(number))==3:
        if is_under_bist:
            return sad+zire_bist
        else:
            return sad+bist_be_bala    

    if len(str(number))==2:
        if is_under_bist:
            return zire_bist
        else:
            return bist_be_bala    

    if len(str(number))==1:
        return my_dict[number]



a=1051

print('meghdar_dehi=',meghdar_dehi(a))
print('tarjome=',tarjome(a))