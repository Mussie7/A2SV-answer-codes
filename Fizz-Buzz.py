def fizzBuzz(n, lists):
    List = []
    for i in range(n):
        i+=1
        if i % 3 == 0:
            List.append("Fizz")
        elif i % 5 == 0:
            List.append("Buzz")
        elif i % 15 == 0:
            List.append("FizzBuzz")
        else:
            List.append(str(i))
    return List
