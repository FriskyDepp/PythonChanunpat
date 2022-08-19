acc_score = int(input("Input ur accumulated score : "))

mid_score = int(input("Input ur midterm score : "))

final_score = int(input("Input ur final score : "))

total_score = acc_score+mid_score+final_score
print

if total_score>=80:
    print("A")
elif total_score>=75:
    print("B+")
elif total_score>=70:
    print("B")
elif total_score>=65:
    print("C+")
elif total_score>=60:
    print("C")
elif total_score>=55:
    print("D+")
elif total_score>=50:
    print("D")
elif total_score>=0:
    print("F")





