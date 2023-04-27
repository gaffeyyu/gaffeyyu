import time

def focus_timer(mins):
    focus_minutes = mins
    focus_seconds = mins * 60
    
    print(f"Set your focus for {focus_minutes} minutes.")
    
    for i in range(focus_seconds, 0, -1):
        minutes, seconds = divmod(i, 60)
        time_left = f"{minutes:02d}:{seconds:02d}"
        
        print(focus_minutes, "minute(s) remaining.", time_left, end="\r")
        time.sleep(1)
    
    print("Time is up!")
    
focus_timer(25) # Set the timer to focus for 25 minutes
