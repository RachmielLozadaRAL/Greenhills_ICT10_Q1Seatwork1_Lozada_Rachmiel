# Seatwork 1
from pyscript import display, document

string_sample = 'Rachmiel'
integer_sample = 15
float_sample = 162.56
list_sample = ['Japan', 'South Korea', 'Vietnam']
boolean_sample = True
dict_sample = {'color': 'black', 'carBrand': 'Honda', 'shoeSize': '10', 'bestFriend': 'SomePointZero'}
set_sample = {'apple', 'strawberry', 'banana', 'mango', 'watermelon'}
tuple_sample = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

display(type(string_sample), target='output')
display(type(integer_sample), target='output')
display(type(float_sample), target='output')
display(type(boolean_sample), target='output')
display(type(list_sample), target='output')
display(type(tuple_sample), target='output')
display(type(set_sample), target='output')
display(type(dict_sample), target='output')

# display(f"Hello! I am {string_sample} which as of now I am currently {integer_sample} years old and I am {float_sample} cm tall. The countries that I wanna go to are {list_sample}. it is {boolean_sample} that I am a student. I have loved the color {dict_sample['color']}, I drive a {dict_sample['carBrand']}, my shoe size is {dict_sample['shoeSize']}, and my best friend is {dict_sample['bestFriend']}. Days of the week are {tuple_sample}. And lastly, the fruits that I like are {set_sample}.", target='output')

document.getElementById('output').innerHTML = (
	f"Hello! I am {string_sample} which as of now I am currently {integer_sample} years old and I am {float_sample} cm tall. "
	f"The countries that I wanna go to are {list_sample}. It is {boolean_sample} that I am a student. "
	f"I loved the color {dict_sample['color']}, I drive a {dict_sample['carBrand']}, my shoe size is {dict_sample['shoeSize']}, "
	f"and my best friend is {dict_sample['bestFriend']}. Days of the week are {tuple_sample}. "
	f"And lastly, the fruits that I like are {set_sample}."
)