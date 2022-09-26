9월 6일 화요일 (이론)

**Django**



---

# 1. Form

#### `html`에 작성한 `form` 태그 대신 `forms.py` 에 `ArticleForm` 클래스로 작성한다.

- `Model` 클래스와 관련없다.
- `form` 의 입력 부분을 `html` 태그로 작성하지않고 `form `클래스를 작성하여 사용한다.
  - `html` 에서 `{{ form }}`으로 사용한디.
  - `form`의 형태가 다 붙어있기 때문에 `. as_p` 를 사용하여 각각 요소를 `p` 태그로 감싸 띄워준다.

- `Widgets`을 활용하여 `input` 태그의 표현을 바꾼다.
  - `Charfield`는 `input text` 형태만 출력이 가능하다. (유효성 검사 가능)
  - `form` 필드의 속성 값에 위젯 할당하여 `input` 요소의 표현을 바꾼다. 
  - 위젯은 `input` 요소의 단순한 출력 부분 담당한다. ( 유효성 검사 불가 )

- `Model` 클래스와 차이점
  - `TextField`가 존재하지 않는다.
  - `CharField` 의 속성 값이 필수 입력 사항이 아니다.



## Code

```python
# articles/forms.py

from django import forms  

class ArticleForm(forms.Form):
     title = forms.CharField(max_length=10)
     content = forms.CharField(widget=forms.Textarea) 
```

```python
# articles/view.py

def new(request):
    # form 클래스 인스턴스 사용하기(view함수에서 데이터를 html에 넘겨준다.)
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

```html
<!-- articles/new.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>NEW</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
      
    {{ form.as_p }}

    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">뒤로가기</a>
{% endblock content %}
```



---

# 2. ModelForm

#### `form.py` 와 `Model` 클래스의 **사용자 입력 필드**가 **중복**되므로  `Model` 클래스를 기반으로한  `ModelForm` 클래스를 만들어준다.

- `Model` 클래스와 관련있다.

- 사용자의 입력을 동일한 필드에 매핑을 시키고 싶다면 `Model` 클래스를 기반으로한 `form`을 만들어준다.
- `forms.py` 에 `ModelForm` 을 만든다. ( `ArticleForm` 클래스를 지우고 작성 )
- `forms` 라이브러리의 `ModelForm` 클래스를 상속 받는다. 

- `Model` 클래스에 대한 정보를 가져감으로써 재정의할 필요가 없다.
- 어떤 모델을 기반으로 `form`을 작성할 것인지에 대한 정보를 `Meta` 클래스에 지정한다.

- `Meta` 클래스 (참고)

  ```python
  class Meta:
      model = Article 
      fields = '__all__'  
  ```

  - `ModelForm` 클래스의 정보를 작성하는 곳
  - `model` , `fields`변수명 변경 금지
  - `model`에는 클래스를 호출하지 않고 이름만 작성
    - 참조 값
    - 클래스 값을 호출하지 않고 클래스 자체가 전달된다.
    - `model`을 인스턴스로 만들지 않음
    - **필요한 시점에 호출(사용)**한다.
  - `Meta` 클래스의 위치에 파이썬의 문법적인 의미부여 하지말기
    -  `ModelForm` 클래스의 설계가 `model`의 정보를 등록하는 곳을 안쪽 클래스로 동작하도록 설계되어있다.
    -  설계의 사용법을 익히는 것이지 분석할 필요는 없다. ( 분석 시간이 아님 )



## Code

#### 변경 전

```python
# articles/models.py

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

```python
# articles/forms.py

from django import forms  

class ArticleForm(forms.Form):
     title = forms.CharField(max_length=10)
     content = forms.CharField(widget=forms.Textarea) 
```

#### 변경 후

```python
# articles/forms.py

from django import forms   
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article 
        fields = '__all__'  
```



---

# 3. ModelForm with view funcions

#### `ModelForm` 클래스를 사용하여 함수 줄이기

- 필드의 개수와 상관없이 하나로 줄어든다.
- `form` 은 **유효성 검사** 도구
  -  `form.is_valid()`
  - 방어 수단 (보안)
  - `create` 인스턴스를 저장하기 전에 검증을 진행
- `is_valid()`의 반환 값이 `False`인 경우
  - `form` 인스턴스의 `errors `속성에 값이 작성되는데, **유효성 검증을 실패한 원인**이 **딕셔너리 형태로 저장**됨 



## Code

#### 변경 전

```python
# articles/view.py

def create(request):
    # 사용자의 데이터를 받아서
    title = request.POST.get('title')
    content = request.POST.get('content')

    # DB에 저장
    article = Article(title=title, content=content)
    article.save()

    return redirect('articles:detail', article.pk)
```



#### 변경 후  (유효성 검사) 

- `is_valid()` 의   `errors  `속성 `print`

```python
# articles/view.py

def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():           # True / False  # 검증을 통과하면 (검증 과정)
        article = form.save()                     # 생성된 게시글을 저장하면 새로 생성된 글을 반환 값으로 준다.
        return redirect('articles:detail', article.pk)
    print(f'에러: {form.errors}')
    
     # 에러: <ul class="errorlist"><li>title<ul class="errorlist"><li>필수 항목입니다.</li></ul></li></ul>
    
    return redirect('articles:new')               # 통과 못하면 new.html로 간다.
```

- 사용자에게  `error` 메시지 출력

```python
# articles/view.py

def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():           # True / False  # 검증을 통과하면 (검증 과정)
        article = form.save()
        return redirect('articles:detail', article.pk)
    # print(f'에러: {form.errors}')
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```



<img width="458" alt="필수 항목입니다  (유효성 검사)" src="https://user-images.githubusercontent.com/109335452/188556534-b304084f-5939-404e-b492-3bfd41bf573f.png"    >



# 4. Form과 ModelForm

- 공통점
  - 사용자의 요청을 받아서 처리한다.

- `ModelForm`이 `Form`보다 더 좋은 것이 아니라 각자 **역할이 다른 것**이다.
  - 사용자의 요청에 따라 다르다.
    - DB에 저장할지
    - 데이터로만 쓸지
-  `Form`
  - 사용자로부터 받은 데이터가 DB에 영향을 미지치 않고 단순 데이터만 사용되는 경우
  - 예시
    - 로그인: 인증과정에만 사용
- `ModelForm`
  - 사용자로부터 받은 데이터가 DB와 연관되어 있는 경우
  - 예시
    - 게시판에 글 작성



---

# 5. Widgets 활용하기

- **유효성검사와는 관련없다.**
- **출력되는 `input` 태그의 표현을 바꾼다.**
- DB에 영향을 주지 않는다.
- `ArticleForm` 클래스 안에 `Meta` 클래스와 **따로 위젯을 작성**하는 방법을 권장한다.
- 위젯은 `forms` 필드 안에서 작성한다.

