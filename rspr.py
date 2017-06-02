#Making a dictionary where each key is a node and the values for each key are [INV, OUTu, CURRENT_SCORE]
#CURRENT_SCORE is initialized to 1/6

INITIAL_SCORE = float(1/6)
prob = 0.8

all_nodes = {}

node_a = [['B'], ['B', 'F'], INITIAL_SCORE]
node_b = [['A'], ['A', 'C'], INITIAL_SCORE]
node_c = [['B', 'E'], ['D', 'E'], INITIAL_SCORE]
node_d = [['C', 'E'], ['E'], INITIAL_SCORE]
node_e = [['C', 'D'], ['C', 'D'], INITIAL_SCORE]
node_f = [['A'], [], INITIAL_SCORE]

all_nodes['A'] = node_a
all_nodes['B'] = node_b
all_nodes['C'] = node_c
all_nodes['D'] = node_d
all_nodes['E'] = node_e
all_nodes['F'] = node_f


#print(all_nodes)
new_scores = {} #This list is used to store the scores while the rest of the nodes are assessed.

threshold = 0.0001
break_loop = False
count = 0
while not break_loop: 

	for node in all_nodes:
		#print(node)
		values = all_nodes[node]

		current_sum = 0
		for inv in values[0]: #calculating the summation expression for each term u in inv
			score_u = all_nodes[inv][2] #getting the score of term u
			out_u = len(all_nodes[inv][1]) #Getting the size of the set of pages u links to
			quotient = float(score_u / out_u) 
			current_sum += quotient

		total_score = (1-prob) + prob * current_sum

		new_scores[node] = total_score


	#updating values in all_nodes and checking the threshold. If the change for each node is less than the threshold the loop breaks.
	threshold_violation = False
	for node in new_scores:
		new_score = new_scores[node]
		old_score = all_nodes[node][2]
		if abs(old_score - new_score) > threshold:
			threshold_violation = True
		all_nodes[node][2] = new_score

	if not threshold_violation:
		break_loop = True

	#for k, v in all_nodes.items(): print(k, v)
	#print()
	if break_loop:
		break
	count += 1

print(count)

for k, v in all_nodes.items(): print(k, v[2])
