"""Статистика каталога фильмов без сторонних библиотек."""

import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movies):
    """Вернуть средний рейтинг с одним знаком после запятой."""
    if not movies:
        return 0.0
    return round(sum(movie["rating"] for movie in movies) / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    """Вернуть максимальный, минимальный и средний возраст фильмов."""
    if not movies:
        return (0, 0, 0)
    ages = [current_year - movie["year"] for movie in movies]
    return (max(ages), min(ages), math.ceil(sum(ages) / len(ages)))


def duration_in_hours(minutes):
    """Перевести минуты в часы и остаток минут."""
    return f"{minutes // 60}ч {minutes % 60}м"


def rating_tier(rating):
    """Определить категорию рейтинга."""
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    """Определить категорию года выпуска через match."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


def print_non_comedies(movies):
    """Вывести названия фильмов, кроме комедий."""
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def print_first_masterpiece(movies):
    """Найти первый фильм с рейтингом строго выше девяти."""
    index = 0
    while index < len(movies):
        if movies[index]["rating"] > 9.0:
            print(movies[index]["title"])
            break
        index += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    """Посчитать фильмы длиннее указанного порога."""
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


def normalize_title(title):
    """Сделать первую букву каждого слова заглавной вручную."""
    words = title.split()
    return " ".join(word[0].upper() + word[1:] for word in words)


def make_slug(title):
    """Подготовить название для ссылки."""
    return normalize_title(title).lower().replace(" ", "-")


def format_report_line(movie):
    """Собрать описание фильма в одну строку."""
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, '
        f"{duration}, жанры: {genres}"
    )


def titles_sorted_by_rating(movies):
    """Вернуть названия по убыванию рейтинга, не меняя каталог."""
    ordered = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in ordered]


def top_n_by_rating(movies, n=3):
    """Вернуть первые n пар (название, рейтинг)."""
    ordered = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in ordered[: max(n, 0)]]


def count_by_genre(movies):
    """Посчитать фильмы по жанрам через dict.get."""
    counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(movies):
    """Собрать список фильмов каждого актёра."""
    actors = {}
    for movie in movies:
        for actor in movie["actors"]:
            actors.setdefault(actor, []).append(movie["title"])
    return actors


def above_average_ratings(movies):
    """Отобрать фильмы выше среднего рейтинга генератором словаря."""
    average = average_rating(movies)
    return {
        movie["title"]: movie["rating"] for movie in movies if movie["rating"] > average
    }


def all_genres(movies):
    """Собрать все жанры объединением множеств."""
    genres = set()
    for movie in movies:
        genres.update(movie["genres"])
    return genres


def common_actors(movie1, movie2):
    """Найти актёров, снявшихся в обоих фильмах."""
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    """Найти жанры первого каталога, отсутствующие во втором."""
    return all_genres(movies_a) - all_genres(movies_b)


def iter_high_rated(movies, min_rating=8.0):
    """Выдавать подходящие фильмы по одному."""
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def total_high_rated_duration(movies):
    """Сложить длительность фильмов с рейтингом строго выше семи."""
    return sum(movie["duration_min"] for movie in movies if movie["rating"] > 7)


def build_report(movies):
    """Вывести основной отчёт и демонстрацию остальных этапов."""
    print("ОТЧЁТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {catalog_age_stats(movies)[2]} лет")
    print("\nТоп-3 фильма:")
    for movie in sorted(movies, key=lambda movie: movie["rating"], reverse=True)[:3]:
        print(f"  {format_report_line(movie)}")
    print("\nФильмов по жанрам:")
    counts = count_by_genre(movies)
    for genre, count in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
        print(f"  {genre} — {count}")
    print("\nВсе жанры каталога: " + ", ".join(sorted(all_genres(movies))))
    print("\nФильмы без комедий:")
    print_non_comedies(movies)
    print("\nПервый фильм с рейтингом выше 9:")
    print_first_masterpiece(movies)
    print(f"Фильмов длиннее 120 минут: {count_long_movies(movies)}")
    print("\nКатегории и ссылки:")
    for movie in movies:
        print(
            f"{make_slug(movie['title'])}: {rating_tier(movie['rating'])}, "
            f"{decade_label(movie['year'])}"
        )
    print("\nНазвания по рейтингу:", titles_sorted_by_rating(movies))
    print("Топ в виде кортежей:", top_n_by_rating(movies))
    print("Выше среднего:", above_average_ratings(movies))
    print("\nФильмографии:")
    for actor, titles in sorted(actor_filmography(movies).items()):
        print(f"{actor}: {', '.join(titles)}")
    if len(movies) >= 2:
        print("Общие актёры первых двух:", sorted(common_actors(*movies[:2])))
        print(
            "Жанры только первого:", sorted(genres_only_in_one(movies[:1], movies[1:]))
        )
    print("\nФильмы с рейтингом не ниже 8:")
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))
    print(f"Длительность фильмов с рейтингом > 7: {total_high_rated_duration(movies)}")


if __name__ == "__main__":
    build_report(movies)
