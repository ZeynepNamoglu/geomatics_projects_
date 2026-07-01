decimal_degree = float(input("Please enter the decimal degree you want to convert: "))
coord_type = input("Is this coordinate Latitude(lat) or Longtitude(lon)?:").strip().lower()

def convert_to_degree(decimal, coordinate_type):
    if coordinate_type == "lat":
        direction = "Nort" if decimal >= 0 else "South"
    elif coordinate_type == "lon":
        direction = "East" if decimal >= 0 else "West"
    else:
        direction = "" 


    abs_decimal = abs(decimal)


    degree = int(abs_decimal)

    remainder = abs_decimal - degree

    minute_float = remainder * 60
    minute = int(minute_float)

    second_remainder = minute_float - minute

    second = second_remainder * 60

    return direction, degree, minute, round(second,2)


test_dir, test_deg, test_min, test_sec = convert_to_degree(decimal_degree, coord_type)

print(f"\nDecimal degree: {decimal_degree}")
print(f"\nDMS Format: {test_deg} degrees {test_min} minutes {test_sec} seconds {test_dir}")
