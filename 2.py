txt = "Hello wrlcome to Cathay 60th year anninversary"
txt1 = txt.lower()

A = {}

for i in txt:
    if i.isalpha():
        if i in A:
            A[i]+=1
        else:
            A[i]=1
for letter,count in A.items():
    print(f"{A}:{count}次")                

