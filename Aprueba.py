exam_score = float(input("Enter exam score: "))
total_classes = float(input("Enter number of classes: "))
attended_classes = float(input("Enter number of classes attended: "))
if exam_score >= 70 and attended_classes >= 32:
    print("pass")
else:
    print("fail")
grade = ((exam_score/100 * 0.7) + (attended_classes/total_classes * 0.3)) * 100
print("The grade is: ",grade)