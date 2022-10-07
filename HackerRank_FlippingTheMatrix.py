# Flippig the matrix question on hacker rank
# Difficulty : Medium, Sourcs: Hacker Rank
"""
# Question: Find max possible sum of 1st quadrant by,
# flipping any row or column any number of time


# Logic: we have to find the max(As) + max(Bs) + max(Cs) + max(Ds)
as (0,0) can only be caken by one of the A's
similarly (0,1) position can be taken by only one of the B's

[A  C  C  A]      1st Pass(A): {(0,0), (0,3), (3,0), (3,3)}
[B  D  D  B]      2st Pass(C): {(0,1), (0,2), (3,1), (3,2)}
[B  D  D  B]      3st Pass(B): {(1,0), (1,3), (2,0), (2,3)}
[A  C  C  A]      4th Pass(D): {(1,1), (1,2), (2,1), (2,2)}
"""


def flipping_matrix(matrix):
  t = len(matrix) - 1           #4 -1 = 3
  n = len(matrix) // 2          #4//2 = 2
  max_sum = 0
  
  for i in range(n): # 0, 1
    for j in range(n): # (0,0), (0,1), (1,0), (1,1)
      max_value = max(matrix[i][j], matrix[i][t-j], matrix[t-i][j], matrix[t-i][t-j])
      # pass1 i=0 j=0       [0][0],       [0][3]            [3][0]          [3][3]
      # pass2 i=0 j=1       [0][1],       [0][2],           [3][1],         [3][2]
      # pass3 i=1 j=0       [1][0],       [1][3],           [2][0],         [2][3]
      # pass4 i=1 j=1       [1][1],       [1][2],           [2][1],         [2][2]
      max_sum += max_value
  return max_sum
    
    
    
mat1 = [[112, 42, 83, 119],[56, 125, 56, 49],[15, 78, 101, 43],[62, 98, 114, 108]]
print(flipping_matrix(mat1))
    