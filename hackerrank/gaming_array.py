def gaming_array1(arr):
    # Write your code here
    if not arr or len(arr) < 1:
        return 'BOB'
    player = 'BOB'
    while True:
        arr = arr[:arr.index(max(arr))]
        if len(arr) > 0:
            if player == 'BOB':
                player = 'ANDY'
            else:
                player = 'BOB'
        else:
            return player

def gaming_array(arr):
    # Write your code here
    mx, __mx = [], 0 # store left max
    for i in arr:
        if i>__mx:
            __mx = i
        mx.append(__mx)
    ans = 0;
    #print 'Hi'
    #print n, arr,mx
    j=len(mx)-1
    while j>=0:
        #print j,' ==> ',
        while j>=0 and arr[j]!=mx[j] :
            j-=1;#find left max actual position in arr and split array over that point
        j-=1
        #print j
        ans+=1;#count as this one partition(Step)
    if ans%2==1:
        return 'BOB'
    else:
        return 'ANDY'


if __name__ == "__main__":
    assert gaming_array([7, 4, 6, 5, 9]) == 'ANDY'
