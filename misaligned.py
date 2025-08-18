
def get_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map.append((get_pair_number(i, j), major, minor))
    return color_map

def get_pair_number(majorIndex, minorIndex):
    return majorIndex * 5 + minorIndex

def print_color_map():
    color_map = get_color_map()
    for i in color_map:
        print(i)
    return len(color_map)

result = print_color_map()
assert(result == 25)
assert(get_pair_number(0,0) == 1)
print("All is well (maybe!)")
