# Query set

### 참고자료
* https://www.youtube.com/watch?v=EZgLfDrUlrk 


### Lazy Loading 
* 정말 필요한 시점에 SQL을 호출
* 직접 사용하지 않으면 SQL 사용 X
* 선언한 시점에 SQL 호출되는 것이 아닌 list()로 묶는 시점에 실제 SQL이 호출됨
  ```python
  users: QuerySet = User.objects.all()        # 여기서의 user는 쿼리셋
          .
          .
          .
  user_list: List[User] = list(user)          # 이 시점이 실제 SQL이 호출되는 시점
  ```
* SQL의 경우 한 번만 호출해서 데이터를 재사용하면 되지만 ORM은 이후 로직을 모르기 때문에 현 시점에 필요한 만큼만 데이터를 가져오기 때문에 비효율적인 부분도 있음
    ```python
  users: QuerySet = User.objects.all()
  
  user = users[0]                   # LIMIT 1 옵션이 걸린 SQL 호출
  user_list = list(users)           # 모든 user의 목록을 얻기 위해 다시 SQL을 호출
    
    ```
* queryset caching
    * 순서를 바꾸는 동작만으로도 비효율을 줄일 수 있음
    ```python
  users: QuerySet = User.objects.all()
  
  user_list = list(users)           # 모든 user의 목록 호출
  user = users[0]                   # 기존 정보를 캐싱하여 불필요한 호출 방지
    
    ```
