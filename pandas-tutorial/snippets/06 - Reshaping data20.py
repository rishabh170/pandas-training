df.pivot_table(index='Pclass', columns='Gender', 
               values='Survived', aggfunc='mean')