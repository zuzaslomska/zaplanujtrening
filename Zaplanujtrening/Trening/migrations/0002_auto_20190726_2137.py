# Generated by Django 2.2.2 on 2019-07-26 21:37

from django.db import migrations

def fake_trainers(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    MyUser = apps.get_model('Trening', 'MyUser')


    MyUser.objects.create(
        username="karolkrawczyk1",
        first_name="Karol",
        last_name="Krawczyk",
        password="karolek123",
        email="karolkrawczyk@gmail.com",
        about="Praca instruktora jest moją pasją. Wkładam w nią całą swoją energię. Przynosi mi ona wiele radości i satysfakcji, gdyż wiem, że pomagam drugiej osobie. Nie zwlekaj z podjęciem decyzji i zdecyduj się na poprawę swojego życia.",
        trener="True",
        avatar="profile_pics/karolkrawczyk.jpg",
        rating="5.0",
        all_votes="25",
        sum_of_votes="125"
        )


    MyUser.objects.create(
        username="annakopytko90",
        first_name="Anna",
        last_name="Kopytko",
        password="kopytko123",
        email="annakopytko@gmail.com",
        about="Praca instruktora jest moją pasją. Wkładam w nią całą swoją energię. Przynosi mi ona wiele radości i satysfakcji, gdyż wiem, że pomagam drugiej osobie. Nie zwlekaj z podjęciem decyzji i zdecyduj się na poprawę swojego życia.",
        trener="True",
        avatar="profile_pics/aniakopytko.jpg",
        rating="4.5",
        all_votes="2",
        sum_of_votes="9"
    )


    MyUser.objects.create(
        username="pawelpolak",
        first_name="Paweł",
        last_name="Polak",
        password="polaczek123",
        email="pawelpolak@gmail.com",
        about="Praca instruktora jest moją pasją. Wkładam w nią całą swoją energię. Przynosi mi ona wiele radości i satysfakcji, gdyż wiem, że pomagam drugiej osobie. Nie zwlekaj z podjęciem decyzji i zdecyduj się na poprawę swojego życia.",
        trener="True",
        avatar="profile_pics/pawelpolak.jpg",
        rating="3.8",
        all_votes="10",
        sum_of_votes="38"
    )

    MyUser.objects.create(
        username="zaplanujtrening",
        first_name="Zaplanuj",
        last_name="Trening",
        password="Krowisko1",
        email="zaplanujtrening@o2.pl",
        about="Potrzebuję cudu,żeby być chociaż 2/10 ",
        trener="False",
        avatar="profile_pics/zaplanujtrening.jpg",
        rating="0.0",
        all_votes="0",
        sum_of_votes="0"
        )

def rating(apps, schema_editor):
    Rating = apps.get_model('Trening', 'Rating')
    MyUser = apps.get_model('Trening', 'MyUser')

    Rating.objects.create(
        comments="Pan Paweł jest najlepszym instruktorem na świecie",
        user_comment=MyUser.objects.get(pk=1),
    )
    Rating.objects.create(
        comments="Lepiej wyglądam i lepiej się czuję,dzięki!",
        user_comment=MyUser.objects.get(pk=2),
    )
    Rating.objects.create(
        comments="Nie jestem zadowolony,spodziewałem się więcej",
        user_comment=MyUser.objects.get(pk=3),
    )

def parts_of_the_body(apps, schema_editor):
    Parts = apps.get_model('Trening', 'Parts')

    Parts.objects.create(part="mięsień naramienny")
    Parts.objects.create(part="mięsień czworoboczny")
    Parts.objects.create(part="mięsień piersiowy większy")
    Parts.objects.create(part="mięsień podgrzebieniowy")
    Parts.objects.create(part="biceps")
    Parts.objects.create(part="mięsień trójgłowy ramienia")
    Parts.objects.create(part="mięśnie najszerszy grzbietu")
    Parts.objects.create(part="mięśnie skośne brzucha")
    Parts.objects.create(part="powięź piersiowo-lędźwiowa")
    Parts.objects.create(part="mięśnie proste brzucha")
    Parts.objects.create(part="mięsień pośladowy wielki")
    Parts.objects.create(part="mięsień czworogłowy uda")
    Parts.objects.create(part="mięśnie dwugłowe uda")
    Parts.objects.create(part="mięsień piszczelowy przedni")
    Parts.objects.create(part="mięsień łydki")

def exercises(apps, schema_editor):
    Exercises = apps.get_model('Trening', 'Exercises')
    Parts = apps.get_model('Trening', 'Parts')

    Exercises.objects.create(
        exercise_name="plank",
        description="""Przyjmij pozycję deski, tzn. nogi wyprostowane, łokcie znajdują się pod linią barków a wzrok skierowany w dół. Ciało znajduje się w linii prostej.
                        Złącz dłonie w pięść, mocno zaciśnij i napnij ramiona i barki tak, jakbyś chciał odwieść ramiona do zewnątrz
                        Trzymając nogi złączone, napnij mięśnie czworogłowe (z przodu) uda i pośladki
                        Wyobraź sobie, jakbyś chciał złączyć łokcie z palcami u stóp""",
        gif="profile_pics/plank.jpg",
        part=Parts.objects.get(pk=10),
    )

    Exercises.objects.create(
        exercise_name="brzuszki",
        description="""Należy położyć się na podłodze z nogami na ziemi. 
        Ćwiczenie wykonuje się najczęściej z rękami splecionymi za głową, unosząc plecy i robiąc skłon w przód spinając mięśnie brzucha do dotknięcia łokciami kolan""",
        gif="profile_pics/brzuszki.jpg",
        part=Parts.objects.get(pk=10),
    )

    Exercises.objects.create(
        exercise_name="pompka",
        description="Wykonuje się je w pozycji poziomej, twarzą do ziemi. Polega na podnoszeniu i obniżaniu tułowia.",
        gif="profile_pics/pompki.gif",
        part=Parts.objects.get(pk=3),
    )

class Migration(migrations.Migration):

    dependencies = [
        ('Trening', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fake_trainers),
        migrations.RunPython(rating),
        migrations.RunPython(parts_of_the_body),
        migrations.RunPython(exercises),
    ]
