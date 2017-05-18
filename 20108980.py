tb, ch, re, qu = [], [], [], []

def dfs(cv):
        for i in range(len(tb[cv])):
                if tb[cv][i] == True and ch[i] == False:
                        re.append(i+1)
                        ch[i] = True
                        dfs(i)

def bfs(sv):
        qu.insert(0, sv)

        while len(qu) != 0:
                cv = qu.pop()

                if ch[cv] == False:
                        re.append(cv+1)
                        ch[cv] = True

                for i in range(len(tb[cv])):
                        if tb[cv][i] == True and ch[i] == False:
                                qu.insert(0, i)

v, e, sv = map(int, input().split())
tb = [[False for i in range(v)] for j in range(v)]
ch = [False for i in range(v)]
ch[sv-1] = True

for i in range(e):
        fr, to = map(int, input().split())
        tb[fr-1][to-1] = True
        tb[to-1][fr-1] = True

re.append(sv)
dfs(sv-1)
print(' '.join(map(str, re)))

ch = [False for i in range(v)]
re = []

bfs(sv-1)
print(' '.join(map(str, re)))
