from xml.dom.minidom import ProcessingInstruction

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/Users/udaypandey/Desktop/Project /Student Data /student.csv")
print(df.head())

df.describe()

df.info()

df.isnull().sum()

## Drop unnamed column

df.drop("Unnamed: 0", axis = 1)

print(df.head())

df["WklyStudyHours"] = df["WklyStudyHours"].str.replace("05-Oct", "5-10")

df.head()

#Gender Distribution

plt.figure(figsize= (5,6))
ax = sns.countplot(data = df, x = "Gender")
ax.bar_label(ax.containers[0])
plt.title("Gender")
plt.show()

# From the above chart we have analyzed the number of females in the data is more than the number of males

gb = df.groupby("ParentEduc").agg({"MathScore": 'mean', "ReadingScore": "mean", "WritingScore": "mean"})
print(gb)

sns.heatmap(gb, annot = True)
plt.title("Relation b/w Parent Edu and Children Marks")
plt.show()

# From the chart we have understood that parents education have direct impact on their children scores.

gb1 = df.groupby("EthnicGroup").agg({"MathScore": 'mean', "ReadingScore": "mean", "WritingScore": "mean"})
print(gb1)

sns.heatmap(gb1, annot = True)
plt.title("Relationship b/w Ethnic group & Children Marks")
plt.show()

# From the chart we have understood that Ethnic Group have direct impact on children scores.

gb2 = df.groupby("ParentMaritalStatus").agg({"MathScore": 'mean', "ReadingScore": "mean", "WritingScore": "mean"})
print(gb2)

sns.heatmap(gb2, annot = True)
plt.title("Relation b/w Parent Matrital and Children Marks")
plt.show()

gb3 = df.groupby("WklyStudyHours").agg({"MathScore": 'mean', "ReadingScore": "mean", "WritingScore": "mean"})
print(gb3)

sns.heatmap(gb3, annot = True)
plt.title("Relation b/w StudyHours and Children Marks")
plt.show()

sns.boxplot(data= df, x = "ReadingScore")
plt.show()

print(df["EthnicGroup"].unique())

groupA = df.loc[(df['EthnicGroup'] == "group A")].count()
groupB = df.loc[(df['EthnicGroup'] == "group B")].count()
groupC = df.loc[(df['EthnicGroup'] == "group C")].count()
groupD = df.loc[(df['EthnicGroup'] == "group D")].count()
groupE = df.loc[(df['EthnicGroup'] == "group E")].count()

l = ["group A", "group B", "group C", "group D", "group E"]
mlist = [groupA["EthnicGroup"], groupB["EthnicGroup"], groupC["EthnicGroup"], groupD["EthnicGroup"]], groupE["EthnicGroup"]
print(mlist)

ax = sns.countplot(data =df, x = 'EthnicGroup')
ax.bar_label(ax.containers[0])