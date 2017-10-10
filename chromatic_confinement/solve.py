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
	tree.left = build_kd_tree(vals[:mid], (dim+1)%d, d)
	if(tree.left != None):
		tree.left.parent = tree
	tree.right = build_kd_tree(vals[mid+1:], (dim+1)%d, d)
	if(tree.right != None):
		tree.right.parent = tree
	return tree


def dist_squared_3(A, B):
	return (A[0] - B[0])**2 + (A[1] - B[1])**2 + (A[2] - B[2])**2

(N, K) = list(map(int, input().split(' ')))
ns = [(0,0,0)] * N
for x in range(N):
	ns[x] = tuple(map(int, input().split(',')))

tree = build_kd_tree(ns, 0, 3)

ks = [(0,0,0)] * K
for x in range(K):
	ks[x] = tuple(map(int, input().split(',')))

def find_nearest_neighbor(root, color, top):
	# We go down the tree to find the nearest leaf node
	while(root.left != None or root.right != None):
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
	# We set our best guess to this leaf node
	best_guess = root.val
	guess_dist = dist_squared_3(root.val, color)
	while(root != top):
		prev = root;
		root = root.parent
		dist = dist_squared_3(root.val, color)
		if(dist <= guess_dist):
			guess_dist = dist
			best_guess = root.val
		# If the sphere intersects with the cube of the other half of
		# the tree we must recurse down it.
		if(guess_dist > (root.val[root.dim] - color[root.dim])**2):
			other = root
			if(root.left == prev):
				other = root.right
			elif(root.right == prev):
				other = root.left
			if(other != None):
				recurse_guess = find_nearest_neighbor(other, color, other)
				recurse_guess_dist = dist_squared_3(recurse_guess, color)
				if(recurse_guess_dist <= guess_dist):
					guess_dist = recurse_guess_dist
					best_guess = recurse_guess
	dist_top = dist_squared_3(top.val, color)
	if(dist_top <= guess_dist):
		best_guess = top.val
		guess_dist = dist_top
	return best_guess

for x in range(K):
	color = ks[x]
	nn = find_nearest_neighbor(tree, color, tree)	
	print(nn)
