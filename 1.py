a = []
def input_five():
    for i in range(5):
        result = int(input("輸入成績"))
        a.append(result)

input_five()

def quit():
    for i in a:
        ten = i // 10
        num = i % 10
        number = (num * 10 + ten)
        print(number)

quit()
      