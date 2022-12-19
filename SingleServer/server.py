# Simulation of a Single Server Queueing System in python
import random
import math

Q_LIMIT = 100 # Limit on the queue length
BUSY = 1 # Server is busy
IDLE = 0 # Server is idle

next_event_type = 0
num_custs_delayed = 0 # Initialize statistical counter
num_delays_required = 0
num_events = 0
num_in_q = 0 # Initialize state variable (number in queue)
server_status = IDLE # Initialize state variable (server status)

area_num_in_q = 0.0 # Initialize statistical counter
area_sever_status = 0.0 # Initialize statistical counter
mean_interarrival = 0.0 
mean_service = 0.0
sim_time = 0.0 # Initialize Simulation Clock
time_last_event = 0.0 # Initialize state variable (time of last event)
total_of_delays = 0.0 # Initialize statistical counter

time_arrival = [0] * (Q_LIMIT+1)
time_next_event = [0] * 3


def initialization(): # Initialize function.

    # Initialize the event list. Since no customers are present, the departure (service completion) event is eliminated from consideration.

    time_next_event[1] = sim_time + expon(mean_interarrival) # Arrival event # mean_interarrival is 1.0

    # Set to a large number to when initializing to ensure first event is arrival
    time_next_event[2] = 1.0e30 # Representation of 10^30   # Departure event


def timing(): # Timing function. 

    global sim_time, next_event_type, num_events

    # Set to a large number
    main_time_next_event = 1.0e29 # Representation of 10^29
    next_event_type = 0

    # Determine the event type for the next event to occur. 

    for i in range(num_events): # num_events is set to 2 in main
        if (time_next_event[i+1] < main_time_next_event): # Check between Arrival Event time_next_event[1] and Departure Event time_next_event[2]
            main_time_next_event = time_next_event[i+1] # Sets the main_time_next_event to the time for the specific event type. First iteration will have it set to time of Arrival Event
            next_event_type = i+1 # First iteration will have next_event_type set to Departure Event after execution of for loop once

    # Check to see whether the event list is empty.

    if (next_event_type == 0):
        # The event list is empty, so stop the simulation.
        print(f"\nEvent list is empty at time {sim_time}", file = outfile)
        exit(1)

    # The event list is not empty, so advance the simulation clock. 
    sim_time = main_time_next_event # First iteration will have simulation time set to time of Arrival Event # Second iteration will have it set to time of Departure Event

def arrive():

    global server_status, num_in_q, total_of_delays, num_custs_delayed, sim_time, mean_interarrival, time_next_event, Q_LIMIT, time_arrival, mean_service
    
    delay = 0.0

    # Schedule next arrival.

    time_next_event[1] = sim_time + expon(mean_interarrival) # Arrival event # mean_interarrival is 1.0

    # Check to see whether server is busy.
    if (server_status == BUSY):
        # Server is busy so increment the number of customers in the queue.
        num_in_q += 1


        # Check to see whether an overflow condition exists.
        if(num_in_q > Q_LIMIT):
            # The queue has overflowed, so stop the simulation.
            print("\nOverflow of the array time_interval at", file = outfile)
            print(f" time {sim_time}", file = outfile)
            exit(2)

        # There is still room in the queue, so store the time of arrival of the 
        # arriving customer at the (new) end of time_arrival.    
        
        time_arrival[num_in_q] = sim_time # Time of arrival of the specific customer(sim_time) is stored in time_arrival
    
    else:
        # Server is idle, so arriving customer has a delay of zero. 
        delay = 0.0
        #total_of_delays += delay

        # Increment the number of customers delayed, and make server busy.
        num_custs_delayed += 1
        server_status = BUSY

        # Schedule a departure (service completion).  Initially for the first iteration, we had set it to a large number to remove it from consideration
        time_next_event[2] = sim_time + expon(mean_service) # Departure event


def depart():   # Departure event function.

    global total_of_delays, num_custs_delayed, num_in_q, server_status, time_next_event, sim_time, time_arrival, mean_service
    delay = 0.0

    # Check to see whether the queue is empty.
    if (num_in_q == 0):

        # The queue is empty so make the server idle and eliminate the
		# departure (service completion) event from consideration.
        server_status = IDLE
        time_next_event[2] = 1.0e30 # Departure event # Set to a large number to remove it from consideration

    else:
        # The queue is nonempty, so decrement the number of customers in queue.
        num_in_q -= 1
        
        # Compute the delay of the customer who is beginning service
		# and update the total delay of accumulator.
        delay = sim_time - time_arrival[1]
        total_of_delays += delay

        # Increment the number of customers delayed, and schedule departure.
        num_custs_delayed += 1
        time_next_event[2] = sim_time + expon(mean_service) # Departure event

        # Move each customer in queue (if any) up one place.

        for i in range(num_in_q):
            time_arrival[i+1] = time_arrival[i + 2]

def report():   # Report generator function
    # Compute and write estimates of desired measures of performance.
    global total_of_delays, num_custs_delayed, sim_time, area_num_in_q, area_sever_status

    print(f"\nAverage delay in queue  {round((total_of_delays/num_custs_delayed),4)} minutes\n\n", file = outfile)
    print(f"Average no in queue  {round((area_num_in_q/sim_time),4)}\n\n", file = outfile)
    print(f"Server Utilization  {round((area_sever_status/sim_time),4)}\n\n", file = outfile)
    print(f"Time Simulation ended  {round(sim_time,4)}", file = outfile)
    #Change to 4 decimal places


def update_time_avg_stats():    # Update area accumulators for time-average statistics.

    global time_last_event, sim_time, area_num_in_q, area_sever_status, num_in_q, server_status

    time_since_last_event = 0.0 

    # Compute time since last event, and update time_last_event marker. 
    time_since_last_event = sim_time - time_last_event # Second iteration will have Time of Arrival - Time of Departure
    time_last_event = sim_time # First iteration will update time_last_event to be time of the Arrival Event

    # Update area under number-in-queue function
    """
        Area is the integral of curve Q(t) dt from 0 to T(n) divided by T(n)
        Q(t) is number of customers in queue at time t for t >= 0
        T(n) is the time required to observe n delays in queue
        This simplifies to areas of rectangles as simulation progresses through time
    """
    area_num_in_q += num_in_q * time_since_last_event # First iteration will have it as zero since there are no people in queue

    # Update area under server-busy indicator function. 
    """
        Area is the integral of the curve B(t) dt from 0 to T(n) divided by T(n)
        B(t) is whether the server is busy(1) or idle(0)
        T(n) is the time that the server is busy or idle
        It simplifies to areas of a rectangle as simulation progresses through time
    """
    area_sever_status += server_status * time_since_last_event  # First iteration will have it as zero as the server is idle(0)

def expon(mean): # Exponential variate generation function.

    # Return an exponential random variate with mean "mean".
    return -(float(mean)) * math.log(random.random())


if __name__ == '__main__':
    # Open input and output files.
    infile = open("mm1.in", "r")
    outfile = open("mm2.out", "r+")

    #  Specify the number of events for the timing function 
    num_events = 2

    # Read input parameters
    input_parameters = infile.readline().split()
    
    # Store input parameters in specific variables
    mean_interarrival = input_parameters[0] # 1.0  
    mean_service = input_parameters[1] # 0.5
    num_delays_required = input_parameters[2] # 1000

    # Write report heading and input parameters
    print('Single-server queueing system\n\n', file = outfile)
    print('Mean interarrival time {mean_interarrival}, \n\n', file = outfile)
    print(f"Mean service time {mean_service} \n\n", file = outfile)
    print(f"No of Customers {num_delays_required} \n", file = outfile)
    
    # Initialize the simulation 
    initialization()

    # Run the simulation while more delays are still needed i.e. number of customers delayed are less than 1000
    while (num_custs_delayed < int(num_delays_required)):

        # Determine the next event 
        timing()

        # Update time-average statistical accumulators. 
        update_time_avg_stats()

        # Invoke the appropriate event function 
        if (next_event_type == 1):
            arrive()
        elif (next_event_type == 2):
            depart()

    # Invoke the report generator and end the simulation
    report()

    # Return file pointer to beginning and ouput content to screen
    outfile.seek(0)
    print(outfile.read())

    # Close both files
    infile.close()
    outfile.close()