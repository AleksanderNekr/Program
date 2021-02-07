def solution(length_of_mkad, speed, riding_time):
    s = speed * riding_time
    sM = s % length_of_mkad
    sMM = length_of_mkad + sM
    solve = sMM % length_of_mkad
    return solve
speed = int(input())
riding_time = int(input())
length_of_mkad = 109
print(solution(length_of_mkad, speed, riding_time))