answer = 0
for i in range(2,999999):
    sum_ = 0
    for j in str(i):
        sum_ += int(j)**5
    if sum_ == i:
        print sum_
        answer += sum_
print answer
