from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()       # returns the exact date and time at the time the line of code is executed.
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Pasaron {time_elapsed.total_seconds()} segundos para ejecutar la función')
    return wrapper


@execution_time
def random_func():
    for _ in range(1, 1000000):
        pass

#random_func()


@execution_time
def suma(a: int, b: int) -> int:
    return a + b


@execution_time
def saludo(nombre="Yeder"):
    print(f"Hola {nombre}")


random_func()
suma(2,3)
saludo("Jose")

