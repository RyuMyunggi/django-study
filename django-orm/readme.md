# Django ORM

## Django ORM이란 ?
* sql: structured query language. 관계형 데이터 베이스에서 수정, 삭제 등의 동작을 할 때 사용되는 언어
* orm:
    * 객체(object)의 관계(relational)를 연결해주는 것을 의미. 한 마디로 객체지향적인 방법을 사용하여 데이터베이스를 조작 할 수 있는 것
    * django orm은 파이썬 애플리케이션과 데이터베이스 sql 사이의 통역사의 역할. sql 쿼리문 없이도 쉽게 데이터 베이스의 데이터들을 다룰 수 있음
    * django model class를 통해서 객체를 만들고 이 객체를 통해서 db에 접근하는 방식
    * ex) Book.objects.all() (all()은 모델의 모든 데이터들 가져오는 명령어)
        * 여기서 objects는 model manager. db와 django model 사이에 질의 연산의 인터페이스 역할

## ORM의 장단점
### 장점
* 빠르고 간단하게 개발이 가능하여 생산성 증가. 사소한 것들을 개발자가 신경쓰지 않아도 됌
* 부수적인 코드가 줄어들고 객체에 대한 코드를 별도로 작성하다보니 가독성이 좋아짐
* 유지보수가 편하고 코드의 재사용성이 높아짐

### 단점
* ORM에 대한 추가 학습이 필요
* 프로젝트가 일정 수준의 규모가 올라간다면 sql 쿼리로 작성하는 것이 좋을 수 있음
* 정확히 원리를 이해하지 않아 이후에 발생할 문제 대처 능력이 떨어질 수 있음

## Django Model API
* all(): 테이블 데이터를 전부 가져옴
* value(*fields): dictionary 형태로 변환하여 데이터를 가져옴
* get(): 하나의 row만을 가져옴
* filter(): 특정 조건에 맞는 row들을 가져옴
* exclude(): 특정 조건을 제외하고 나머지 row들을 가져옴
* count(): 데이터의 개수(row의 수)를 가져옴
* order_by(): 데이터를 키에 따라 정렬하기 위해 order_by() 사용, -붙으면 내림차순
* disinct(): 중복된 값은 하나로 표시하여 필드 중복 방지
* first(): 데이터들 중 처음에 있는 row만 가져옴
* last(): 데이터들 중 마지막 row만 가져옴
* create(**kwargs): 새로운 object를 생성하는 동시에 저장. 테이블에 새로운 데이터 추가하고 생성된 instance를 반환 (insert)
* save(): 테이블에 데이터 갱신 (update)
* delete(): 테이블에 데이터 삭제
* model api를 연결해서 사용 가능
    * ex) Object.objects.filter(category = 1).values()

## 쿼리셋 (Query Set)이란 ?
* objects를 사용해서 다수의 데이터를 가져오는 함수를 사용할 때 반환되는 객체
* 전달 받은 모델의 객체 목록
* 리스트와 구조는 같지만 파이썬 기본 자료구조가 아니까 때문에 읽고 쓰기 위해서는 자료형 변환을 해줘야함
