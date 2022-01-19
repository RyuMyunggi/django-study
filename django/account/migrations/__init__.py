"""
models.py에 정의된 모델의 생성/변경 내역의 히스토리 및 데이터베이스 적용
이를 사용하면 데이터베이스에 접근하지 않아도 모델의 반복적인 변경을 가능하게 해줌
migrations 테이블 이름은 앱이름_모델이름이 조합되어 자동으로 생성
pk가 지정되어 있지 않으면 자동으로 id 컬럼 생성, pk키 지정
관례적으로 django는 외래키 컬럼의 마지막에 _id 자동 추가

관련 명령어
    * python manage.py makemigration <app-name>: 마이그레이션 파일 생성. sql command 파일 생성
    * python manage.py migrate <app-name>: 마이그레이션 적용
    * python manage.py showmigrations <app-name>: 마이그레이션 적용 현황
    * python manage.py sqlmigrate <app-name> <migration-name>: 지정 마이그레이션 sql 내역
        ex) python manage.py sqlmigrate account 0001
"""