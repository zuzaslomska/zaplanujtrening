# Zaplanuj Trening

"Zaplanuj Trening" korzysta z frameworku Django oraz systemu zarządzania bazami danych PostgreSQL.
Projekt zawiera aplikację "Trening", która jest dedykowana osobom chcącym zmienić swój styl życia.
Projekt posiada 3 rodzaje użytkowników: 
1. niezalogowany użytkownik 
2. użytkownik posiadający konto w serwisie - po zalogowaniu może korzystać z porad trenerów personalnych i edycji konta.
3. użytkownik "Trener" - może układac plany ćwiczeń oraz wszystko,co użytkownik posiadający konto w serwisie.

## Przed uruchomieniem
Przed uruchomieniem projektu w systemie PostgreSQL należy utworzyć bazę danych "zaplanujtrening", a następnie:
1. zainstalować wymagane pakiety: pip3 install -r requirements.txt
2. przeprowadzić migracje: python3 manage.py makemigrations/migrate
4. uruchomić serwer: python3 manage.py runserver
