
def get_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map.append((get_pair_number(i, j), major, minor))
    return color_map

def get_pair_number(majorIndex, minorIndex):
    return majorIndex * 5 + minorIndex + 1

def format_color_map_entry(entry):
    """Format a single row with proper alignment."""
    number, major, minor = entry
    return f"{number:<3} | {major:<6} | {minor:<6}"

def print_color_map():
    color_map = get_color_map()
    for i in color_map:
        print(format_color_map_entry(i))

print_color_map()

result = get_color_map()
assert(len(result) == 25)

assert(get_pair_number(0,0) == 1)
assert(get_pair_number(4,4) == 25)

assert(format_color_map_entry((1, 'White', 'Blue')) == "1   | White  | Blue  ")
assert(format_color_map_entry((12, "Red", "Green")) == "12  | Red    | Green ")

print("All is well (maybe!)")
