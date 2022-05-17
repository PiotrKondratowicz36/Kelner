import pandas
from sklearn.tree import DecisionTreeClassifier


class Decision_Tree:
    dataset = pandas.read_csv("tests.csv")
    print(dataset)

    d = {'F': 1, 'M': 2}
    dataset['Sex'] = dataset['Sex'].map(d)
    d = {'NO': 0, 'YES': 1}
    dataset['Vegetarian'] = dataset['Vegetarian'].map(d)
    d = {'LOW': 1, 'AVERAGE': 2, 'HIGH': 3}
    dataset['Budget'] = dataset['Budget'].map(d)
    d = {'MAIN': 1, 'DESSERT': 2}
    dataset['Type'] = dataset['Type'].map(d)
    d = {'COLD': 1, 'HOT': 2}
    dataset['Temperature'] = dataset['Temperature'].map(d)
    d = {'LIGHT': 1, 'HEAVY': 2}
    dataset['Weight'] = dataset['Weight'].map(d)
    d = {'SOUP': 1, 'SCALLOPS': 2, 'CHICKEN': 3, 'PORKCHOP': 4,
         'RISOTTO': 5, 'DUCK': 6, 'STEAK': 7, 'RATATOUILLE': 8,
         'ICECREAM': 9, 'PAVLOVA': 10, 'PANNACOTTA': 11, 'SOUFFLE': 12}
    dataset['Dish'] = dataset['Dish'].map(d)

    features = ['Age', 'Sex', 'Vegetarian', 'Budget', 'Type', 'Temperature', 'Weight']

    X = dataset[features]
    y = dataset['Dish']

    decision_tree = DecisionTreeClassifier()
    decision_tree = decision_tree.fit(X.values, y)

    # export tree.dot
    # data = tree.export_graphviz(decision_tree, out_file='tree.dot', feature_names=features)

    # legend
    # age
    # sex          1 - Female,     2 - Male
    # vegetarian   0 - No,         1 - Yes
    # budget       1 - Low,        2 - Average,      3 - High
    # type         1 - Main,       2 - Dessert
    # temperature  1 - Cold,       2 - Hot
    # weight       1 - Light,      2 - Heavy
    # dish         1 - Soup,       2 - Scallops,     3 - Chicken,
    #              4 - Pork chop,  5 - Risotto,      6 - Duck,
    #              7 - Steak,      8 - Ratatouille,  9 - Ice Cream,
    #              10 - Pavlova,   11 - Panna Cotta  12 - Souffle

    print('Selected dish: ')
    print(decision_tree.predict([[23, 1, 1, 2, 1, 2, 1]]))
