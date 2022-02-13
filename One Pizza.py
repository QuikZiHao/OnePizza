# ————————————————————————————————————#
# Project Name: One Pizza                                                 #
#                                                                         #
# author : Quik Zi Hao                                                    #
#          George Lee Yip                                                 #
#          Chee Sien Zhen                                                 #
# TeamName : FoonYewFakeTaxi                                              #
# Date: 14 - 2 - 2022                                                     #                   #
#                                                                         #
# ————————————————————————————————————#


filename ="e_elaborate"   #input ur input file here
f = open(filename+".in.txt", 'r')
file = f.readlines()
Nppl = int(file[0])
book = []
menu = set()
newmenu = set()
customer = 0
for i in range(0,Nppl):
    like = file[2*i+1].split()
    like = like[1:]
    dislike = file[2*i+2].split()
    dislike = dislike[1:]

    new = [set(like),set(dislike)]
    book.append(new)

    #print('newmenu before', newmenu)
    newmenu = menu.union(set(like))
    #print('newmenu now', newmenu)
    newmenu = newmenu-set(dislike)
    newmenucus = 0
    #print('newmenu after',newmenu,i)

    for k in range(0,len(book)):
        if book[k][0] <= newmenu and book[k][1]&newmenu == set():
            newmenucus += 1

    if newmenucus>customer:
        customer = newmenucus
        menu = newmenu

output = str(len(menu))
menu = list(menu)
str1 = ' '.join(menu)
output = output+" "+str1

a_file = open(filename+".out.txt", "x")
a_file.write(output)
a_file.close()
