def ready_queue_checker(job_list, time):
    ready_queue = [] 
    for item in job_list:
        if (time >= item[1]) and (P_state[item[2]] == 0):
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
    P_state = [0]*n 
     
    for i in range(n):
        print(f"For process {i+1}:")
        AT = int(input("  Arrival Time: "))
        BT = int(input("  Burst Time: "))        
        P = int(input("   Priority: "))
        arrivalTime.append(AT)
        burstTime.append(BT)
        priority.append(P)

    job_list = list(zip(priority, arrivalTime, P_id, burstTime))

    timePassed = 0
    process_left = n
    while(process_left):
        ready_queue = ready_queue_checker(job_list, timePassed)
        if len(ready_queue):
            process = min(ready_queue)
            aT = process[1] 
            bT = process[3]
            pId = process[2]
            completionTime[pId] = timePassed = timePassed + bT
            TAT[pId] = completionTime[pId] - aT
            WT[pId] = TAT[pId] - bT
            P_state[pId] = 1
            
            process_left -= 1
                
        else:
            timePassed += 1

    print("Therefore, the TAT and WT of the processes is as follows:")
    for i in range(n):
        print(f"Process {i+1}:\n\tTAT= {TAT[i]}\tWT= {WT[i]}")

    print(f"Average TAT = {sum(TAT)/n}")
    print(f"Average WT = {sum(WT)/n}")