def mergesort(arr):
	if len(arr) > 1:
		L = arr[:len(arr)//2]
		R = arr[len(arr)//2:]

		mergesort(R)
		mergesort(L)

		i, j, k = 0, 0, 0

		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i +=1

			else:
				arr[k] = R[j]
				j +=1

			k += 1

		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

arr = [2,5,7,8,9,3,4,1,6]
mergesort(arr)
print(arr)
