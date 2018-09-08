#import library
from sklearn import tree
#selecting decision tree machine learning model
classifier=tree.DecisionTreeClassifier()
#Dataset
#Height,Weight,Shoe size
x=[[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
[177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]
#gender
y=['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
'female', 'male', 'male']
#training Model
classifier=classifier.fit(x,y)
#predicting result
prediction=classifier.predict([[177,79,45]])
#print predictions
print(prediction)