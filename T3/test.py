import cv2
import pickle

img = cv2.imread('./img/low_fi.jpg')

# print(img)    

img_serialized = pickle.dumps(img)

# print(img_serialized)

img_deserialized = pickle.loads(img_serialized)

print(img_deserialized)
