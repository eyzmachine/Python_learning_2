from xml.etree import ElementTree as et

def cube_parser():
	input_xml = input()
	root = et.fromstring(input_xml)
	price = 1
	color_dict = dict({'red': 0, 'green': 0, 'blue': 0})
	
	def price_count(current_price, element):
		nonlocal color_dict
		color_dict[element.attrib['color']] += current_price
		for child in element:
			price_count(current_price + 1, child)
	
	price_count(price, root)
	print(f'{color_dict["red"]} {color_dict["green"]} {color_dict["blue"]}')
	
cube_parser()