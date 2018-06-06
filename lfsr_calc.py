""" 
	author : ndale
	date : 10/28/2017

	LFSR calculator for paper1, exercise 3, AYD 621

	Calculates output of x^10 + x^7 + 1 polynomal
	using python lists	
"""

def shift(current_list):
	""" A new value is inserted on the left side of the list (value_to_add)
		and the most right value is the bit_out that is returning to the caller
		function alongside the new list. value_to_add is the xor operation between
		x^10 and x^3.
		This function is executed on every run and returns to the caller the new list, 
		which is the initial value for the next run and the outstrem bit
	"""
	value_to_add = current_list[6] ^ current_list[9]
	current_list.insert(0, value_to_add)
	bit_out = current_list.pop()
	return current_list, bit_out

def calc_output_stream(current_list, runs=1023):
	""" The default number of runs is 1023 because of the grade of polynomal. 
	L=10, so the period of the output stream is 2^10 - 1 = 1023.
	On every run a shift() operation is performed on the list
	and the result is inserted in the list. In order to handle the output bit 
	in an efficient way, every bit_out value is inserted in a new list 
	called output stream. The list is printed on screen and in a file named "out.txt" 
	"""
	output_stream=[]
	for i in range(runs):						
		current_list, feedback = shift(current_list)
		print("run : %d output bit %d" % (i, feedback))
		output_stream.append(feedback)	
	#print(output_stream)
	print("".join(str(x) for x in output_stream))
	create_output_stream_file("out.txt", output_stream)

def create_output_stream_file(filename, out_stream):
	with open(filename, 'w') as out:		
		out.write("".join(str(x) for x in out_stream))

if __name__=="__main__":	
	#init_state=[0,0,1,1,1,1,1,1,0,1]
	#init_state=[1,0,1,1,1,1,1,1,0,0]
	init_state=[1,1,1,1,1,1,1,1,1,1]
	#init_state = [0,0,0,0,0,0,0,0,0,1]
	calc_output_stream(init_state, 128) 	
	#calc_output_stream(init_state, 2046)
	#calc_output_stream(init_state)

