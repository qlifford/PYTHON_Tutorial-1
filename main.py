# list = ["a", "b", "c", "d", "e", "f", "g", 1, 2, 3, 4, 5, 6,  7, True, False] # single dimentional list
# print(dir(list))

# list.append(6)
# counts = list.count(6)
# counts = list.clear()
# list.insert(1,"a1")

# print(list)

# multi dimentional list
# my_list = [123, 456, ["banana", "apple", "cherry",[True, False]]]
# print(my_list[2][3][0])








# exercise
# 1. print 5.4 in console
# 2. print 'green' in console
# 3. print 3 in console
# 4. print 'Prado' in console
# 5. print True in console
# 6. print "cheers" in console
# 7. What is the element at index [1][1] in console
# multi_dim_list = [[1, 2, 3], [[5.4, 3.1], [True, False, ["Prado", "Nissan"]]],"Cheers",['green', 'blue', 'yellow']]

# print(multi_dim_list[3][0])
# print(multi_dim_list[1][1][0])

# Tuples
# my_tuple = ((1, 2, 3, 4), 5, 6, 7, 8, 9, 10,9)
# print(my_tuple.count(9))
# x = list(my_tuple[0] + my_tuple)
# print(x)
# def chk_prime(n):
#     if n == 2:
#         # return True
#         print(True)
#     for i in range(2, n):
#         if n % i == 0:
#             # return False
#             print(False)
#     # return True 
#     print(True)
# chk_prime(4)

# import keyword

# print(keyword.kwlist)
# print('This is a\nNew line\nThis is a   tabbed line\tit\'s nice') 

# a = "let    ter"
# b = a.strip()
# print(dir(b))
# print(b.upper())
# import requests

# counter = 10

# while counter:
#     print (counter)
#     counter -= 1
# response = None

# while response not in [True or False]:
#     response = input("Please enter True or False\n")
#     response = response.lower() == "true"
# print ("Thank you for your response!")

# value = "python"
# result = int(value)
# print(result)
# try:
#     result = int(value).strip()
#     print(type(result))
# except ValueError as e:
    # print(e)

li = [11, 12, 13, 14]
l = iter(li)
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
print(next(li))