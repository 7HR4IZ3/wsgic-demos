from xml.etree.ElementTree import Element, tostring
from xml.dom.minidom import parseString

def dict_to_xml(data, root=None):

	if not root:
		root = Element("root")
	elif isinstance(root, str):
		root = Element(root)
	
	assert isinstance(root, Element)

	def main(data, root):
		for key in data:
			value = data[key]

			element = Element(key)
			if isinstance(value, dict):
				val = main(value, element)
			elif isinstance(value, (list, tuple, set)):
				val = main({"item": x for x in value}, element)
			else:
				val = str(value)
			
			element.text = val
			root.append(element)
		return tostring(root).decode("utf-8")

	return parseString(main(data, root).replace("&lt;", "<").replace("&gt;", ">")).toprettyxml()

data = {
	"name": "Thraize",
	"age": 9,
	"likes": {
		"coding": 90,
		"games": 70,
		"anime": {
			"naruto": 89,
			"dbz": 70,
			"bleach": 90
		}
	}
}
ret = dict_to_xml(data)
print(ret)
