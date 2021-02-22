from PIL import Image
import numpy as np

im_frame = Image.open("images/SegmentationExample" + '.png')
np_frame = np.array(im_frame)

print(np_frame.shape)

merged_array = (np.append(np_frame, np_frame, axis=2))
print(merged_array.shape)

im = Image.fromarray(np_frame)
im.save("your_file.tiff")


# a = np.asarray([[[1,2], [1,2]],[[1,2], [1,2]]])
# print(a.shape)
# print(a)
# b = np.asarray([[[1,2], [1,2]],[[1,2], [1,2]]])


# arr_merged = np.append(a,b, axis=0)
# print(f'Merged 2x2 Arrays along Axis-2:\n{arr_merged}')

# print(arr_merged.shape)

# a = a.append()




# np_frame.(alpha)

# # Save as TIFF
# im.save('result.tif')