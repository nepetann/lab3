print ('Print string: ')
s = input()
l = sorted(s)
s=''
for i in l:
  s=s+i
print ('\nSorted string:\n',s)
amount = len(s)
l=[]
two=1
l.append('')
while (two<amount):
  l.append('')
  two=two*2


def foo (s,amount,k):

  if (amount>1):
    cent = int(amount/2)+1
    l[k]=l[k]+s[cent-1]
    first = s[:cent-1]
    second = s[cent:]
    foo(first,cent-1,k+1)
    foo(second,amount-cent,k+1)
  elif  (amount==0):
    l[k]=l[k]+'-'
  elif (amount==1):
    l[k]=l[k]+s
  
foo(s,amount,0)
print ('\nBinary tree:')
for i in l:
  print (i)

newAmount=amount
for i in range(1,newAmount):
  if (s[i]==s[i-1]):
    s[i]=''
    newAmount-=1
