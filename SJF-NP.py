from random import randint

# Deduce the number of processes randomly using the randint function of Random module
processes = randint(2, 4)
pid_list = []  # list of Processes
completion_time = [0]*processes
turnaround_time = [0]*processes
waiting_time = [0]*processes
P_state = [0]*processes

for i in range(processes):
    pn = i  # pn denotes process number
    pid_list.append(pn)

print("Following are the process ids")
print(pid_list)


def Arrival_Time(processes):
    arr_list = []
    for _ in range(processes):
        aT = randint(0, 10)  # at represents arrival time of a process
        arr_list.append(aT)

    return arr_list


arrival_time_list = Arrival_Time(processes)
print("\nFollwing are the arrival times along with process ids")

# Zip the arrival time of the process with their corresponding process number
print(list(zip(pid_list, arrival_time_list)))


def Burst_Time(processes):
    bt_list = []
    for _ in range(processes):
        bT = randint(2, 7)
        bt_list.append(bT)

    return bt_list


burst_time_list = Burst_Time(processes)

print("\nFollowing are the burst times along with process ids")
print(list(zip(pid_list, burst_time_list)))

print("\n\nFollowing list shows the process ids with their corresponding arrival time and burst time in the format: 'Burst Time', 'Arrival Time', 'PID'")
process_info = list(zip(burst_time_list, arrival_time_list, pid_list))
print(process_info)


def ready_queue_checker(job_list, time):
    ready_queue = []
    for item in job_list:
        if (time >= item[1]) and (P_state[item[2]] == 0):
            ready_queue.append(item)
    return ready_queue


timePassed = 0
process_left = processes
while(process_left):
    ready_queue = ready_queue_checker(process_info, timePassed)
    if len(ready_queue):
        process = min(ready_queue)
        aT = process[1]
        bT = process[0]
        pId = process[2]
        completion_time[pId] = timePassed = timePassed + bT
        turnaround_time[pId] = completion_time[pId] - aT
        waiting_time[pId] = turnaround_time[pId] - bT
        P_state[pId] = 1

        process_left -= 1

    else:
        timePassed += 1

print("Therefore, the TAT and WT of the processes is as follows:")
for i in range(processes):
    print(
        f"Process {i+1}:\n\tTAT= {turnaround_time[i]}\tWT= {waiting_time[i]}")

    print(f"Average TAT = {sum(turnaround_time)/processes}")
    print(f"Average WT = {sum(waiting_time)/processes}")
