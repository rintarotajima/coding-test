N, C = map(int, input().split())
T = [int(input()) for i in range(N)]
sum = 0

if N == 1:
    sum+=1
else:
    for i in range(N):
        if T[i] - T[i-1] < C:
            sum
        else:
            if T[i] - T[i-1] >= C:
                sum +=1

print(sum)


    
