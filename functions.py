
#this is a different method 

from PIL import Image
import functions		

def encode(hexcode, digit):
	if True:
		hexcode = hexcode[:-1] + digit		
		return hexcode
	else:
		return None

def decode(hexcode):
	if hexcode[-1] in ('0', '1'):
		return hexcode[-1]
	else:
		return None

def hide(filename, message):
	img = Image.open(filename) # Meh
	binary = functions.str2bin(message) + '1111111111111110' #marking end of message
	img = img.convert('RGBA')
	if img.mode in ('RGBA'):					   

		data = img.getdata()					   

		newData = []							   

		digit = 0
		temp = ''
		for item in data:
			if (digit < len(binary)):
				newpix = encode(functions.rgb2hex(item[0],item[1],item[2]),binary[digit])  
																				 
				r, g, b = functions.hex2rgb(newpix)
				newData.append((r,g,b,255))
				digit += 1
			else:
				newData.append(item)

		img.putdata(newData)						
		img.save(filename, "PNG")
		return True

	return False
def retr(filename):
	img = Image.open(filename)
	binary = ''

	img = img.convert('RGBA')
	if img.mode in ('RGBA'):			
		data = img.getdata()

		for item in data:
			hidden_digit = decode(functions.rgb2hex(item[0],item[1],item[2]))
			if hidden_digit == None:
				pass
			else:
				binary = binary + hidden_digit
				if (binary[-16:] == '1111111111111110'):
					return functions.bin2str(binary[:-16])

		return functions.bin2str(binary)

	else:
		return "works!."

if __name__ == '__main__':
	fh = open('text.txt', 'r')
	s = fh.read()
	hide_check = hide('.png', s)
	s = retr('stegno.png')

	
