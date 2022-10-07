#rearrange the elements of the array in a zig-zag fashion
# for input:		      [4, 3, 7, 8, 6, 2, 1]
# expected output:		[3, 7, 4, 8, 2, 6, 1]



def zigZag(arr, n):
  # using flag helps to conditionaly apply the operation in alternate manner
  flag = True
  for i in range(n-1):
    if flag:
	    if arr[i] > arr[i+1]:
  		  arr[i],arr[i+1] = arr[i+1], arr[i]
    else:
       if arr[i] < arr[i+1]:
  		    arr[i],arr[i+1] = arr[i+1], arr[i]
  		        
    flag = bool(1 - flag)
  print(arr)
	
# Driver program
arr = [4, 3, 7, 8, 6, 2, 1]
n = len(arr)
zigZag(arr, n)