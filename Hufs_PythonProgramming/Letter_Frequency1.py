f = open("data/hamlet.txt","r")
text = f.read()
text = text.lower()

frequency = []
i = 0

alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in alphabet_list:
	frequency.append(text.count(i))

sum(frequency)

print("Letter Frequency in alphabet order")
print("+----------+")
print("| C | freq |")
print("+----------+")

for i in range(len(alphabet_list)):
	print("| %s | %5.2f|" %(alphabet_list[i], frequency[i] / sum(frequency) * 100))
	i += 1
print("+----------+")
