import pandas
data = pandas.read_csv('../titanic.csv', index_col='PassengerId')

#Task 1
sex_counts = data['Sex'].value_counts()

with open("answers/task1.txt", "w") as text_file:
    text_file.write("%s %s" % (sex_counts['male'], sex_counts['female']))

#Task 2
alive_count = data['Survived'].value_counts()

alive_percentage = float(alive_count[1]) / alive_count.sum() * 100

with open("answers/task2.txt", "w") as text_file:
    text_file.write("%.2f" % (alive_percentage))

#Task 3
counts = data['Pclass'].value_counts()
allp = counts.sum()
fpercentage = float(counts[1]) / allp * 100
with open("answers/task3.txt", "w") as text_file:
    text_file.write("%.2f" % (fpercentage))

#Task 4
mean_age = data['Age'].mean()
median_age = data['Age'].median()
with open("answers/task4.txt", "w") as text_file:
    text_file.write("%.2f %.2f" % (mean_age, median_age))

#Task 5
pair_wise = data.corr()
correlation = pair_wise['Parch']['SibSp']
with open("answers/task5.txt", "w") as text_file:
    text_file.write("%.2f" % (correlation))

#Task 6
clean_names = []
names = list(data['Name'][data['Sex'] == 'female'])
for name in names:
	if '(' in name:
		name = name.split('(')[1].split(' ')[0]
	elif 'Miss.' in name:
		name = name.split('Miss. ')[1].split(' ')[0]
	else:
		print name
	clean_names.append(name)

print clean_names
names_data = pandas.DataFrame.from_items([('Name', clean_names)]).Name.value_counts()
print names_data(0, axis=1)
#with open("answers/task5.txt", "w") as text_file:
#    text_file.write("%.2f" % (correlation))