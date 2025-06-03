from sklearn.linear_model import Ridge
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import csv
# reading data from csv file
with open('/Users/saman/Downloads/hpi_master.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
# extract the Y column from dataset: it is an avarage of two last column
y_train = []
for i in range(1,len(data)):
    if data[i][9] and data[i][8]:
        y_train.append((int(float(data[i][9]))+int(float(data[i][8])))/2)
# print(y_train)

with open("/Users/saman/Downloads/hpi_master.csv", "r") as source: 
    reader = csv.reader(source) 

    with open("output.csv", "w") as result: 
        writer = csv.writer(result) 
        for r in reader: 
            if r[8] and r[9]:
            # Use CSV Index to remove a column from CSV 
                p=3
                q=3
                if r[0] == 'purchase-only':
                    p=0
                else:
                    p=1
                if r[1] == 'monthly':
                    q=0
                else:
                    q=1
            #r[3] = r['year'] 
                writer.writerow((p, q, r[3], r[4], r[5],r[6],r[7]))

with open('output.csv', newline='') as f:
    reader = csv.reader(f)
    X_train = list(reader)

del X_train[0]
# Create a sample dataframe
df = pd.DataFrame(X_train)

# Use the Pandas factorize method to map the categorical values to integers
df[7] = pd.factorize(df[2])[0]
df[8] = pd.factorize(df[3])[0]
df[9] = pd.factorize(df[4])[0]

# Show the result

df = df.drop(2, axis = 1)
df = df.drop(3, axis = 1)
df = df.drop(4, axis = 1)

print(df)

df_x = df
df_y = pd.DataFrame(y_train)
train_x, test_x = train_test_split(df_x, test_size=0.2)
train_y, test_y = train_test_split(df_y, test_size=0.2)


ridge_params = {'alpha': [0.001, 0.01, 0.1, 1 ,10,100] }

ridge_grid = GridSearchCV(Ridge(),
                           ridge_params , cv=5,
scoring = 'neg_mean_squared_error')
ridge_grid.fit(train_x, train_y)
y_pred = ridge_grid.predict(test_x)

print(y_pred)
print(test_y)
best_ridge = ridge_grid.best_estimator_
# print(best_ridge)