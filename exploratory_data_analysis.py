import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



df = pd.read_csv('Titanic-Dataset.csv')

print(df.shape)
print(df.columns)
print(df.info())
print(df.describe(include='all'))
print(df.isnull().sum())
print(df[['Age', 'Fare' , 'SibSp' , 'Parch']].median())

num_cols = ['Age', 'Fare', 'SibSp' , 'Parch']

for col in num_cols:
    plt.figure(figsize=(10,6))
    sns.histplot(df[col], kde=True, bins=20)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

for col in num_cols:
    plt.figure(figsize=(10,6))
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col}')
    plt.grid(True)
    plt.show()

corr_matrix = df[['Survived' , 'Age' , 'Parch' , 'SibSp' , 'Fare']].corr()

plt.figure(figsize=(10,6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

sns.pairplot(df[['Survived', 'Age', 'Fare', 'SibSp', 'Parch']], hue='Survived', corner=True)
plt.suptitle("Pairplot of Numerical Features by Survival", y=1.02)
plt.show()



sns.barplot(x='Sex', y='Survived', data=df)
plt.title('Survival Rate by Sex')
plt.show()


sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Survival Rate by Class')
plt.show()


sns.violinplot(x='Survived', y='Age', data=df)
plt.title('Age Distribution by Survival')
plt.show()


sns.boxplot(x='Survived', y='Fare', data=df)
plt.title('Fare Distribution by Survival')
plt.show()


grouped = df.groupby(['Pclass', 'Sex'])['Survived'].mean().unstack()
print("\n--- Survival Rate by Class and Sex ---")
print(grouped)


grouped.plot(kind='bar', stacked=True)
plt.title('Survival Rate by Class and Gender')
plt.ylabel('Survival Rate')
plt.show()

