#Write code for test score data entry validation to take scores and display “valid score” or “invalid score” if the entered score is not within 0 to 100.

score = int(input("Enter a score: "))

if score <= 0 or score > 100:
  print("Invalid score")
else:
  print("Valid score")