# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i in range(len(arr)):
    if arr[i]==target:
      return i
    else:
      pass

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1
  try:
    for i in range(len(arr)):
      my_point = (high+low)//2
      #print(high,low,my_point)
      if arr[my_point]>target:
        high = my_point
      elif arr[my_point]<target:
        low = my_point
      elif arr[my_point]==target:
        return my_point
  except:
    return -1

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low=0, high=0):
  low = 0
  high = len(arr)
  if len(arr) == 0:
    return -1 # array empty
  
  # TO-DO: add missing if/else statements, recursive calls
  my_point = (high+low)//2
  print(low,high,my_point,arr)
  #print(high,low,my_point)
  if arr[my_point]>target:
    return binary_search_recursive(arr[low:my_point], target)
  elif arr[my_point]<target:
    adjuster = my_point
    return binary_search_recursive(arr[my_point:high], target)+adjuster
  elif arr[my_point]==target:
    return my_point

  return -1
