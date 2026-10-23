"""Контрольные ответы, граничные случаи и ограничения задания."""

import ast
import copy
import inspect
import io
import unittest
from contextlib import redirect_stdout

import catalog_analysis as catalog


class CatalogTests(unittest.TestCase):
    def test_statistics(self):
        self.assertEqual(catalog.average_rating(catalog.movies), 7.2)
        self.assertEqual(catalog.catalog_age_stats(catalog.movies), (15, 2, 8))
        self.assertEqual(catalog.duration_in_hours(155), "2ч 35м")
        self.assertEqual(catalog.total_high_rated_duration(catalog.movies), 713)
        self.assertEqual(catalog.count_long_movies(catalog.movies), 4)

    def test_boundaries(self):
        for rating, expected in [
            (4.9, "слабо"),
            (5, "средне"),
            (7, "хорошо"),
            (8.99, "хорошо"),
            (9, "шедевр"),
        ]:
            self.assertEqual(catalog.rating_tier(rating), expected)
        for year, expected in [
            (2014, "старые"),
            (2015, "недавние"),
            (2020, "недавние"),
            (2021, "новые"),
        ]:
            self.assertEqual(catalog.decade_label(year), expected)

    def test_top_and_original_data(self):
        original = copy.deepcopy(catalog.movies)
        self.assertEqual(
            catalog.top_n_by_rating(catalog.movies),
            [
                ("The Quiet Algorithm", 9.2),
                ("midnight in oslo", 8.9),
                ("The Dune Chronicles", 8.6),
            ],
        )
        catalog.titles_sorted_by_rating(catalog.movies)
        self.assertEqual(catalog.movies, original)

    def test_strings_and_sets(self):
        self.assertEqual(catalog.normalize_title("  silent  hours "), "Silent Hours")
        self.assertEqual(catalog.make_slug("Silent Hours"), "silent-hours")
        self.assertEqual(
            catalog.common_actors(catalog.movies[0], catalog.movies[3]), {"O. Isaac"}
        )
        self.assertEqual(
            catalog.genres_only_in_one(catalog.movies[5:6], catalog.movies[:5]),
            {"mystery"},
        )
        self.assertEqual(
            catalog.count_by_genre(catalog.movies),
            {
                "drama": 5,
                "sci-fi": 3,
                "comedy": 3,
                "thriller": 3,
                "action": 2,
                "mystery": 1,
            },
        )

    def test_empty_and_no_masterpiece(self):
        self.assertEqual(catalog.catalog_age_stats([]), (0, 0, 0))
        self.assertEqual(catalog.top_n_by_rating([], 3), [])
        output = io.StringIO()
        with redirect_stdout(output):
            catalog.print_first_masterpiece([])
        self.assertIn("Шедевров не найдено", output.getvalue())
        self.assertEqual(
            list(catalog.iter_high_rated(catalog.movies, 9)), [catalog.movies[7]]
        )

    def test_required_language_features(self):
        requirements = [
            (catalog.rating_tier, ast.IfExp),
            (catalog.decade_label, ast.Match),
            (catalog.print_non_comedies, ast.Continue),
            (catalog.print_first_masterpiece, ast.Break),
            (catalog.above_average_ratings, ast.DictComp),
            (catalog.iter_high_rated, ast.Yield),
            (catalog.total_high_rated_duration, ast.GeneratorExp),
        ]
        for function, node_type in requirements:
            tree = ast.parse(inspect.getsource(function))
            self.assertTrue(
                any(isinstance(node, node_type) for node in ast.walk(tree)),
                function.__name__,
            )


if __name__ == "__main__":
    unittest.main()
