'''
Simple Prototype
Goal:
Use "a", "b" for each index, acting as amino acid residues
Compare two sequences, F, H, to indicate
	2 different kingdoms
For each index, return its status:
	Is it unique to F, or H, or both?
'''

f = "aaaabbbb"
h = "bbbaaaaa"
result = []
length = len(f)
for i in range(0, length):
	# Traverse both lists and compare
	# Put comparison in result list
	if f[i] != h[i]:
		# result.append("dif")
		result.append("f:"+f[i]+" h:"+h[i])
	else:
		result.append("f = h")
print "f =",f
print "h =",h
print result
