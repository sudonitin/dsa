def find_complement(num):
    bit_count = 0
    temp_num = num
    sum_of_bits = 0
    while temp_num > 0:
        temp_num = temp_num // 2
        sum_of_bits += 2 ** bit_count
        bit_count += 1
    return num ^ sum_of_bits

print(find_complement(5))
print(find_complement(10))
print(find_complement(8))