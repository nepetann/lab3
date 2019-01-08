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
cleanL=l.copy()

def foo (s,amount,k,tree):

  if (amount>1):
    cent = int(amount/2)+1
    l[k]=l[k]+s[cent-1]
    first = s[:cent-1]
    second = s[cent:]
    foo(first,cent-1,k+1,tree)
    foo(second,amount-cent,k+1,tree)
  elif  (amount==0):
    tree[k]=tree[k]+'-'
  elif (amount==1):
    tree[k]=tree[k]+s
  return (tree)


tree=foo(s,amount,0,l)
print ('\nBinary tree:')
for i in tree:
  print (i)

l.clear()
l=cleanL.copy()
newS=[]
for i in s:
    if i not in newS:
        newS.append(i)
newS = ''.join(newS)
newAmount = len(newS)
print ('\nString without repetitions:\n',newS)

newTree=foo(newS,newAmount,0,l)
print ('\nBinary tree:')
for i in newTree:
  print (i)

rep={}
for i in newS:
  rep[i]=0
for i in s:
  rep[i]+=1

hesh={}
print('Hash-table:')
for key in rep:
  hesh[rep[key]]=[]
for key in rep:
  hesh[rep[key]]+=key
for key in sorted(hesh):
  print(key,'-',hesh[key])
  
