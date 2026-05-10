# Round Robin
n = int (input("Number of processes: "))
burst = []
for i in range (n):
    burst.append(int(input(f"p{i+1} Burat Time: ")))
tq = int(input("Time Quantum: "))
remaining = burst.copy()
time = 0
completion = [0]*n
while sum (remaining) > 0:
    for i in range(n):
        if remaining [i] > 0:
            if remaining[i]>tq:
                time+= tq
                remaining[i] -= tq
            else:
                time += remaining[i]
                remaining[i]=0
                completion[i]=time

Waiting = []
for i in range(n):
    Waiting.append(completion[i]-burst[i])
average = sum(Waiting)/n
print(f"Waiting time ",Waiting)
print(f"average time ",average)
