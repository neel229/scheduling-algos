# Program to run the FCFS scheduling algorithm

# Generate random number of processes using Random module

from random import randint

# Deduce the number of processes randomly using the randint function of Random module
processes = randint(2, 4)
pid_list = []  # list of Processes
completion_time = [0]*processes
turnaround_time = [0]*processes
waiting_time = [0]*processes

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

print("\n\nFollowing list shows the process ids with their corresponding arrival time and burst time in the format: 'PID', 'Arrival Time', 'Burst Time'")
print(list(zip(pid_list, arrival_time_list, burst_time_list)))


# Sorting the process ids on the basis of their arrival time
sorted_list = list(zip(arrival_time_list, burst_time_list, pid_list))
sorted_list.sort()


# Calculating the Turnaround time and waiting time
def Computation(sorted_list):
    time_track = sorted_list[0][0]
    for single_process in sorted_list:
        arrival_time = single_process[0]
        burst_time = single_process[1]
        pid = single_process[2]

        completion_time[pid] = time_track = time_track + burst_time
        turnaround_time[pid] = completion_time[pid] - arrival_time
        waiting_time[pid] = turnaround_time[pid] - burst_time

    return turnaround_time, waiting_time


turnaround_time_list, waiting_time_list = Computation(sorted_list)
print("\nTurnaround times are: \t", turnaround_time_list)

avg_turnaround_time = sum(turnaround_time_list) / len(turnaround_time_list)
print("\nAverage Turnaround time is: \t", avg_turnaround_time)

print("\nWaiting times are: \t", waiting_time_list)

avg_waiting_time = sum(waiting_time_list) / len(waiting_time_list)
print("\nAverage Waiting Time is: \t", avg_waiting_time)
