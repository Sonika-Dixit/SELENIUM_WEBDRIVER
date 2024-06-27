# Election season has started in Chefland and the election commission wants to know the count of eligible voters.

# There are 
# 𝑁
# N people in Chefland where the age of the 
# 𝑖
# 𝑡
# ℎ
# i 
# th
#   person in 
# 𝐴
# 𝑖
# A 
# i
# ​
#  .
# Given that a person needs to be at least 
# 𝑋
# X years old to vote, find the number of eligible voters.

# Input Format
# The first line of input will contain a single integer 
# 𝑇
# T, denoting the number of test cases.
# Each test case consists of multiple lines of input.
# The first line of each test case contains two space-separated integers 
# 𝑁
# N and 
# 𝑋
# X — the number of people in Chefland, and the minimum age required for a person to vote in Chefland.
# The next line contains 
# 𝑁
# N space-separated integers, where the 
# 𝑖
# 𝑡
# ℎ
# i 
# th
#   integer denotes the age of the 
# 𝑖
# 𝑡
# ℎ
# i 
# th
#   person.
# Output Format
# For each test case, output on a new line, the number of eligible voters in Chefland.


##solution:

t = int(input())
for i in range(t):
    n,x= map(int,input().split(" "))
    a = input().split()[:n]
    A="".join(a)
    # print(A)
    cnt=0
    for i in A:
        if int(i)>=x:
            cnt=cnt+1
    print(cnt)   