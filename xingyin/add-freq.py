# coding: utf-8

f1 = open("c.txt")
f2 = open("d.txt", "w")
cnt = 40000
m = {}
for line in f1:
	line = line.strip().decode("utf-8")
	if line == "" or line[0] == u"#":
		print >> f2, line.encode("utf-8")
		continue
	print >> f2, (u"%s#序%s" % (line, cnt)).encode("utf-8")
	if cnt > 30000:
		cnt -= 1
f1.close()

for (k, vs) in m.iteritems():
	x = 3
	if len(vs) < 3:
		x = len(vs)
	for i in xrange(0, x):
		print >> f2, (u"%s\t%s" % (vs[i], k)).encode("utf-8")
f2.close()

print "done!"
