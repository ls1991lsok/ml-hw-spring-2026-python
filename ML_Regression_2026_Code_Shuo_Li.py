import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline

train = pd.read_csv('spring2026_kaggle_linear_regression_challenge_train.csv')
test = pd.read_csv('spring2026_kaggle_linear_regression_challenge_test.csv')
sample = pd.read_csv('spring2026_sampleSubmission.csv')

feats = [f'x{i}' for i in range(15)]
medians = train[feats].median()
X_train = train[feats].fillna(medians)
X_test = test[feats].fillna(medians)
y = train['target']

model = make_pipeline(StandardScaler(), Ridge(alpha=4100))
model.fit(X_train, y)
pred = model.predict(X_test)

submission = pd.DataFrame({'Id': test['Id'], 'target': pred})
submission = sample[['Id']].merge(submission, on='Id')
submission.to_csv('Li_Shuo.csv', index=False)
