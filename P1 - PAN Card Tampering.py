import cv2
from PIL import Image,ImageOps
import numpy as np
from skimage.metrics import structural_similarity as ssim

original = Image.open('/Users/sawantalwar/Downloads/Pan Card Tampering Flask App/sample_data/original.jpg')
tampered = Image.open('/Users/sawantalwar/Downloads/Pan Card Tampering Flask App/sample_data/tampered.jpg')

get_ipython().system("mkdir '/Users/sawantalwar/Downloads/Pan Card Tampering Flask App/new_data'")

original2 = original.resize((250,160))
tampered2 = tampered.resize((250,160))

original2.save('/Users/sawantalwar/Downloads/Pan Card Tampering Flask App/new_data/original.jpg')
tampered2.save('/Users/sawantalwar/Downloads/Pan Card Tampering Flask App/new_data/tampered.jpg')

original2.size,original2.format

original2 = cv2.imread('/Users/sawantalwar/Downloads/Pan Card Tampering Flask App/new_data/original.jpg')
tampered2 = cv2.imread('/Users/sawantalwar/Downloads/Pan Card Tampering Flask App/new_data/tampered.jpg')


original3 = cv2.cvtColor(original2,cv2.COLOR_BGR2GRAY)
tampered3 = cv2.cvtColor(tampered2,cv2.COLOR_BGR2GRAY)


score,diff = ssim(original3,tampered3,full=True)
diff = (diff * 255).astype('uint8')
print(score)
