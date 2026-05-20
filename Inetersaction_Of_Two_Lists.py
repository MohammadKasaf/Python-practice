
def intersaction_of_two_lists(A,B):

    intersected_list=[]

    for i in range(len(A)):
        if A[i] in B:
            intersected_list.append(A[i])

    print(intersected_list)

A=[1,2,3,4,5,23]
B=[3,4,5,6,7]
intersaction_of_two_lists(A,B)