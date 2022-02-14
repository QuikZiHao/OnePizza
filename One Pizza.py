# ——————————————————————————————————————————————————————————————————————————————————————————————————————————#
#                                   Project Name: One Pizza                                                 #
#                                                                                                           #
#                                   author : Quik Zi Hao                                                    #
#                                            George Lee Yip                                                 #
#                                            Chee Sien Zhen                                                 #
#                                   TeamName : FoonYewFakeTaxi                                              #
#                                   Date: 14 - 2 - 2022                                                     #               
#                                                                                                           #
# ——————————————————————————————————————————————————————————————————————————————————————————————————————————#


import random
filename ="input_file\d_difficult"   #input ur input file here
f = open(filename+".in.txt", 'r')
file = f.readlines()
Nppl = int(file[0])
book = []
menu = set()
newmenu = set()
customer = 0
finallyCustomer = 0
finallyMenu = set()
for i in range(0,Nppl):
    like = file[2*i+1].split()
    like = like[1:]
    dislike = file[2*i+2].split()
    dislike = dislike[1:]
    new = [set(like),set(dislike)]
    book.append(new)
for times in range(20):
    menu = set()
    newmenu = set()
    customer = 0
    for i in range(0,Nppl):
        #print('newmenu before', newmenu)
        newmenu = menu.union(book[i][0])
        #print('newmenu now', newmenu)
        newmenu = newmenu-set(book[i][1])
        newmenucus = 0
        #print('newmenu after',newmenu,i)

        for k in range(0,Nppl):
            if book[k][0] <= newmenu and book[k][1]&newmenu == set():
                newmenucus += 1

        if newmenucus>customer:
            customer = newmenucus
            menu = newmenu
    if(customer>finallyCustomer):
        finallyCustomer = customer
        finallyMenu = menu
    print(times,customer)
    random.shuffle(book)
output = str(len(finallyMenu))
menu = list(finallyMenu)
str1 = ' '.join(finallyMenu)
output = output+" "+str1
a_file = open(filename+".out.txt", "x")
a_file.write(output)
a_file.close()
