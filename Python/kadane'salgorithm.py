def maxi(s):
   max_sum = s[0]
   cur_sum = s[0]
   
   for i in range(1,len(s)):
       cur_sum = max(s[i],cur_sum+s[i])
       max_sum = max(max_sum,cur_sum)
   return max_sum
   
t = int(input())
for i in range(t):
    n = input()
    s = list(map(int,input().split()))
    print(maxi(s))
