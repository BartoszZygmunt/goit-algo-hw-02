import queue
import threading #requests in parallel
import time
import random
import keyboard
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"
finish = False # Flag to stop the program

# Create a new / empty queue
request_queue = queue.Queue()

# Create new request and add to the queue
def generate_request():
    global finish
    while not finish:
        if keyboard.is_pressed('esc'): 
            finish = True # Press 'ESC' to exit the program
            break
        request_id = random.randint(10000, 99999)  # Generating a unique request ID
        request_queue.put(request_id)
        print(f"{RED}Generated request ID: {request_id}{RESET}")
        time.sleep(random.uniform(0.5, 1.5))  # Simulate the time interval for generating requests

# Function to process requests from the queue
def process_request():
    global finish
    while not finish:
        if keyboard.is_pressed('esc'): 
            finish = True # Press 'ESC' to exit the program
            break
        if not request_queue.empty():
            request_id = request_queue.get()
            print(f"{GREEN}Processing request ID: {request_id}{RESET}")
            time.sleep(random.uniform(0.3, 4.0))  # Simulate the time taken to process the request
            request_queue.task_done() # Mark the request as done
        else:
            print("The queue is empty, waiting for new requests...")
            time.sleep(1)

def on_esc_press(event):
    global finish
    finish = True
    print("ESC pressed. Exiting...")


# Main cycle of the program
def main():
    print(f"{RED}Press 'ESC' to exit the program :){RESET}")
    time.sleep(1)
    
    # Set up the keyboard event listener
    keyboard.on_press_key('esc', on_esc_press)

    generate_thread = threading.Thread(target=generate_request)
    process_thread = threading.Thread(target=process_request)

    generate_thread.start()
    process_thread.start()

    generate_thread.join()
    process_thread.join()

if __name__ == "__main__":
    main()
