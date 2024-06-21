#!/usr/bin/python3
output = ""
for i in range(99):
    output += "{} = 0x{:x}\n".format(i, i)
output += "98 = 0x{:x}".format(98)
print(output, end="")
