id = input()
pw = ["apple","banana","grape","blueberry","orange"]
cnt = 0
for i in range(5):
    
    if id == pw[i][2] or id ==  pw[i][3]:
        cnt += 1
        print(pw[i])
print(cnt)