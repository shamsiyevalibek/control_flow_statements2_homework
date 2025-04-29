def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    s = str(n)  
    max_digit = max(s) 
    return s.index(max_digit)
print(main(56473))