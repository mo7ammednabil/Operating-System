# Priority Scheduling
n = int(input("Number of processes: "))
arrival = []
burst = []
priority = []

for i in range(n):
    arrival.append(int(input(f"P{i+1} Arrival: ")))
    burst.append(int(input(f"P{i+1} Burst: ")))
    priority.append(int(input(f"P{i+1} Priority: ")))

time = 0
done = [False] * n
completion = [0] * n

while False in done:
    idx = -1
    for i in range(n):
        if arrival[i] <= time and done[i] == False:
            if idx == -1 or priority[i] < priority[idx]:
                idx = i
                
    if idx != -1:
        time += burst[idx]
        completion[idx] = time
        done[idx] = True
    else:
        time += 1

waiting = []
for i in range(n):
    waiting.append(completion[i] - arrival[i] - burst[i])

average = sum(waiting) / n

print("Waiting Time:", waiting)
print("Average Waiting Time:", average)