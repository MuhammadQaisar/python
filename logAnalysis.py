# logparse.py
import datetime
import sys

def get_next_event(sample):
    with open(sample, "r") as datafile:
        for line in datafile:
            if "dut: Device State: " in line:
                line = line.strip()
                action = line.split()[-1]
                timestamp = line[:19]
                yield (action, timestamp)

def compute_time_diff_seconds(start, end):
    format = "%b %d %H:%M:%S:%f"
    start_time = datetime.datetime.strptime(start, format)
    end_time = datetime.datetime.strptime(end, format)
    return (end_time - start_time).total_seconds()

def extract_data(sample):
    time_on_started = None
    errs = []
    total_time_on = 0

    for action, timestamp in get_next_event(sample):
        if "ERR" == action:
            errs.append(timestamp)
        elif ("ON" == action) and (not time_on_started):
            time_on_started = timestamp
        elif ("OFF" == action) and time_on_started:
            time_on = compute_time_diff_seconds(time_on_started, timestamp)
            total_time_on += time_on
            time_on_started = None
    return total_time_on, errs

if __name__ == "__main__":
    total_time_on, errs = extract_data(sys.argv[1])
    print(f"Device was {total_time_on} seconds")
    if errs:
        print("Timestamps of errors")
        for err in errs:
            print(f"\t{err}")
    else:
        print("No error events found.")
