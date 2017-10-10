class Tree(object):
	def __init__(self):
		self.left = None
		self.right = None
		self.dim = None
		self.val = None
		self.parent = None

def build_kd_tree(vecs, dim, d):
	if(len(vecs) == 0):
		return None
	if(len(vecs) == 1):
		ret = Tree()
		ret.val = vecs[0]
		return ret
	vals = sorted(vecs, key=lambda v: v[dim])
	mid = int(len(vals)/2)
	tree = Tree()
	tree.val = vals[mid]
	tree.dim = dim
	#print("The value for this node is", str(tree.val))
	#print("%%%%%")
	#print(str(mid))
	#print("%")
	#print(str(vals))
	#print("%")
	#print(str(vals[:mid]))
	#print("%")
	#print(str(vals[mid+1:]))
	#print("%%%%%")
	tree.left = build_kd_tree(vals[:mid], (dim+1)%d, d)
	if(tree.left != None):
		tree.left.parent = tree
	tree.right = build_kd_tree(vals[mid+1:], (dim+1)%d, d)
	if(tree.right != None):
		tree.right.parent = tree
	return tree

def print_tree_in_order(tree):
	print("ROOT")
	print(tree.val)
	if(tree.left != None):
		print("LEFT")
		print_tree_in_order(tree.left)
	if(tree.right != None):
		print("RIGHT")
		print_tree_in_order(tree.right)
	

def dist_squared_3(A, B):
	return (A[0] - B[0])**2 + (A[1] - B[1])**2 + (A[2] - B[2])**2

(N, K) = list(map(int, input().split(' ')))
ns = [(0,0,0)] * N
for x in range(N):
	ns[x] = tuple(map(int, input().split(',')))

tree = build_kd_tree(ns, 0, 3)

#print("VALL")
#print(str(tree.left.left.val))
#print(str(tree.right.left.val))

#print("##########")
#print_tree_in_order(tree)
#print("##########")

ks = [(0,0,0)] * K
for x in range(K):
	ks[x] = tuple(map(int, input().split(',')))

def find_nearest_neighbor(root, color, top):
	# We go down the tree to find the nearest leaf node
	while(root.left != None or root.right != None):
		#print("LOOP&&&")
		#print(str(color[root.dim]) + " < " + str(root.val[root.dim]) + "?")
		if(color[root.dim] < root.val[root.dim] and root.left != None):
			root = root.left
			continue
		elif(color[root.dim] >= root.val[root.dim] and root.right != None):
			root = root.right
			continue
		# We MUST traverse to leaf node, even if it doesn't fit with binary search
		if(root.left != None):
			root = root.left
			continue
		elif(root.right != None):
			root = root.right
			continue
		break
	#print("after looping we are on node " + str(root.val))
	# We set our best guess to this leaf node
	best_guess = root.val
	guess_dist = dist_squared_3(root.val, color)
	while(root != top):
		#print("while iter")
		prev = root;
		root = root.parent
		dist = dist_squared_3(root.val, color)
		if(dist <= guess_dist):
			#print("setting best guess to " + str(root.val))
			guess_dist = dist
			best_guess = root.val
		# If the sphere intersects with the cube of the other half of
		# the tree we must recurse down it.
		if(dist > (root.val[root.dim] - color[root.dim])**2):
			#print("intersection")
			other = root
			if(root.left == prev):
				other = root.right
			elif(root.right == prev):
				other = root.left
			if(other != None):
				#print("entering recurse guess with top " + str(other.val))
				recurse_guess = find_nearest_neighbor(other, color, other)
				#print("recurse guess was " + str(recurse_guess))
				recurse_guess_dist = dist_squared_3(recurse_guess, color)
				if(recurse_guess_dist <= guess_dist):
					guess_dist = recurse_guess_dist
					best_guess = recurse_guess
					#print("setting recurse guess to best")
	#print("best guess 1 was " + str(best_guess))
	dist_top = dist_squared_3(top.val, color)
	if(dist_top <= guess_dist):
		#print("resetting with top")
		best_guess = top.val
		guess_dist = dist_top
	#print("best guess was " + str(best_guess))
	return best_guess

for x in range(K):
	color = ks[x]
	nn = find_nearest_neighbor(tree, color, tree)	
	print(nn)

