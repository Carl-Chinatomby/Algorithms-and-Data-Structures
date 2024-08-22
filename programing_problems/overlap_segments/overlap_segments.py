
def merge_and_sort(segments):
	"""brute force solution that stores the intervals and condenses

	Not memory efficient.
	"""
	line_graph = []
	retval = {}

	# populate the array
	for segment in segments:
		if segment['start'] < segment['end']:
			continue

		if len(line_graph) < segment['end']:
			# we need dynamically change the size
			new_line_graph = [ None for x in len(segment['end'])]
			for index, value in enumerate(line_graph):
				new_line_graph[index] = value
				line_graph = new_line_graph

		for x in range(segement['start'], segment['end']):
			line_graph[x] = 1


	# create the response
	



	return retval


def merge_and_sort(segments):
	return {}
