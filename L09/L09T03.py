# lukujen käsittely ja tulostetaminen tilanteissa, joissa annettu oikea tai väärä luku tai jotain muuta 
from typing import Any

def is_this_zero(num: Any) -> bool:
    if isinstance(num, (int, float)):
        return num == 0
    else:
        raise TypeError("Input must be a number.")

def safe_is_this_zero(num: Any) -> tuple[bool, str | None]:
    try:
        result = is_this_zero(num)
        return (result, None)
    except TypeError:
        return (False, "Input must be a number.")

def verify_is_this_zero(test_cases: list[Any]) -> list[tuple[Any, tuple[bool, str | None]]]:
    results = []
    for case in test_cases:
        result = safe_is_this_zero(case)
        results.append((case, result))
    return results

def main():
    test_cases = [0, 5, "5", None]
    test_results = verify_is_this_zero(test_cases)
    for input_value, (result, error_message) in test_results:
        if isinstance(input_value, str):
            formatted_input = f'"{input_value}"'
        else:
            formatted_input = str(input_value)

        if error_message:
            print(f"Input: {formatted_input}, Result: Error - {error_message}")
        else:
            print(f"Input: {formatted_input}, Result: {result}")

if __name__ == "__main__":
    main()
