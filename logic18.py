def main(a):
    """Given a five-digit integer a, check the following statement "All digits of the number are in descending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    b=a%100000//10000
    c=a%10000//1000
    d=a%1000//100
    e=a%100//10
    f=a%10
    return a>b>c>d>e
print(main(98754))