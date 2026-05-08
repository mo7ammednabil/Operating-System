# Shortest Job First
n = int (input("Number of processes: "))
burst = []
for i in range (n):
    bt = int(input(f"p{i+1} Burst Time: "))
    burst.append(bt)
burst.sort()
waiting = [0]*n
for i in range (1,n):
    waiting[i]= waiting[i-1] + burst [i-1]

average = sum(waiting)/n
print(f"Burust Time {burst}")
print(f"Waiting Time {waiting}")
print(f"average waitnig time {average}")