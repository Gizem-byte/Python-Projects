print("Grade Calculator")



scores = []

while True:
    score = input("Enter a test score (or 'done' ): ")
    if score.lower() == 'done':
        print("Good bye")
        break
    scores.append(float(score))
    average_test_score = sum(scores) /len(scores)
    print(f"Average score: {average_test_score:.1f}")

    if average_test_score >= 90 :
 
       print("Grade: A")

    elif average_test_score >=80:
    
       print("Grade: B")

    elif average_test_score >=70:
    
       print("Grade: C")

    elif average_test_score >=60:
    
       print("Grade: D")

    else:
       print("Grade D or F")



    

