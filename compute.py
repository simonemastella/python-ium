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


def compare_all_slice(arrSmall, arrBig):
    arrSmallN = arrSmall
    arrSmallE = list(list(x)[::-1] for x in zip(*arrSmallN))
    arrSmallS = list(list(x)[::-1] for x in zip(*arrSmallE))
    arrSmallW = list(list(x)[::-1] for x in zip(*arrSmallS))
    result = {"N": [],
              "S": [],
              "W": [],
              "E": []}
    assert arrSmallN == list(list(x)[::-1] for x in zip(*arrSmallW))
    height = len(arrSmallN)
    width = len(arrSmallN[0])
    for i in range(len(arrBig)-height+1):
        for j in range(len(arrBig[i])-width+1):
            if arrSmallN == (get_slice(arrBig, startW=j, startY=i, width=width, height=height)):
                result["N"].append({"x": j, "y": i})
            if arrSmallS == (get_slice(arrBig, startW=j, startY=i, width=width, height=height)):
                result["S"].append({"x": j, "y": i})

    height, width = width, height
    for i in range(len(arrBig)-height+1):
        for j in range(len(arrBig[i])-width+1):
            if arrSmallE == (get_slice(arrBig, startW=j, startY=i, width=width, height=height)):
                result["E"].append({"x": j, "y": i})
            if arrSmallW == (get_slice(arrBig, startW=j, startY=i, width=width, height=height)):
                result["W"].append({"x": j, "y": i})
    return result


if __name__ == "__main__":

    big = []
    comp = [[8]
            ]
    for i in range(1, 11):
        big.append([])
        for j in range(1, 11):
            big[i-1].append(i*j)

    # print_array(small)

    # print_array(get_slice(small, startW=1, startY=1, width=3, height=3))
    import time
    start_time = time.time()
    ris = compare_all_slice(comp, big)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(ris)
    print_array(big)
