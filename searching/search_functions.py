def linear_search(data, key):
    for i in range(len(data)):
        if data[i] == key:
            return i
    return -1
def binary_search(data, key):
    left = 0
    right = len(data)-1

    while(left<=right):
        mid = int((left + right) / 2)
        if data[mid] == key:
            return mid
        elif key > data[mid]:
            left = mid + 1
        elif key < data[mid]:
            right = mid

    return -1

# print(linear_search([2,4,6,8,10,12,14,16,18,20], 8))
print(binary_search([3,6,7,19,25,32,45,51,52,63,63,69,79,80,95], 95))