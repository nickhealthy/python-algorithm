def solution(arr):
    row, col = len(arr), len(arr[0])
    if row < col:
        new_row = [0] * col
        for _ in range(col - row):
            arr.append(new_row)

        return arr

    else:
        for i in range(len(arr)):
            for _ in range(row - col):
                arr[i].append(0)

        return arr