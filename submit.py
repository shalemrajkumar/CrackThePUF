import numpy as np
import sklearn
from sklearn.svm import LinearSVC

# You are allowed to import any submodules of sklearn that learn linear models e.g. sklearn.svm etc
# You are not allowed to use other libraries such as keras, tensorflow etc
# You are not allowed to use any scipy routine other than khatri_rao

# SUBMIT YOUR CODE AS A SINGLE PYTHON (.PY) FILE INSIDE A ZIP ARCHIVE
# THE NAME OF THE PYTHON FILE MUST BE submit.py

# DO NOT CHANGE THE NAME OF THE METHODS my_fit, my_map, my_decode etc BELOW
# THESE WILL BE INVOKED BY THE EVALUATION SCRIPT. CHANGING THESE NAMES WILL CAUSE EVALUATION FAILURE

# You may define any new functions, variables, classes here
# For example, functions to calculate next coordinate or step length

################################
# Non Editable Region Starting #
################################
def my_fit( X_train, y_train ):
################################
#  Non Editable Region Ending  #
################################
    
    # Use this method to train your models using training CRPs
    # X_train has 8 columns containing the challenge bits
    # y_train contains the values for responses
    
    # THE RETURNED MODEL SHOULD BE ONE VECTOR AND ONE BIAS TERM
    # If you do not wish to use a bias term, set it to 0
    
    clf_PUF = LinearSVC(loss = "hinge", C = 1, verbose=False)
    
    X = my_map(X_train)
    
    clf_PUF.fit(X, y_train)
    
    y = 1 - 2*y_train
    
    return clf_PUF.coef_, clf_PUF.intercept_
    

################################
# Non Editable Region Starting #
################################
def my_map( X ):
################################
#  Non Editable Region Ending  #
################################

	# Use this method to create features.
	# It is likely that my_fit will internally call my_map to create features for train points
    
    n_samples, n_feats = X.shape

    d = 2 * X - 1

    e = np.cumprod( np.flip( d, axis = 1 ), axis = 1 )

    x = np.concatenate([e, d[:, :-1]], axis=1)

    x = x[:, :, None] * x[:, None, :]

    feat = x[:, np.triu(np.ones_like(x[0, :, :], dtype=bool), k=1)]
            
    return feat


################################
# Non Editable Region Starting #
################################
def my_decode( w ):
################################
#  Non Editable Region Ending  #
################################

	# Use this method to invert a PUF linear model to get back delays
	# w is a single 65-dim vector (last dimension being the bias term)
	# The output should be four 64-dimensional vectors

    p = np.zeros((64))
    q = np.zeros((64))
    r = np.zeros((64))
    s = np.zeros((64))
    
    
    p[63] = w[-1]
    
    for i in range(62, 0, -1):
    
        p[i] = 2 * w[i+1] - p[i+1]
        
    
    p[0] = w[1] + w[0]- 0.5 * p[1]
    
    r[0] = 2 * w[0] - p[0]

    if (np.any(p<0)):
        e = np.min(p)
        p = p - e
        q = q - e
        
    if (np.any(r<0)):
        g = np.min(r)
        r = r - g
        s = s - g        
    
    return p, q, r, s

