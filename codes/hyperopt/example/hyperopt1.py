from hpsklearn import HyperoptEstimator, extra_trees
from sklearn.datasets import fetch_mldata
from hyperopt import tpe
import numpy as np

# Download the data and split into training and test sets

digits = fetch_mldata('MNIST original')

X = digits.data
y = digits.target

test_size = int(0.2 * len(y))
np.random.seed(13)
indices = np.random.permutation(len(X))
X_train = X[ indices[:-test_size]]
y_train = y[ indices[:-test_size]]
X_test = X[ indices[-test_size:]]
y_test = y[ indices[-test_size:]]

# Instantiate a HyperoptEstimator with the search space and number of evaluations

estim = HyperoptEstimator(classifier=extra_trees('my_clf'),
                          preprocessing=[],
                          algo=tpe.suggest,
                          max_evals=1,
                          trial_timeout=300)

# Search the hyperparameter space based on the data

estim.fit( X_train, y_train )

# Show the results

print( estim.score( X_test, y_test ) )
# 0.962785714286

print( estim.best_model() )
# {'learner': ExtraTreesClassifier(bootstrap=True, class_weight=None, criterion='entropy',
#           max_depth=None, max_features=0.959202875857,
#           max_leaf_nodes=None, min_impurity_decrease=0.0,
#           min_impurity_split=None, min_samples_leaf=1,
#           min_samples_split=2, min_weight_fraction_leaf=0.0,
#           n_estimators=20, n_jobs=1, oob_score=False, random_state=3,
#           verbose=False, warm_start=False), 'preprocs': (), 'ex_preprocs': ()}
