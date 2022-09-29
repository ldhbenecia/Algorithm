letters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

shuffle = [58, 36, 16, 69, 47, 56, 99, 84, 9, 60, 8, 2, 68, 3, 18, 13, 95, 46, 25, 63, 48, 28, 89, 45, 81, 85, 43, 59, 87, 96, 11, 65, 50, 66, 22, 62, 4, 27, 5, 0, 41, 75, 23, 53, 6, 40, 32, 92, 73, 39, 74, 31, 55, 82, 83, 94, 30, 17, 61, 49, 15, 35, 19, 51, 64, 72, 67, 42, 90, 38, 34, 76, 86, 44, 26, 70, 24, 88, 57, 21, 1, 10, 52, 71, 14, 33, 77, 20, 54, 93, 37, 12, 98, 29, 80, 7, 78, 79, 97, 91]

enc = "ZK8\n='8J=m>b=^8m=82>b\n=8=gUqmi8Xq>s3=\tpXs=OK>=3pi3Q= K8\n=^Ki=O8^=2i8b\npdbs=8J3=2Xpssp8J\nQ= K8\n=^Ki=s>$i3=,>!8X\n=8J3=r8'KQ= Ki=ri8\nsi^Q=4J3=`iQ"


enc2=''

for i in enc:
	n1=letters.index(i)
	n2=shuffle.index(n1)
	enc2+=letters[n2]
   
print(enc2)