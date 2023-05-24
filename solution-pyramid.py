
# build pyramid 

def build_normal_pyramid(width, sym='H'):

    storage_normal = []

    # iterator
    a = 1
    
    if 50 > width > 0:
        if width % 2 != 0:
            for x in range(1, width + 1):
                num_sym = sym*a
                spaces = int(width - x)
                row  = ' ' * spaces + num_sym + ' ' * spaces
                storage_normal.append(row)
                a += 2
            
            return storage_normal

        return None


def build_flipped_pyramid(width, sym='H'):
    
    storage_flipped = []
    
    # iterator
    a = width
    if 50 > width > 0:
        if width % 2 != 0:
            while a != 0:
                num_sym = sym*a
                l = int((width - a) / 2)
                row = ' ' * l + num_sym + l * ' '
                storage_flipped.append(row)
                a -= 2

                if a < 0:
                    print(f'\nBuilding infinite pyramids is bad, but listening to gta vice city comercials is good https://www.youtube.com/watch?v=iflwZTNcb4E\n')
                    break

    return storage_flipped


x = build_flipped_pyramid(47)
for i in x:
    print(i)