# Gabriel KUKA 

# Round Robin scheduling algorithm for OS processes

# Each process has a number of cpu bursts needed to complete the execution of that process
# quantum stores the number of cpu bursts allocated for each process
# n stores the total number of processes in the system
# current_time stores the "actual" linear time of computations 
# Arrival time is the time at which the process enters the system (the ready queue)

# The turn around time is the actual time when the process completed - arrival time
# The waiting time of a process is the turn around time - burst time

# This program calculates the average waiting time for a process and the average turn around time

quantum, n, current_time = 0, 0, 0;

def enterData():
	
	global quantum, n;
	
	quantum = int(input("Enter the quantum for each process: "));
	n = int(input("Enter the number of processes: "));
	
	arrival_time = [0] * n;
	burst_time = [0] * n;	
		

	for i in range(n):
		print("Enter data for process {}".format(i+1));
		arrival_time[i] = int(input("Enter the arrival time for p{}: ".format(i+1)));
		burst_time[i] = int(input("Enter burst time for process{}: ".format(i+1)));

	displayData(arrival_time, burst_time);
			

def Round_Robin(burst_time):
	global n, quantum, current_time;
	
	rem_bt = [0] * n;
	waiting_time = [0] * n;
	turn_around_time = [0] * n;
	total_wt, total_tat = 0, 0;
	
	for i in range(n):
		rem_bt[i] = burst_time[i];
	
	while(True):				# loop until all processes are completed
		exec_done = True;
		
		for i in range(n):		# loop through processes
			if rem_bt[i] > 0:	# if process[i] isn't completed
				exec_done = False;
				if rem_bt[i] > quantum:
					current_time += quantum;					
					rem_bt[i] -= quantum;
				else:
					current_time += rem_bt[i];
					waiting_time[i] = current_time - burst_time[i];
					turn_around_time[i] = burst_time[i] + waiting_time[i];
					rem_bt[i] = 0;

		if exec_done == True: 		# if all processes are completed
			break;	
		

	for i in range(n):			# compute total waiting time and total turn around time
		total_wt += waiting_time[i];
		total_tat += turn_around_time[i];

	displayResults(waiting_time, turn_around_time, total_wt, total_tat)
			
					
def displayData(arrival_time, burst_time):
	
	print("\nQuantum is ", quantum)	

	for i in range(n) : 
		print("Process ", i+1, "\tArrival Time=",arrival_time[i], " Burst Time=",burst_time[i])
	
	Round_Robin(burst_time)

def displayResults(waiting_time, turn_around_time, total_wt, total_tat):
	
		print("\t\t\t\t~~~ Final Results ~~~\n");
		print("Process    Waiting Time    Turn Around Time");
		for i in range(n):
			
			print(" ",i+1,"\t\t",waiting_time[i],"\t\t",turn_around_time[i]);

		print("\nAverage waiting time per process: %.5f" %(total_wt/n))
		print("Average turn around time per process: %.5f" %(total_tat/n))


if __name__ == "__main__" :
	enterData();
	