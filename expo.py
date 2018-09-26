def raise_power(base_num, expo_num):
    result = 1
    for index in range(expo_num):
        result = result * base_num
    return result

# print(raise_power(3, 4))
print(raise_power(423, 332))