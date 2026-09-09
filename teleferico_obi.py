capacity = int(input())
students_num = int(input())
trips_num = 0

while (students_num > 0):
    students_num -= (capacity-1)
    trips_num += 1

print(trips_num)
