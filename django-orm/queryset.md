# Query set

### 참고자료
* https://www.youtube.com/watch?v=EZgLfDrUlrk 

## Django Queryset
* 전달 받은 객체의 목록
* query set은 반드시 1개의 query(메인쿼리)를 가지면 0~n개의 queryset(추가 쿼리셋)을 가짐
  * 추가 쿼리셋은 prefatch_related()에 의해서 결정
### Django queryset 특징
* Lazy Loading
* Caching 
* Eager Loading

### Lazy Loading 
* 정말 필요한 시점에 SQL을 호출
* 직접 사용하지 않으면 SQL 사용 X
* 선언한 시점에 SQL 호출되는 것이 아닌 list()로 묶는 시점에 실제 SQL이 호출됨 (실제 쿼리셋에 담겨있는 데이터를 이용하는 경우에 SQL문이 호출)
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
* 주의할 점
  * LazyLoading이라는 특성 때문에 여러 개의 쿼리셋이 한번에 합쳐 실행되면 매우 느리게 동작할 수 있음
  * LazyLaoding의 특성 때문에 이미 알고 있는 값도 다시 한 번 호출이 일어날 수 있음
  
### queryset caching
* 순서를 바꾸는 동작만으로도 비효율을 줄일 수 있음
    ```python
  users: QuerySet = User.objects.all()
  
  user_list = list(users)           # 모든 user의 목록 호출
  user = users[0]                   # 기존 정보를 캐싱하여 불필요한 호출 방지
    
    ```
 
### eager Laading
* SQL로 한 번에 많은 데이터를 가져오려는 경우 쿼리셋에서는 Eager Lading(즉시 로딩)이라는 전략이 존재
* django에서는 즉시 로딩을 selected_related(), prefatch_related() 메서드를 통해 Eager Loading을 사용할 수 있음
* selected_related(): join()을 통해 데이터를 즉시 로딩. 역참조 불가
* prefatch_related(): 추가 쿼리셋을 이용해 데이터를 갖고 오고 애플리케이션 단에서 합쳐서 데이터를 반환. 역참조 가능
  ```python
  # A queryset
      queryset= {
        Model.objects.prefetch_related(
        "b_model_set",
        "c_model"
        )}
  
  from django.db.models import Prefetch
  
  # B queryset
    queryset ={
        Model.objects.
        prefetch_related{
        Prefatch(to_attr="b_model_set", queryset=BModel.objects.all()),
        Prefatch(to_attr="c_models", queryset=CModel.objects.all()),
        )
  ```
* 외래키에 대한 필터 뒤에 prefatch_related()를 사용하면 추가 쿼리가 발생. 웬만해서는 prfetch를 먼저하고 filter를 사용
