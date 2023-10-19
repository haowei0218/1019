def find_last_person(n):
    colleagues = list(range(1, n + 1))
    position = 0
    while len(colleagues) > 1:
        position = (position + 2) % len(colleagues)  
        del colleagues[position]  
    return colleagues[0] 


n = int(input("请输入同事的数量："))
result = find_last_person(n)
print(f"最后留下的同事是第 {result} 位。")
