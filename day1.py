a=10
b=10
print(a&b)
print(a|b)
print(a^b)

def is_even(n) -> bool:
    """
    짝수 판정 함수
    :param n: 판정할 정수
    :return:  짝수면 True, 홀수면 False
    """

    if n%2==0:
        return True
    return False

#비트연산자 사용해서 함수구현
def is_even_bit(n)->bool:
    return not n&1

#n=int(input())

#입력값에 대한 8진수 함수구현
def dec_oct(n) -> int:
    if n==0:
        return ""
    else:
        return dec_oct(n//8) + str(n%8)
#n = int(input())
#print(dec_oct(n))



#입력된 숫자까지의 합을 구하기
#O(n)의 시간을 가진다.
def hap(n)->int:
    total=0 #1번
    for i in range(1,n+1):
        total+=i #n번
    return total
n = int(input()) #1번
print(hap(n))    #1번
#총 3+n번


#