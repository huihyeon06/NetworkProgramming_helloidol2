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
      2. python manage.py makemigrations 먼작귀
      3. python manage.py migrate 먼작귀