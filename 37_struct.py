from struct import *
# store as bytes data

packed_date = pack('iif', 6, 19, 4.73)
print(packed_date)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))


#to get data back to normal b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'

original_data = unpack('iif',packed_date)
print(original_data)
print(type(packed_date))