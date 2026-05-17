
def duplicate_elements():

    lis=[]
    for i in range(6):
        num=int(input("enter a number :"))
        lis.append(num)

    duplicates = []
    dic={}

    for i in range(len(lis)):
        if lis[i] in dic:
            dic[lis[i]]=dic.get(lis[i])+1
        else:
            dic[lis[i]]=1

    for key,value in dic.items():
        if value>1:
            duplicates.append(key)

    return duplicates


elements=duplicate_elements()
for i in range (len(elements)):
    print(elements[i])
