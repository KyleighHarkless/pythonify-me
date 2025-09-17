def ofun_power(base:int, power:int):
    # Base case once power reaches 0 function will stop
    if power == 0:
        return 1
    
    if power > 0: 
        return base * ofun_power(base, power - 1)
    # This will be used if the power if negative resulting in a fraction
    elif power < 0:
        return (1/base) * ofun_power(base, power + 1)
    

user_base = input("Input base: ")
user_power = input("Input power: ")

resulted_power = ofun_power(user_base, user_power)