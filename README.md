# helloidol2

---

1. startproject helloidlo2
   1. python -m pip install django~=4.2
   2. django-admin startproject helloidol2 .
   3. File > Settings... > Language & Frameworks > Django > 
      [v] Enable Django Support
   4. Run > Edit Configurations... > + > Django Server > Name : runserver
   5. VCS > Enable Version Control Intergration... > git > ok
2. startapp 먼작귀
   1. python manage.py startapp 먼작귀
   2. '먼작귀', in INSTALLED_APPS settings.py
3. 먼작귀/
   1. models
      1. Character
         1. name, feature, created_at, updated_at
         2. `__str__()`: 객체를 출력할 때, 알맞은 string으로 출력하자
         3. `get_absolute_url()`: 캐릭터 하나 데이터 가져오자
      2. python manage.py makemigrations 먼작귀
      3. python manage.py migrate 먼작귀
   2. admin
      1. Character
      2. python manage.py createsuperuser
   3. views
      1. R : CharacterListView
      2. R : CharacterDetailView
   4. templates/먼작귀/
      1. character_list.html
      2. character_detail.html
   5. urls
      1. 먼작귀 : character_list
      2. 먼작귀 : character_detail
4. templates/
   1. base.html
      1. settings.py > TEMPLATES
         1. 'DIRS':[BASE_DIR/'templates']