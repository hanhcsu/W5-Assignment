# Write a program that keeps track of purchased books and counts the amount of points awarded:
# Points list: 0 books - 0 points, 2 books - 5 points, 4 books - 15 points, 6 books - 30 points, 8 books - 60 points:
books = int(input("How many books did you purchase this month?: "))
while books < 0:
    print("Please enter a valid number.")
    books = int(input("How many books did you purchase this month?: "))
points = 0
if books >= 0 and books < 2:
    points = 0
elif books >= 2 and books < 4:
    points = 5
elif books >= 4 and books < 6:
    points = 15
elif books >= 6 and books < 8:
    points = 30
else:
    points = 60
# Output the number of points awarded:
print(f"You have earned {points} points this month.")