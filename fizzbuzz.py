
# FIZZBUZZ - https://yh.pingpong.se/courseId/11264/content.do?id=4707369
# Uppgiften går ut på att skriva ut alla tal mellan 1 och 100, ett tal per rad.
# - Om talet är jämnt delbart med 3 så ska ordet “Fizz” skrivas ut istället för talet.
# - Om talet är jämnt delbart med 5 så ska ordet “Buzz” skrivas ut istället för talet.
# - Om talet är jämnt delbart med både 3 och 5 så ska ordet “Fizzbuzz” skrivas ut istället för någonting annat.

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




