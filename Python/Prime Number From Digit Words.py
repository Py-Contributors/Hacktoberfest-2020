import math
myDictionary= {
      "one":1,
      "two":2,
      "three":3,
      "four":4,
      "five":5,
      "six":6,
      "seven":7,
      "eight":8,
      "nine":9,
      "ten":10,
      "eleven":11,
      "twelve":12,
      "thirteen":13,
      "fourteen":14,
      "fifteen":15,
      "sixteen":16,
      "seventeen":17,
      "eighteen":18,
      "nineteen":19,
      "twenty":20,
      "thirty":30,
      "forty":40,
      "fifty":50,
      "sixty":60,
      "seventy":70,
      "eighty":80,
      "ninety":90,
      "hundred":100,
  }

def Print_Prime_Numbers(number_in_text):
  text=number_in_text.strip().split(" ")
  num=0
  if len(text)<=2 and "hundred" not in text:
    for i in text:
      num+=myDictionary[i]
  else:
    num=myDictionary[text[0]]*myDictionary[text[1]]
    text=text[2:]

    for i in text:
      num+=myDictionary[i]

  print(num)
  primes=[]
  for i in range(2,num+1):
    primes.append(i)

  i = 2
  #from 2 to sqrt(number)
  while(i <= int(math.sqrt(num))):
      #if i is in list
      #then we gotta delete its multiples
      if i in primes:
          #j will give multiples of i,
          #starting from 2*i
          for j in range(i*2, num+1, i):
              if j in primes:
                  #deleting the multiple if found in list
                  primes.remove(j)
      i = i+1

  return primes

print(Print_Prime_Numbers("nine hundred ninety nine"))
