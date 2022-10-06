# Function to return Peak element
# peak element: which is not smaller than the value of its adjacent elements(if they exists)
# function should return index to the any valid peak element
  
def peakElement(arr, n):
  # Code here
  # if only one element in array, return index=0
  if n < 2:
    return (0)
    
  # if first element is Peak element return index=0
  if arr[0] >= arr[1]:
    return 0
    
  # if last element is Peak element return index(n-1)
  elif arr[-1] >= arr[-2]:
    return (n-1)
  # check for rest elements and compair with it neighbour
  for i in range(1, n-1):
    if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
      return i
  
  return (-1)
  
print(peakElement([1,2,3], 3))