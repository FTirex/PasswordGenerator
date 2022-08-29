import random 

password = ""

ListA = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

ListC = ['*','-','/','+','.',',',';',':','§','\,','&','é','"','#','{','}','[',']','(',')','-','|','è','ç','à','^','@','=','']

ListN = ['1','2','3','4','5','6','7','8','9','0']

for i in range (16):
    
    password += random.choice(ListA) + random.choice(ListC) + random.choice(ListN) + random.choice(ListA[i].lower())+"\n"
    
print(password)