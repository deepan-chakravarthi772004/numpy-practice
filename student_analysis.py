import numpy as np

marks = np.array([
    [85,90,78],
    [70,88,92],
    [60,75,80],
    [95,89,96],
    [45,55,50]
])

print("Student Marks:")
print(marks)

# Total marks of each student
total = np.sum(marks,axis = 1)

# Average marks of every student
average = np.mean(marks,axis = 1)

# Highest and Lowest mark of each student
highest = np.max(marks,axis = 1)
lowest = np.min(marks,axis = 1)

print("\nTotal marks:",total)
print("Average marks:",average)
print("Highest marks:",highest)
print("Lowest marks:",lowest)

# Subject wise average
print("Subject averages:",np.mean(marks,axis=0))

#Overall class average
print("Overall average:",np.mean(marks))

# Pass if average >= 50
passed = average >= 50

for i in range (len(marks)):
    result = "PASS" if passed[i] else "FAIL"

    print(f"Student {i+1}:Average = {average[i]:.2f}",{result})

# Rank students by total marks

ranking = np.argsort(total)[::-1]

print("\nStudent ranking:")

for rank, index in enumerate(ranking,start=1):
    print(f"Rank{rank}:Student{index+1} - {total[index]}marks")