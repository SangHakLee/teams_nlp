# 1. load_word2vec_format 느린 처리 해결
## 1.1. 문제
자연어 처리 `load_word2vec_format`으로 불러오는 데이터의 크기가 너무 커서 `most_similar` 요청마다 1분 내외로 걸리는 문제

## 1.2. 가정
1. `most_similar` 함수가 느리다?
    - **X**로 판단
    - 이유: 광현님이 보여주신 Jupyter 환경에선 빠르다
1. `load_word2vec_format` 처음 불러오면 그다음 `most_similar`는 빠르다?
    - **O**로 판단
    - 이유: 코드를 보니 input할 때마다 `load_word2vec_format`를 하고 있다. 이 부분에서 오래 걸릴 것 같다.

## 1.3. 해결책
가장 빠르고 쉬운 해결책은 `load_word2vec_format`을 매번 부르지 않는 것.
python process의 memory 변수 접근 속도를 믿어본다.

### 1.3.1. 프로세스
1. similar()
1. binary 파일의 내용을 읽어서 저장할 전역 변수 정의
    ```python
    model = None
    ```
1. `load_word2vec_format`는 항상 불러오지 않고 `model`이 `None`일 때만 불러온다. 
    - 1 요청: `None`이기 때문에 `load_word2vec_format` 후 `model`에 저장
    - 2 요청: `None`아니기 때문에 `model` 값 사용
    - n 요청: `None`아니기 때문에 `model` 값 사용

### 1.3.2. TODO
여러분이 생각해보세요.

이 방법의 문제점은 `2..n` 요청은 빠르지만 `1` 요청은 느리다는 점

만약 flask 웹 서버가 올라가기 전에 먼저 `load_word2vec_format` 후 model에 넣고 쓴다면??