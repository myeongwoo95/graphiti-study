from langchain_core.tools import tool


# 1. 덧셈 툴
@tool
def add_numbers(a: int, b: int) -> int:
    """두 숫자를 더합니다.
    
    Args:
        a: 첫 번째 숫자
        b: 두 번째 숫자
    
    Returns:
        두 숫자의 합
    """
    result = a + b
    print(f"[툴 호출] add_numbers({a}, {b}) = {result}")
    return result


# 2. 곱셈 툴
@tool
def multiply_numbers(a: int, b: int) -> int:
    """두 숫자를 곱합니다.
    
    Args:
        a: 첫 번째 숫자
        b: 두 번째 숫자
    
    Returns:
        두 숫자의 곱
    """
    result = a * b
    print(f"[툴 호출] multiply_numbers({a}, {b}) = {result}")
    return result


# 3. 문자열 길이 확인 툴
@tool
def get_string_length(text: str) -> int:
    """문자열의 길이를 반환합니다.
    
    Args:
        text: 길이를 확인할 문자열
    
    Returns:
        문자열의 길이
    """
    length = len(text)
    print(f"[툴 호출] get_string_length('{text}') = {length}")
    return length
