# A問題
N = int(input())
a = N // 100
b = N // 10 % 10
c = N % 10
result1 = int(f"{b}{c}{a}")
result2 = int(f"{c}{a}{b}")
print(result1, result2)


# 振り返り
#  百の位の数値、十の位の数値、一の位の数値は考えればわかるのをやらなかった。
#  数値を結合する方法を学んだ。
#  a = 3 b = 5のとき、35を出力したい。
# result = int(str(a) + str(b))
# result = a * 10 + b
# result = int(f"{a}{b}")

