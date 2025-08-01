import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from my_first_db.models import Actor, Genre


def main() -> QuerySet:
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    
    genres = ["Western", "Action", "Dramma"]

    for actors_name, actors_surname in actors:
        Actor.objects.create(
            first_name = actors_name,
            last_name = actors_surname
        )

    for genre in genres:
        Genre.objects.create(
            name = genre
        )

    Genre.objects.filter(
        name="Dramma",
    ).update(name="Drama")
    
    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(last_name="Clooney")

    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(
        name="Action"
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")


if __name__ == "__main__":
    main()

