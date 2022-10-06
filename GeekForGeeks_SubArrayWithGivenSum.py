#Function to find a continuous sub-array which adds up to a given number.
# GeekForGeeks 6/10/2022

# Sliding window method 
def subArraySum(arr, n, s): 
#Write your code here

  # check if s == 0 
  # then there is no such sub array 
  # hence return [-1]
  if s == 0:
    return [-1]
         
  currSum = arr[0]
  start = 0
  i = 1
  while i <= n:
         
    while currSum > s and start < i+1:
      # when the sum(window) become > s, 
      # we shorten our window by subtracting the start val
      currSum = currSum - arr[start]
      start += 1
         
    if currSum == s:
      # checking if currSum has become equal to s(required)
      return [start+1, i]
     
    if i < n:
      currSum = currSum + arr[i]
      # updating the currSum till it become > s 
    i+=1
  return [-1]
       
       
print(subArraySum([135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103, 154, 93, 183, 22, 117, 119, 96, 48, 127, 172, 139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134], 42, 468))

# expected output: [38, 42]