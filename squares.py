numbers = [1,2,3,4,5]
squares = (num*num for num in numbers)
print(next(squares),next(squares))
sqrs = list(squares)
print(sqrs)
