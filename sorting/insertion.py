
def insertion(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1

		while j >= 0 and arr[j] > key:
			arr[j + 1] = arr[j]
			j -= 1

		arr[j+1] = key

L = [5, 7, 8, 2, 3, 1, 4, 6, 9]
insertion(L)
print(L)
