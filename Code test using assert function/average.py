def average(L):
    if not L:
        return None
    return sum(L)/len(L)
if __name__ == "__main__":
    L = [1,2,3,4,5]
    expected_result = 3
    assert expected_result == average(L),"average(L) produced incorrect result"



'''
right hole assert kono problem korbena.
But wrong korle assertion error dekhabe.

assert holo jodi mittha hoy tahole porer
stringti print korbe assertion error a.
'''
