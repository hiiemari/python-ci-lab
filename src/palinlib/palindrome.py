def is_palindrome(text: str) -> bool:
    """Check whether or not a string is a palindrome.

    Args:
        - text: the string to check

    Returns:
        - True if a palindrome, otherwise False.
        
    Examples:
        - "abba" is a palindrome; should return True.
        - "abcd" is not a palindrome; should return False.
    """

    text_length = len(text)
    queue = []
    halfway = text_length // 2

    for c in text[:halfway]:
        queue.append(c)

    if text_length % 2 == 0:
        for c in text[halfway:]:
            if c != queue.pop():
                return False
    else:
        for c in text[halfway + 1:]:
            if c != queue.pop():
                return False
        
    return True