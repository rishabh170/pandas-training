c = cast
c = c[c.name == 'Mohanlal']
g = c.groupby(['year', 'title']).size()
g[g > 1]