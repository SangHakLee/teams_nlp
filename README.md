# teams_nlp
팀스 자연어처리팀

# How to use

## Pre-Requiered

### Python
python v3.x.x

### pip modules
- pip install flask
- pip install flask-bootstrap
- pip install flask-moment
- pip install Flask-WTF
- pip install unidecode
- pip install gensim
- pip install nltk

### nltk

> AttributeError: module 'nltk' has no attribute 'download'
> - nltk.download()

> AttributeError: module 'nltk' has no attribute 'word_tokenize'
> - nltk.download('all')

1. Run python cmd
1. import
```python
>>> import nltk
>>> nltk.download()
>>> nltk.download('all')
```
1. download
![image](https://user-images.githubusercontent.com/9030565/43557236-a429a19a-963e-11e8-9393-b3123f2444ef.png)
## Run
```
$ python translate_local.py
```