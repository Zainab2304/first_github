import pandas as pd 

chilla= pd.read_csv("chilla_data.csv")
# print(chilla)

import seaborn as sns 
import matplotlib.pyplot as plt

# sns.set_theme (style= "ticks", color_codes= True )

p= sns.countplot(x="Gender", hue= "Age" , data= chilla)
p.set_title("Ye rha humamra pehla khud se bna graph")
plt.show()
