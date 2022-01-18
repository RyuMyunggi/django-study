# Django

## Model
### model
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
- 필드타입
    * AutoField: ID로 사용가능한 자동으로 증가하는 integerField. 모델의 기본키 필드는 별도 지정하지 않으면 자동으로 추가됌
    * BigAutoField: 1 ~ 9223372036854777807까지 숫자에 맞도록 보장. 64비트 정수
    * BigIntegerField: -9223372036854 ~ 9223372036854777807까지까지 숫자 보장. 기본 필드 위젯은 text input
    * BooleanField: true / false field, None에 대한 허용이 필요하다면 NullBooleanField를 사용해야함
    * CharField: 작은 문자열에서 큰 사이즈의 문자열을 위한 문자열 필드. 많은 양의 텍스트일 경우 TextField를 사용해야함
        * 추가적으로 max_length(필드의 최대길이)를 지정할 수 있음. 필수 인수
    * DateField: 날짜 필드
        * auto_now: 객체가 저장될 때마다 매번 자동으로 필드를 현재시간이 설정
        * auto_now_add: 객체가 처음 생성될 때 자동으로 현재시간이 설정
    * DateTimeField: 날짜 시간 필드
    * DecimalField: 고정소수. 두 개의 필수 인수가 있음
        * max_digits: 숫자에 허용되는 최대 자리수
        * decimal_places: 숫자와 함께 저장될 소수 자릿수
    * EmailField: 유효한 이메일 주소인지 체크하는 CharField. 입력값을 검증하는데 EmailValidator 사용
    * FileField: 파일 업로드 필드. primary key 인수를 지원하지 않고 사용할 경우 에러 발생
    * ImageField: FileField로 부터 모든 속성과 메서드를 상속받지만 유효한 이미지인지 검증
    * IntegerField

- 필드 옵션
    * blank: validation시에 empty 허용 (default=False)
    * null: 허용 여부 (default=False)
    * db_index: 인덱스 필드 여부 (default=False)
    * default 값 지정, 혹은 return 함수 지정
    * unique: 현재 테이블 내 유일성 여부 (default=False)
    * choice: select 박스 사용시 사용
    * verbose_name: 필드 레이블, 미지정시 필드명 사용
    * primary_key: 해당 필드가 primary key임을 표시

- 관계형 필드
    * 모델을 설계하는데 매우 중요한 개념.
    * on_delete (필드 간의 관계에서 삭제에 대한 옵션)
        * 1인 쪽의 데이터가 삭제 되었을 때 N의 데이터를 어떻게 처리 할지에 대한 설정
        * CASCADE: 이와 연결되어 있는 모든 N쪽 데이터를 삭제
        * PROTECT: 1인 쪽의 데이터가 삭제 되지 않도록 보호해줌
        * SET_NULL: null 값으로 대체하게 되어 필드에 null=True 옵션이 있어야함
        * SET_DEFAULT: default로 값을 대체하게 되어 필드에 default=True 옵션이 있어야만 가능
        * DO_NOTHING: 아무것도 하지 않지만 db에서 오류가 날 수 있음
        * SET: 대체할 값을 지정

    * ForeignKey
        * 1:N 관계를 의미
        * ex) 한 명의 유저가 쓰는 다수의 포스팅, 한 명의 유저가 쓰는 다수의 댓글, 게시글과 댓글
        ```python
        class Post(models.Model):
          pass
        class Comment(models.Model):
          post = models.ForeignKey(Post, on_delete=models.CASCADE)
        ```
    * OneToOneField
       * 1:1 관계를 의미
       * ex) 한 명의 유저는 한 개의 프로필
       ```python
       class User(AbstractBaseUser):
          pass
       class Profile(models.Model):
          user = models.OneToOneField(User, on_delete=models.CASCADE)
       ```
    * ManyToManyField
        * M:N 관계를 의미
        * M:N 관계에서 어느 쪽이라도 필드 지정이 가능
        * 한 개의 포스팅에 여러개의 태그, 한 개의 태그에 여러개의 포스팅
        ```
        class Post(models.Model):
            pass
        class Article(models.Model):
            pass
        class Tag(models.Model):
            name = models.CharField(max_length=100, unique=True)
            post_set = models.ManyToManyField('Post', blank=True)
            article_set = models.ManyToManyField('Article', blank=True)
        ```

    * reverse_name
        * 참조 대상이 되는 모델에서 본인을 참조하는 모델의 데이터를 접근 할 때 사용하는 형식
        * default: 모델명소문자_set
- ex)
    ```python
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation', primary_key=True)

    class Product(models.Model):
        owner = models.ForeignKey(User, on_delete=models.CASCADE)
    ```

### Meta
- 메타 데이터는 다른 데이터에 대한 정보를 제공하는 특정 데이터 집합
- 메타 클래스는 권한, 데이터베이스 이름, 단/복수 이름, 추상화, 순서 등과 같이 모델에 대한 사항을 정의하는데 사용(선택사항)
- 메타 데이터의 가장 유용한 기능 중 하나는 모델 타입을 쿼리할 때 반환되는 기본 레코드 순서를 제어(sorting)
- django meta option
    * db_table: 데이터 베이스 내에서 테이블을 식별하는데 사용해야하는 이름을 설정
    * ordering: 모델 객체의 순서를 정으하는데 사용
    * verbose_name: 사람이 읽을 수 있는 모델 객체의 이름으로 관리자 화면등에 등장
- 주요 메소드가 위치하는 순서
    * 모든 데이터베이스 필드
    * 커스텀 매니저 속성
    * Meta 클래스
    * def __init__() 메소드
    * def __str__() 메소드
    * def save() 메소드
    * def get_absolute_url() 메소드
    * 기타 커스텀 메소드

    ```python
    class Meta:
        db_table = 'data_table'
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
