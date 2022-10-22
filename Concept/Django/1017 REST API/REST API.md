[TOC]

# REST API

## 1. REST

- Representational State Transfer
- API Server를 개발하기 위한 일종의 소프트웨어 방법론 (규약 X)
- REST 원리를 따르는 시스템을 RESTful 하다고 부른다.
- **자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법**을 서술 (모음)



## 2. REST에서 자원을 정의하고 주소를 지정하는 방법

1. 자원의 식별
   - **URL**
2.  자원의 행위
   - **HTTP Method** (GET, POST, PUT, DELETE)
3. 자원의 표현
   - **Json**으로 표현된 데이터를 제공
   - Json ( 현재 API에서 가장 많이 사용하는 데이터 타입 )

---

# Response JSON

- JSON을 응답하는 Django 서버를 구성하는 법을 학습
- **Django REST framework를 사용한 JSON 데이터 응답해보기**



## 1. 사전 준비

1.  가상 환경 생성, 활성화
2.  패키지 설치
3.  migrate 진행
4.  준비된 fixtures 파일을 load하여 실습용 초기 데이터 입력
5.  입력된 데이터 확인



## 2. Serialization

- 데이터 구조나 객체를 어떠한 언어나 환경에서도 나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정
- 변환 포맷은 json이 가장 보편적으로 쓰인다.

<img width="1003" alt="Serialization" src="https://user-images.githubusercontent.com/109335452/197335907-9056c31d-757d-4c38-8e64-ba4b56f686cd.png">

- Django의 **`serialize( )`** 는 Queryset 및 Model Instance 와 같은 **복잡한 데이터**를 **JSON**, XML 등의 **유형으로 쉽게 변화할 수 있는 Python 데이터 타입으로 만들어준다.**
- 데이터 구조나 객체 (Object)   →   **`Serialize( )`**   →   가공된 데이터 생성 (다른 포맷으로 재구성 할 수 있는 파일)   →   **Object를 Json으로 변환 가능**



## 3. Django REST framework를 사용한 JSON 응답

### 1. Django REST framework (**DRF**)

- Django에서 RESTful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리
- **DRF를 활용하여 JSON 데이터를 응답하는 Django 서버를 구축할 것이다.**



### 2. REST framework 구현

1. `djangorestframework` 설치 ( pip install )

2. settings.py 의 INSTALLED_APPS에 `rest_framework`등록

   ```python
   # 프로젝트 플더 / settings.py
   
   INSTALLED_APPS = [
       'articles',
       'django_extensions',
       'rest_framework',
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'drf_yasg',
   ]
   ```

3. `ModelSerializer`는 ModelForm 클래스와 매우 유사한 구조로 작동

   ```python
   # 앱 폴더 / serializers.py
   
   from rest_framework import serializers
   from .models import Article, Comment
   
   
   class ArticleListSerializer(serializers.ModelSerializer):
   
       class Meta:
           model = Article
           fields = ('id', 'title', 'content', )
   ```

4.  **`serialize( )`** 구현

   ```python
   # 앱 폴더 / view.py
   
   @api_view(['GET'])
   def article_list(request):
   	articles = Article.objects.all()
       serializer = ArticleListSerializer(articles, many=True)
           return Response(serializer.data)
   ```

   - serialize( ) 과정으로 Python 타입의 serializing된 데이터를 만듬

   ```python
   serializer = ArticleListSerializer(articles, many=True)
   ```

   - **serializer**는 Python 타입의 serializing된 데이터

   ```python
   serializer.data
   ```

   -  serializing된 데이터에 `.data` 만 하면 **Json**이 나온다.

---

# REST framework - Single Model

- 단일 모델

## 1. 사전 준비

### 1. 가상 환경 설정

```bash
$ python -m venv venv
```

### 2. 가상 환경 활성화

```bash
$ source venv/Scripts/activate
```

### 3. 패키지 목록 설치

```bash
$ pip install -r requirements.txt
```

### 4. 프로젝트 생성

```bash
$ django-admin startproject [프로젝트이름] .
```

### 5. 애플리케이션(앱) 생성

```bash
$ python manage.py startapp [애플리케이션이름]
```

### 6. migrations

- 데이터베이스에 테이블을 생성하기 위한 설계도 작성

```bash
$ python manage.py makemigrations
```

### 7. migrate

- makemigrations로 만든 설계도를 실제 데이터베이스(db.sqlite3 DB)에 반영

```bash
$ pythion manage.py migrate
```

### 8. object 불러오기

```bash
$ python manage.py loaddata articles.json
```

### 9. DRF 설치

- `djangorestframework` 설치

```bash
$ pip install djangorestframework
```

### 10. DRF 등록

- settings.py 의 INSTALLED_APPS에 `rest_framework`등록

```python
# 프로젝트 플더 / settings.py

INSTALLED_APPS = [
    'articles',
    'django_extensions',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

### 11. 패키기 목록 업데이트

```bash
$ pip freeze > requirements.txt 
```

---

# ModelSerializer