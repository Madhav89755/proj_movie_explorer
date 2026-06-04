import random
from datetime import date

from django.core.management.base import BaseCommand
from app_movie.models import Movie, Genre, Staff


class Command(BaseCommand):
    help = "Populates the database with initial sample data"

    def add_arguments(self, parser):
        parser.add_argument(
            "--movies",
            type=int,
            default=25,
            help="Number of movies to create. Default is 25.",
        )
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete existing data before seeding.",
        )

    def handle(self, *args, **options):
        movie_count = max(options["movies"], 1)
        clear_existing = options["clear"]

        if clear_existing:
            Movie.objects.all().delete()
            Genre.objects.all().delete()
            Staff.objects.all().delete()
            self.stdout.write(self.style.WARNING("Existing movie data removed."))

        genre_names = [
            "Action",
            "Adventure",
            "Animation",
            "Comedy",
            "Crime",
            "Drama",
            "Fantasy",
            "Horror",
            "Mystery",
            "Romance",
            "Sci-Fi",
            "Thriller",
        ]

        staff_names = [
            "Christopher Nolan",
            "Greta Gerwig",
            "Denis Villeneuve",
            "Sofia Coppola",
            "Jordan Peele",
            "Emma Stone",
            "Ryan Gosling",
            "Margot Robbie",
            "Timothee Chalamet",
            "Zendaya",
            "Florence Pugh",
            "Cillian Murphy",
            "Anya Taylor-Joy",
            "Pedro Pascal",
            "Lupita Nyong'o",
            "Oscar Isaac",
            "Robert Pattinson",
            "Saoirse Ronan",
            "Rami Malek",
            "Carey Mulligan",
            "Michael B. Jordan",
            "Viola Davis",
            "Dev Patel",
            "Gal Gadot",
            "Paul Mescal",
            "Ayo Edebiri",
            "Jacob Elordi",
            "Lakeith Stanfield",
            "Naomie Harris",
            "Andrew Garfield",
        ]

        title_adjectives = [
            "Hidden",
            "Last",
            "Silent",
            "Golden",
            "Broken",
            "Infinite",
            "Midnight",
            "Burning",
            "Shattered",
            "Emerald",
            "Neon",
            "Fading",
            "Electric",
            "Lost",
            "Crimson",
        ]
        title_nouns = [
            "Horizon",
            "Memory",
            "Empire",
            "Voyage",
            "Labyrinth",
            "Echo",
            "Reckoning",
            "Whisper",
            "Skyline",
            "Odyssey",
            "Pulse",
            "Signal",
            "Mirage",
            "Legacy",
            "Frontier",
        ]

        genres = [
            Genre.objects.get_or_create(name=name)[0]
            for name in genre_names
        ]
        staff_members = [
            Staff.objects.get_or_create(name=name)[0]
            for name in staff_names
        ]

        existing_titles = set(Movie.objects.values_list("title", flat=True))
        created_movies = 0

        for idx in range(movie_count):
            title = f"{random.choice(title_adjectives)} {random.choice(title_nouns)}"
            if title in existing_titles:
                title = f"{title} {idx + 1}"

            release_year = random.randint(1990, 2026)
            release_date = date(
                release_year,
                random.randint(1, 12),
                random.randint(1, 28),
            )

            director = random.choice(staff_members)

            movie = Movie.objects.create(
                title=title,
                release_date=release_date,
                director=director,
            )

            movie_genres = random.sample(genres, k=random.randint(1, 3))
            movie.genre.set(movie_genres)

            actor_pool = [member for member in staff_members if member.id != director.id]
            cast_size = min(len(actor_pool), random.randint(2, 6))
            movie_actors = random.sample(actor_pool, k=cast_size)
            movie.actors.set(movie_actors)

            existing_titles.add(title)
            created_movies += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Database population completed! Created {created_movies} movies, "
                f"{len(genres)} genres, and {len(staff_members)} staff members."
            )
        )
