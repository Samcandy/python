a = ''
a =input('please input the number: ')
b = ''
zero=['  000',
      ' 0   0',
      '0     0',
      '0     0',
      '0     0',
      ' 0   0',
      '  000']

one=['  1 ',
     '111 ',
     '  1 ',
     '  1 ',
     '  1 ',
     '  1 ',
     '11111']
def pr_zero(a):
	for i in range(7):
		print zero[i]
def pr_one(a):
	for i in range(7):
		print one[i]
def pr(a):
	if a == 0:
		pr_zero(a)
	elif a == 1:
		pr_one(a)
while a > 0:
	if a % 2 == 1:
		b = b+'1'
		a = a / 2
	elif a % 2 == 0:
		b = b+'0'
		a = a / 2
	elif a == 1:
		b = b+'1'
def reverse(string): 
	begin = 0 
	end = len(string) - 1 
	strlist = [i for i in string] 
	while(begin < end):
		a = strlist[begin]
		strlist[begin] = strlist[end]
		strlist[end] = a
		begin += 1
		end -= 1
	return "".join(strlist) 
b = reverse(b)

for i in b:
	pr(int(i))
	print
