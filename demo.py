from content_extractor import contextractor as cte
from gensim.models import KeyedVectors

W2V_MODEL = KeyedVectors.load_word2vec_format('/Users/Niolo/Downloads/GoogleNews-vectors-negative300.bin.gz',
                                              binary=True)

cont_ext = cte.ContentExtractor(W2V_MODEL)
cont_ext.train_model(train_df)
target_paragraphs = cont_ext.extract_content(target_df)