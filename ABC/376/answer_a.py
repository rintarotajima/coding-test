n, c = map(int, input().split())
t = list(map(int, input().split()))

ans = 1 # 飴の数を表す変数
pre = t[0] # 最後に飴をもらった時刻を表す変数

for i in range(1, n): #2番目にボタンを押す時間t[1]からn番目にボタンを押す時間t[n]まで繰り返し
    if t[i] - pre >= c: 
        ans += 1
        pre = t[i] # 飴をもらった時刻を更新

print(ans)
