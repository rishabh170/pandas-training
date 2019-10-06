# df.groupby('Gender')[['Survived']].aggregate(lambda x: x.sum() / len(x))
df.groupby('Gender')[['Survived']].mean()