def non_neg_int(n):
    result = int(n)
    if result > 0:
        print("t")
        raise ValueError(result)
    return result

# while True:
#     try:
#         x = non_neg_int(input("please entrter a nonnegat : "))
#         if x == 999:
#             break
#         print('You entered',x)
#     except ValueError:
#         print('the value you entered is not acceptable')

non_neg_int(1)