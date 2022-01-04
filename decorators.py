from datetime import date, datetime

def excecution_time(func):
    def wrapper(*args, **kwars):
        initial_time = datetime.now()
        func(*args, **kwars)
        final_time = datetime.now()
        time_elapse = final_time - initial_time
        print(f'Pasaron' + str(time_elapse.total_seconds()) + 'segundos')
    return wrapper
    

@excecution_time
def random_func():
    for _ in range(1, 1000000):
        pass


@excecution_time
def suma(a: int, b: int) -> int:
    return a + b

def run():
    random_func()
    suma(5, 6)


if __name__ == "__main__":
    run()