def mintotal(traingle):
    if not traingle:
        return 0

    result = [num for num in traingle[-1]]

    for row in range(len(traingle)-1,-1,-1):
        for col in range(0, row+1):
            result[col] = traingle[row][col] + min(result[col]+result[col+1])

    return result[0]