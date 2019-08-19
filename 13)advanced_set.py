list_grades = [33,44,55]
tuple_grades = (33,44,55)
set_grades = {33,44,55}

set_grades.add(60)
set_grades.add(60)
set_grades.add(50)
#print(set_grades)

lottery_num = {1,2,3,4,5}
winning_num = {1,3,5,7,9,11}

print(lottery_num.intersection(winning_num))

print(lottery_num.union(winning_num))

print({1,2,3,4}.difference({1,2}))