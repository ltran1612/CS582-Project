import time
import sys

def Read(name):
    with open(name) as f:
        lines = f.readlines()
        return "\n".join(lines)

def clean_str(my_str):
    my_str = my_str.replace("\n", " ")
    return my_str

def is_empty(my_str):
    for c in my_str:
        if c != " " and c != "\n" and c != "\t" and c != 0:
            return False
    
    return True

def get_queries(name):
    query_string = Read(name)
    queries = query_string.split(";")
    queries = map(lambda x: clean_str(x), queries)
    return list(filter(lambda x: not is_empty(x) and x != ";", queries))

# https://stackoverflow.com/questions/5574702/how-do-i-print-to-stderr-in-python
def debug(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# mysql cursor and cassandra session
def run_experiment(mysql, cassandra, experiment_function):
    iterations = input("Enter the number of iterations of the experiment (empty for 1): ")
    if iterations == "":
        iterations = 1
    else:
        iterations = int(iterations)

    file_name = input("Enter the output file name (empty for no output file): ")
    if file_name != "":
        with open(file_name, 'w') as sys.stdout:
            experiment_function(mysql, cassandra, iterations)
            sys.stdout = sys.__stdout__
    else:
        experiment_function(mysql, cassandra, iterations)

# https://realpython.com/python-timer/
class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        if self.start_time is not None:
            raise Exception("Timer is running already. You should use stop first")
        
        self.start_time = time.perf_counter()
    
    def stop(self):
        if self.start_time is None:
            raise Exception("Timer has not started yet")
        
        end_time = time.perf_counter()
        duration = end_time * 1000 - self.start_time * 1000
        self.start_time = None
        return duration