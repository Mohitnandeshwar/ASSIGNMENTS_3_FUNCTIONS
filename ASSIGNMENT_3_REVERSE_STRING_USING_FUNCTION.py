def reverse(stri):
	if len(stri) == 0:
		return stri
	else:
		return reverse(stri[1:]) + stri[0]


stri = "Edyoda is Best"

print("The original string is : ", end="")
print(stri)

print("The reversed string(using recursion) is : ", end="")
print(reverse(stri))
