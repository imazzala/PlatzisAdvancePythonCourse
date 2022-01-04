def make_division_by(n):
	
    def division(x):
        return x / n

    return division

 
def make_repeater_of(n):
    
    def repeater(string):
        assert type(string) == str, "solo puedes utilizar cadenas"
        return string * n

    return repeater


def run():
    repeat5 = make_repeater_of(5)
    print(repeat5("Hola"))

    division_by_3 = make_division_by(3)
    print(division_by_3(18))
    division_by_5 = make_division_by(5)
    print(division_by_5(100))


if __name__ == "__main__":
    run()