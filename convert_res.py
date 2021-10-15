from PIL import Image
import os

try:
    os.makedirs('low_res')
except OSError as e:
    print('low_res folder already exists')

file_names = os.listdir('high_res')

for i in range(len(file_names)):
	file_path = 'high_res/'+file_names[i]
	img = Image.open(file_path)
	basewidth = 800

	wpercent = (basewidth / float(img.size[0]))
	hsize = int((float(img.size[1]) * float(wpercent)))
	img = img.resize((basewidth, hsize), Image.ANTIALIAS)
	img.save('low_res/{}'.format(file_names[i]))

