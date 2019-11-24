c = cast
c = c[c.name == 'Govinda']
g = c.groupby(['character']).size()
g[g > 1].sort_values(ascending = False)