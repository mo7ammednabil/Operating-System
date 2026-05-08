# Preemptive Priority Scheduling
n = int(input("Number of processes: "))
arrival = []
burst = []
priority = []

for i in range(n):
    arrival.append(int(input(f"P{i+1} Arrival: ")))
    burst.append(int(input(f"P{i+1} Burst: ")))
    priority.append(int(input(f"P{i+1} Priority: ")))

remaining = burst.copy()
time = 0
completion = [0] * n

while sum(remaining) > 0:
    idx = -1
    for i in range(n):
        if arrival[i] <= time and remaining[i] > 0:
            if idx == -1 or priority[i] < priority[idx]:
                idx = i
                
    if idx != -1:
        remaining[idx] -= 1
        time += 1
        if remaining[idx] == 0:
            completion[idx] = time
    else:
        time += 1

waiting = []
for i in range(n):
    waiting.append(completion[i] - arrival[i] - burst[i])

average = sum(waiting) / n

print("Waiting Time:", waiting)
print("Average Waiting Time:", average)