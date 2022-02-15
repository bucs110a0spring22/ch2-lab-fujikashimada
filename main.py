import random
#Part A
classes_per_week = 2
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
cost_per_class = ((cost_per_week)/(classes_per_week))
print("Cost per class:", cost_per_class)
print("Hope you have a nice day:)")
#Part B
my_list = ("rabbit", 7.0, 1997, "donut", "desk")
print(random.choice(my_list))
print(random.choice(my_list))
print(random.choice(my_list))
print(random.choice(my_list))
print(random.choice(my_list))