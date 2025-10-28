# tasks/task6.py

def solve():
# Ниже пишите решение задачи

   a, b, c = map(int,input().split())
   result = (a*a == b*b + c*c) or (b*b == a*a + c*c) or (c*c == a*a + b*b)
   print(result)
   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()