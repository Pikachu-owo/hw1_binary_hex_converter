while True:
    n = int(input("請輸入數字："))
    if 0 <= n <= 255:
        N = n
        break
    else:
        print("範圍為0-255的數字")

T = ""
while n > 0:
    T = str(n % 2) + T
    n //= 2
if T == "":
    T = 0
print("轉換為二進位：", T)

text = "0123456789ABCDEF"
S = ""
while N > 0:
    A = N % 16
    S = text[A] + S
    N //= 16
if S == "":
    S = 0
print("轉換為十六進位：", S)

