speed = int(input())
riding_time = int(input())
length_of_mkad = 109

kilometres_of_mkad = [point for point in range(length_of_mkad)]

flag = speed * riding_time
flagAb = abs(speed * riding_time)

if flagAb > length_of_mkad:
    while flagAb > length_of_mkad:
        flagAb -= length_of_mkad
if flag < 0:
    flagAb = -flagAb

print(kilometres_of_mkad[flagAb])
