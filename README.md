# django-study
python django study

## Django Model
- Django 웹 애플리케이션은 모델이라는 파이썬 객체를 통해 데이터에 접속하고 관리
- 모델은 저장된 데이터의 구조를 정의
- 모델에는 필드 타입, 데이터의 최대 크기, 기본 값, 선택 리스트 옵션 등이 있음
- 모델의 정의는 기초 데이터 베이스에 대해서 독립적
- Model 등록 절차
    - models.py에서 모델 클래스 정의
    - shell에서 migrations, migrate 실행
    - admin.py에 모델클래스 등록

### Field
- 모델은 모든 타입의, 임의 숫자 필드를 가질 수 있음
- 각각의 필드는 데이터베이스 테이블에 저장할 데이터 column을 나타냄
- ex)
    
    ```python
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    ```
    

### Meta
- 메타 데이터의 가장 유용한 기능 중 하나는 모델 타입을 쿼리할 때 반환되는 기본 레코드 순서를 제어(sorting)
- 필드 이름 목록의 순서를 ordering 속성에 지정해야함
- ex)
    
    ```python
    class Meta:
        ordering = ['-my_field_name']
    ```
    

### Method
- 모델은 메소드를 가질 수 있음
- 최소한 모든 모델마다 표준 파이썬 클래스의 메소드은 __str__()을 정의하여 각각 object가 사람이 읽을 수 있는 문자열을 반환 하도록 해야함
- 이 문자열은 관리자 사이트에 잇는 개별적인 레코드들을 보여주는데 사용
- ex)
    
    ```python
    def __str__(self):
        return self.field_name
    ```
