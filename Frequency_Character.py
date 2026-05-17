def frequency_character():

    lis=[]
    for i in range(6):
        ch=(input("enter a character :"))
        lis.append(ch)

    freq={}

    for i in range(len(lis)):
        if lis[i] in freq:
            freq[lis[i]]+=1
        else:
            freq[lis[i]]=1

    for key,value in freq.items():
        print(f"character {key} and frequency is {value}")

frequency_character()

