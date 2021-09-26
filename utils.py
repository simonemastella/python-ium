
def print_array(arr):
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            print(arr[x][y], end="\t")
        print()


def get_slice(arr, startW, startY, width, height):
    result = []
    for row in range(height):
        result.append(arr[row+startY][startW:width+startW])
    return result


def random_matrix(w,h):
    import random
    return  [[random.getrandbits(1) for z in range(w)]for z in range(h)]

