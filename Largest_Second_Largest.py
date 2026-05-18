
def largest_second_largest(elements):

    largest=0
    second_largest=0

    for num in elements:
        if largest<num:
            second_largest=largest
            largest=num
        elif second_largest<num and num!=largest:
            second_largest=num

    return largest,second_largest

elements=[]
for i in range(6):
    num=int(input("enter a number : "))
    elements.append(num)

largest,second_largest=largest_second_largest(elements)
print(f" largest number is {largest} and second largest is {second_largest} ")