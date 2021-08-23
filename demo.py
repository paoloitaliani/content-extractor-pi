"""
In order to implement the content_extractor you need to follow 3 steps:
- Step 1: load a pre-trained word embedding
  model, I'm using the one available here https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing
- Step 2: define train_df and target_df. train_df is a pandas DataFrame containing the text examples in one column
  and the corresponding labels in the other one. train_df it's used for training the content_extractor model. target_df
  is a pandas DataFrame containing all the text examples that we have at disposal.
- Step 3: We define the ContentExtractor object,
  we train the model and extract just the desired examples that will be saved in the target examples object.
"""

from content_extractor import contextractor as cte
from gensim.models import KeyedVectors
import pandas as pd

# Step 1
W2V_MODEL = KeyedVectors.load_word2vec_format('/Users/Niolo/Downloads/GoogleNews-vectors-negative300.bin.gz',
                                              binary=True)
# Step 2
train_df = pd.read_csv("data/train_df.csv")
target_df = pd.read_csv("data/target_df.csv")

# Step 3
cont_ext = cte.ContentExtractor(W2V_MODEL)
cont_ext.train_model(train_df)
target_examples = cont_ext.extract_content(target_df)
