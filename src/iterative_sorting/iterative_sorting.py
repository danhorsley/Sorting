# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
  for i in range(len(arr)-1):
    smallest = arr[i]
    pos = 0
    for j in range(len(arr[i+1:])):
      if arr[i+1:][j]<smallest:
        smallest = arr[i+1:][j]
        pos = j+1
    #print(i,pos,smallest)
    arr = arr[:i] + [arr[i+pos]] + arr[i:i+pos] + arr[i+pos+1:]
    #print(arr)
  return arr



# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
  passes = 1
  while passes!=0:
    passcount = 0
    for i in range(len(arr)-1):
      if arr[i]>arr[i+1]:
        a = arr[i]
        b = arr[i+1]
        passcount += 1
        arr[i] = b
        arr[i+1] = a
    passes = passcount
  return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr):
  count_dict = {}
  for i in range(len(arr)):

    item_to_count = arr[i]
    counter = 0
    if item_to_count in count_dict:
      pass
    else:
      for item in arr:
        if item <= item_to_count:
          counter += 1
      #print(item_to_count,counter)
      count_dict[item_to_count] = counter
      #print(count_dict)
  ret_arr = [0 for x in arr]
  for j in range(len(arr)):
      #print(j)
      #print('cd',count_dict[arr[-j]])
      ret_arr[count_dict[arr[-j]]-1] = arr[-j] 
      count_dict[arr[-j]] = count_dict[arr[-j]] - 1
      #print(count_dict)
  return ret_arr#, count_dict