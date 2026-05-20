
def move_all_zeros_to_end(elements):

    count_zeros=0
    non_zero_list=[]

    for index in range(len(elements)):
        if elements[index]!=0:
            non_zero_list.append(elements[index])
        else:
            count_zeros+=1

    for i in range(count_zeros):
        non_zero_list.append(0)
    return non_zero_list

size=int(input("enter the list size : "))
elements=[]
for i in range(size):
   elements.append(int(input("enter a number : ")))

final_list=move_all_zeros_to_end(elements)
for index in range(len(final_list)):
    print(final_list[index], end=" ")
