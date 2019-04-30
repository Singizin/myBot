from PIL import Image
import copy

def user_mask(image,w,h):
    user_mask = Image.new('1', (w, h), 'black')
    im = image.load()
    um = user_mask.load()
    for i in range(w):
        for j in range(h):
            r, g, b = im[i, j]
            if r>250and g>250 and b>250:
                um[i, j] = 1
            else:
                um[i, j] = 0
    user_mask.show()
    return user_mask