def roman_to_integer(roman_numeral):
    roman_numeral = roman_numeral.upper()
    value_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    last_value = 0

    for element in roman_numeral:
        current_value = value_map[element]
        if current_value > last_value and last_value != 0:
            total -= last_value
        else:
            total += current_value
        last_value = current_value

    return total

roman_numeral = input("Roman numeral: ")
integer_value = roman_to_integer(roman_numeral)

print(f"{roman_numeral} -> {integer_value}")