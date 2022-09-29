import string

alphabet_list = list(string.ascii_lowercase)

f = open("data/hamlet.txt","r")
text = f.read()
text = text.lower()

frequency = []
i = 0

for i in alphabet_list:
	frequency.append(text.count(i))

sum(frequency)

print("Letter Frequency in frequency order")
print("+----------+")
print("| C | freq |")
print("+----------+")

alphabet_result = []
for i in range(len(alphabet_list)):
	alphabet_result1 = frequency[i] / sum(frequency) * 100
	alphabet_result.append(alphabet_result1)
	
sort = sorted(alphabet_result, reverse=True)

for i,x in enumerate(sort):
	alphabet_sort = alphabet_list[alphabet_result.index(x)]
	print("| %s |%6.2f|" %(alphabet_sort, sort[i]))
	i += 1
print("+----------+")
