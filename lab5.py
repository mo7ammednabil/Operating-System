# SJF Preemptive
n = int(input("Number of processes: "))
arrival = []
burst = []

for i in range(n):
    arrival.append(int(input(f"P{i+1} Arrival: ")))
    burst.append(int(input(f"P{i+1} Burst: ")))

remaining = burst.copy()
time = 0
completion = [0] * n

while sum(remaining) > 0:
    smallest = -1
    for i in range(n):
        if arrival[i] <= time and remaining[i] > 0:
            if smallest == -1 or remaining[i] < remaining[smallest]:
                smallest = i
                
    if smallest != -1:
        remaining[smallest] -= 1
        time += 1
        if remaining[smallest] == 0:
            completion[smallest] = time
    else:
        time += 1

waiting = [0] * n
for i in range(n):
    waiting[i] = completion[i] - arrival[i] - burst[i]

average = sum(waiting) / n

print("Waiting Time:", waiting)
print("Average Waiting Time:", average)