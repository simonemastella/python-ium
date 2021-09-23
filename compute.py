small = [[1, 2, 3, 4, 5, 6],
         [7, 8, 9, 10, 11, 12],
         [13, 14, 15, 16, 17, 18],
         [19, 20, 21, 22, 23, 24],
         [25, 26, 27, 28, 29, 30],
         [31, 32, 33, 34, 35, 36],
         ]
only = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
to_comp = [[0, 0, 0, 0],
           [1, 0, 0, 0],
           [0, 0, 0, 0]]
comp = [[0,0,0]
        ]
big=[]

def print_array(arr):
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            print(arr[x][y], end=" ")
        print()


def get_slice(arr, startW, startY, width, height):
    result = []
    for row in range(height):
        result.append(arr[row+startY][startW:width+startW])
    return result


def compare_all_slice(arrSmall, arrBig):
    arrSmallN = arrSmall
    arrSmallE = list(list(x)[::-1] for x in zip(*arrSmallN))
    arrSmallS = list(list(x)[::-1] for x in zip(*arrSmallE))
    arrSmallW = list(list(x)[::-1] for x in zip(*arrSmallS))
    assert arrSmallN == list(list(x)[::-1] for x in zip(*arrSmallW))
    height = len(arrSmallN)
    width = len(arrSmallN[0])
    for i in range(len(arrBig)-height+1):
        for j in range(len(arrBig[i])-width+1):
            if arrSmallN == (get_slice(arrBig, startW=j, startY=i, width=width, height=height)):
                print("ohYesN",arrSmallN)
            if arrSmallS == (get_slice(arrBig, startW=j, startY=i, width=width, height=height)):
                print("ohYesS",arrSmallS)
                
    height, width = width, height
    for i in range(len(arrBig)-height+1):
        for j in range(len(arrBig[i])-width+1):
            if arrSmallE == (get_slice(arrBig, startW=j, startY=i,width=width, height=height)):
                print("ohYesE",arrSmallE)
            if arrSmallW == (get_slice(arrBig, startW=j, startY=i, width=width, height=height)):
                print("ohYesW", arrSmallW)
    print("ok")
    pass


for i in range(1, 11):
    big.append([])
    for j in range(1, 11):
        big[i-1].append(i*j)

# print_array(small)

# print_array(get_slice(small, startW=1, startY=1, width=3, height=3))
compare_all_slice(comp, to_comp)
