__author__ = 'Bartlomiej Ciurus'


print(5 == 5)  # true, 5 is equals to 5
print(4 > 5)  # false, 5 is greater than 4
print(True)  # true
print(False)  # false
print(type(1))  # <class 'int'> 1 is integer by default
print(type(0))  # <class 'int'> 0 is integer by default

x = 5
print(x == 5 and 3)  # 3, parentheses needed
print(x == 4 and 3)  # false, because first compare is false so second is not checked
print(3 and x == 5)  # true, because 3 is converted to boolean true and x is equals to 5,
#  so logical sum will return true
print(3 and x == 4)  # false, because 3 is converted to boolean true and x is lesser than 5,
#  so logical sum will return false
print(1 < x < 9)  # true, x is greater than 1 and lesser than 9
print(isinstance(True, int))  # true, because True is represented also in integer
print(isinstance(True, bool))  # true, because True is represented in bool by default
