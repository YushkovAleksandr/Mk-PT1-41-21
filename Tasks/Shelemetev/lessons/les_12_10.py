str="five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
listed_str=str.split()
print(listed_str)


listed_str=list(set(listed_str)) 
print(listed_str)


chisla={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"eleven":11,"twelve":12,"thirteen":13,"fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19, "twenty":20, "twenty one":21}

chisla_v_chislax=[]

for x in listed_str:
    print(chisla.get(x))
    chisla_v_chislax.append(chisla.get(x))
print("\n\n\n")
print(chisla_v_chislax)
print("\n\n\n")
x=0
for x in range(len(chisla_v_chislax)):
   
    if chisla_v_chislax[x]<chisla_v_chislax[x-1]:
        print(chisla_v_chislax[x])
        x+=1
    else: print(chisla_v_chislax[x-1])
    x+=1