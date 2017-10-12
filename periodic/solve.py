N = int(input())

elements = ['h','he','li','be','b','c','n','o','f','ne','na','mg','al','si','p','s','cl','ar','k','ca','sc','ti','v','cr','mn','fe','co','ni','cu','zn','ga','ge','as','se','br','kr','rb','sr','y','zr','nb','mo','tc','ru','rh','pd','ag','cd','in','sn','sb','te','i','xe','cs','ba','la','ce','pr','nd','pm','sm','eu','gd','tb','dy','ho','er','tm','yb','lu','hf','ta','w','re','os','ir','pt','au','hg','tl','pb','bi','po','at','rn','fr','ra','ac','th','pa','u','np','pu','am','cm','bk','cf','es','fm','md','no','lr','rf','db','sg','bh','hs','mt','ds','rg','cn','nh','fl','mc','lv','ts','og']

def recurse_singles(index, singles, doubles):
	if index >= len(singles):
		return 0
	if not singles[index][1]:
		return 0
	if index == len(singles) - 1:
		return 1
	if singles[index][2] != -1:
		return singles[index][2]
	s_singles = recurse_singles(index + 1, singles, doubles)
	s_doubles = recurse_doubles(index + 1, singles, doubles)
	singles[index][2] = s_singles + s_doubles;
	return singles[index][2]

def recurse_doubles(index, singles, doubles):
	if index >= len(doubles):
		return 0
	if not doubles[index][1]:
		return 0
	if index == len(doubles) - 1:
		return 1
	if doubles[index][2] != -1:
		return doubles[index][2]
	d_singles = recurse_singles(index + 2, singles, doubles)
	d_doubles = recurse_doubles(index + 2, singles, doubles)
	doubles[index][2] = d_singles + d_doubles;
	return doubles[index][2]

for x in range(N):
	word = input()
	singles = list(word)
	doubles = [None] * (len(singles) - 1)
	for y in range(len(doubles)):
		doubles[y] = singles[y] + singles[y+1]
	singles = list(map(lambda x: [x, x in elements, -1], singles))
	doubles = list(map(lambda x: [x, x in elements, -1], doubles))
	print(str((recurse_singles(0, singles, doubles) + recurse_doubles(0, singles, doubles)) % 100000007))

