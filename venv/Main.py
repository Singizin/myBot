

image = Image.open('files/photos/1.jpg')
grey_dot=150
direction = 3
w,h = image.size
print('Размер фото: гориз. {} пх * верт. {} пх'.format(w,h))
contrast_image = contrast(image,w,h,grey_dot)
contrast_clear = contrast_better(contrast_image,w,h,2)
#mask = edge(contrast_clear,w,h)
#print(image.size, mask.size)
result = pixel_sort(image,contrast_clear,w,h,direction)
result.show()