# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    for i in range(elements):
      if len(arrA)>0 and len(arrB)>0:
        if arrA[0] < arrB[0]:

          merged_arr[i] = arrA[0]
          arrA = arrA[1:]
        else:
          merged_arr[i] = arrB[0]
          arrB = arrB[1:]
      else:
        if len(arrA) == 0:
          merged_arr[i:] = arrB
        else:
          merged_arr[i:] = arrA
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr)>1:
      new_array = merge([arr[0]],merge_sort(arr[1:]))
    else:
      new_array = arr
    return new_array


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    """merge two sorted arrays in place - truly in place this time
    i had some other versions which used two arrays"""
    for i in range(len(arr[start:middle])+len(arr[middle:end])):
      if arr[middle:end]==[] or start==middle:
        pass
      elif arr[start:middle][0] < arr[middle:end][0]:
        start +=1
      else:
        #print(start,middle,end)
        arr[start : middle + 1] = [arr[middle:end][0]] + arr[start:middle]
        #print(arr)
        middle +=1
        start +=1
        ar2_len = len(arr2)
    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
