correct_ans = "abdabcdabc"
student_ans = "aaaaaaaaaa"
score = 0

for i in range(len(correct_ans)):
    if correct_ans[i] == student_ans[i]:
        score = score + 1

print(score)