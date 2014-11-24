from sklearn import tree
train_data = list()
train_label = list()
with open('copd_1000.txt', 'rb') as f:
    for row in f.xreadlines():
        nr = row.strip().split(',') ## nr
        finalrow = [float(nr[3]),
                    float(nr[4]),
                    float(nr[5]),
                    float(nr[6]),
                    float(nr[7])]
        train_data.append(finalrow)
        train_label.append(int(nr[8]))

clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_data, train_label)
''' TEST on test data '''
test_data = list()
with open('copd_test.txt', 'rb') as f:
    for row in f.xreadlines():
        nr = row.strip().split(',') ## nr
        finalrow = [float(nr[3]),
                    float(nr[4]),
                    float(nr[5]),
                    float(nr[6]),
                    float(nr[7])]
        test_data.append(finalrow)

''' TEST on train data '''
# res = clf.predict(train_data)
# counter = 0
# for i in range(1000):
#     if res[i] == train_label[i]:
#         counter += 1
# print counter

''' TEST on test data '''
# res = clf.predict(test_data)
# counter = 1
# for i in res:
#     print '%s ------ %s' % (counter, i)
#     counter += 1