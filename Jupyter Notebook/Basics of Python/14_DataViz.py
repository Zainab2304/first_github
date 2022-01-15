#steps  involves in data visulaization 
# SEt 1: import libraries 
# import seaborn as sns
# import matplotlib.pyplot as plt

#Set 2 : set a theme 
# sns.set_theme(style="ticks", color_codes= True)

#Set 3: import data set also you can import your own data
# kashti= sns.load_dataset("titanic")
# print(kashti)

#step 4: plot basic graph with one variable 
# p= sns.countplot(x="sex", data = kashti)
# plt.show()


#step 5: plot graph with two variable 
# p= sns.countplot(x="sex", data = kashti, hue= "class")#hue means colour 
# plt.show()

#step 6: plot graph with two variable (countplot) with tiltes
# p= sns.countplot(x="sex", data = kashti, hue= "class")#hue means colour and  Class is one of thecoloumn name in data 
# p.set_title("PLot for basic counting with Baba Aammar")
# plt.show()

import seaborn as sns
import matplotlib.pyplot as plt 
sns.set_theme(style="ticks", color_codes= True) #sns.set_theme(style="ticks", color_codes= True)
titanic= sns.load_dataset("titanic")
graph= sns.countplot(x="sex", data=titanic , hue="class")
graph.set_title("ye ha mera graph")
plt.show()
