tri_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))

x = (tri_char + ' ')
for i in range(triangle_height +1):
    print(x*i)