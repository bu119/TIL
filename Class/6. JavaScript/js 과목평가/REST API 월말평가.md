# REST API 월말평가

다음 주 진행되는 REST API 월말평가 관련하여 안내드립니다.

- 일시: 10월 24일 (월) 09:00 ~ 11:00
- 과목: REST API
- 시험범위: DRF
- 시험유형 : 실습형
- 참고사항: postman 사용 가능 이번 시험은 API를 만드는 과제인만큼 postman을 사용하여 테스트 가능합니다. 잘 준비하셔서 모두 좋은 결과 있기를 바라겠습니다. 평가 관련해서 문의사항 있을 시 쓰레드를 통해 질문 남겨주세요.
  1. Article CRUD를 위한 API만 만들어도 통과할 수 있음을 강조
  2. 적어도 `runserver`는 작동해야 한다
  3. 디테일한 문제의 요구사항을 충족하지 못하더라도 기본 로직을 구현해보아라



## Single Model (p75 부터 ~ )

- view함수 작성
- serializer 파일 작성

import 도 다 되있다.



- 1:N이 시험문제

### 시험

- get_object_or_404

```python
article = get_object_or_404(Article, pk=article_pk)
```

