

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
    
    storage_fliped = []

    #iterator
    a = width
    
    if 50 > width > 0:
        if width % 2 != 0:
            for x in reversed(range(1, width + 1)):
                
                num_sym = sym*a
                spaces = int(width - x)
                row = spaces* ' ' + num_sym + spaces* ' '
                storage_fliped.append(row)
                a -= 2
                
            return storage_fliped
        
        return None

n = build_normal_pyramid(13)
m = build_flipped_pyramid(9)
 
