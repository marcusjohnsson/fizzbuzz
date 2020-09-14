# FIZZBUZZ - https://en.wikipedia.org/wiki/Fizz_buzz#:~:text=The%20player%20designated%20to%20go,by%2015%20become%20fizz%20buzz

# If num == 42 print "The answer to life, universe and everything"

nums = list(range(1,101))

for num in nums:
    str = ""
    if num % 3 == 0: 
        str += "Fizz"
    if num % 5 == 0:
        str += "Buzz"
    if not str == "":
        print(f"{str}!")
    else:
        print(num)
