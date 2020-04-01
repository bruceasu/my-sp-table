# coding: utf-8

f1 = open("a.txt")
f2 = open("b.txt")
f3 = open("c.txt", "w")

m = {}
for line in f1:
	line = line.strip().decode("utf-8")
	if line == "" or line[0] == u"#":
		continue
	if line in m:
		m[line] += 1
	else:
		m[line] = 1
f1.close()

n = {}
for line in f2:
	line = line.strip().decode("utf-8")
	if line == "" or line[0] == u"#":
		continue
	kv = line.split("\t")
	w = kv[0]
	c = kv[1]

	if c not in m:
		if c in n:
			if n[c] == 1:
				n[c] += 1
				print >> f3, line.encode("utf-8")
			else:
				pass # 不要这个词
		else:
			n[c] = 1
			print >> f3, line.encode("utf-8")
	else:
		if m[c] == 1:
			if c not in n:
				n[c] = 1
				print >> f3, line.encode("utf-8")
			else:
				pass # 不要这个词
		else:
			pass # 不要这个词
f2.close()

f3.close
print "done!"
