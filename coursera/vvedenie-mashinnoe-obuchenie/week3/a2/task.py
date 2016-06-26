from sklearn import datasets
from sklearn import feature_extraction

TfidfVectorizer = feature_extraction.text.TfidfVectorizer

newsgroups = datasets.fetch_20newsgroups(subset='all', categories=['alt.atheism', 'sci.space'])