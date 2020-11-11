def findNumber(arr, k):
    if arr.count(k) > 0:
        return "YES"
    return "NO"


if __name__ == "__name__":
    assert([1,2,3,4,5], 5) == "YES"