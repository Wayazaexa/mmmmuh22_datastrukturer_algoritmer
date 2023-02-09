
# Basfall
#sum_list([]) # Ska returnera 0

#sum_list([3]) # Ska returnera 3

# Lite mer komplext
#sum_list([2, 3]) # Ska returnera: 2 + sum_list([3])

# Ytterliggare ett steg upp
#sum_list([5, 2, 3]) # Ska returnera: 5 + sum_list([2, 3])


def sum_list(slist):
   sum = 0
   for i in range(0, len(slist)):
      sum += slist[i]

   return sum

def sum_list_r(slist):
   if len(slist) == 0:
      return 0
   else:
      return slist[0] + sum_list_r(slist[1:])
   
print(sum_list_r([5, 2, 3]))