def main(n):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.
    
    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """
    b=n%100000//10000
    c=n%10000//1000
    d=n%1000//100
    e=n%100//10
    f=n%10

    return b+c+d+e+f>5-(b+c+d+e+f)
print(main(11001))