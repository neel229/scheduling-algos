def ready_queue_checker(job_list, time):
    ready_queue = [] 
    for item in job_list:
        if (time >= item[1]) and burstTime[item[2]]:
            ready_queue.append(item)
    return ready_queue

if __name__ == "__main__":        

    n = int(input("Enter the total number of processes: "))

    arrivalTime = []
    burstTime = []
    priority = []
    completionTime = [0]*n
    TAT = [0]*n
    WT = [0]*n
    P_id = list(range(n))
 
    for i in range(n):
        print(f"For process {i+1}:")
        AT = int(input("   Arrival time: "))
        BT = int(input("   Burst time: "))
        P = int(input("   Priority: "))
        arrivalTime.append(AT)
        burstTime.append(BT)
        priority.append(P)

    job_list = list(zip(priority, arrivalTime, P_id))
    burstTime_temp = [i for i in burstTime]

    timePassed = 0
    while True:
        ready_queue = ready_queue_checker(job_list, timePassed)
        if len(ready_queue):
            process = min(ready_queue)
            pId = process[2]
            completionTime[pId] = timePassed = timePassed + 1 
            burstTime[pId] -= 1   
        elif max(burstTime) == 0:
            break
        else:
            timePassed += 1
    

    print("Therefore, the TAT and WT of the processes is as follows:")
    for i in range(n):
        TAT[i] = completionTime[i] - arrivalTime[i]
        WT[i] = TAT[i] - burstTime_temp[i]
        print(f"Process {i+1}:\n\tTAT= {TAT[i]}\tWT= {WT[i]}")

    print(f"Average TAT = {sum(TAT)/n}")
    print(f"Average WT = {sum(WT)/n}")