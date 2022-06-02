# Problem
# Given: A string s of length at most 200 letters and four integers a, b, c and d.

# Return: The slice of this string from indices a through b and c through d (with space in between),
# inclusively. In other words, we should include elements s[b] and s[d] in our slice.


def slice_string(string_input, a, b, c, d):
    a_b = string_input[a: b + 1]
    c_d = string_input[c: d + 1]
    return a_b + " " + c_d


print(slice_string(
    "XC9IEKaB2qrFovFPCs4SR2Y5NgwOSiODhRipariaVKZx7wOVfVnwJkDHhVxaj50G7Gcn7hOx9PLY5xkQOQanSDNI8XUjrbT6c24BlaeviskPsyTt1p05gk5JwbulC0W1Dq9tgFBbKFV8N4kx2IpsNykMAzERBgw82sATB1AcvsINIG1HC0RzfF.",
        33, 39, 100, 105))
