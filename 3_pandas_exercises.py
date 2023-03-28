# Görev 1: Seaborn kütüphanesi içerisinden Titanicveri setini tanımlayınız

import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()

# Görev 2: Titanic verisetindeki kadın ve erkek yolcuların  sayısını bulunuz

df["sex"].value_counts()

print("########################### Shape ###########################")
print(dataframe.shape)
print("########################### Types  ###########################")
print(dataframe.dtypes)
print("########################### Head  ###########################")
print(dataframe.head(head))
print("########################### Tail  ###########################")
print(dataframe.tail(head))
print("########################### NA  ###########################")
print(dataframe.isnull().sum())
print("########################### Quintiles  ###########################")
print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz

print(df.nunique())

# Görev 4: pclass değişkenin inunique değerlerinin sayısını bulunuz

print(df["pclass"].nunique())


# Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz

print(df["pclass"] & df["parch"].nunique())

# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz

df["embarked"].dtype
df["embarked"] = df["embarked"].astype("category")

# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz

df[df["embarked"] == "C"].value_counts()

# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.

df[df["embarked"] != "S"].value_counts()

# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz

df[(df["age"] < 30) & (df["sex"] == "female")].head()

# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz

df[(df["fare"] > 500) | (df["age"] > 70)].value_counts()

# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz

df.isnull().sum()

# Görev 12:  who değişkenini dataframe’den çıkarınız.

df.drop(columns="who", axis=1, inplace=True)
df.head()

# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.

