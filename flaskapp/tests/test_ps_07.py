# Copyright © 2023, Indiana University
# BSD 3-Clause License

"""
Tests for Practice Set 07: Pet Name Ideation
"""

import re
from unittest import TestCase
from unittest import main as unittest_main
from flaskapp.app import app

app.testing = True



class PS_07_02_TemplateContent(TestCase):
    def test_template_contains_an_h1_tag(self):
        with app.test_client() as client:
            self.assertIn(
                b"<h1",
                client.get("/name-ideator/").data,
                "`templates/name-ideator.html` should contain an <h1> tag, so `/name-ideator/` should too"
            )

    def test_template_contains_a_ul_tag(self):
        with app.test_client() as client:
            self.assertIn(
                b"<ul",
                client.get("/name-ideator/").data,
                "`templates/name-ideator.html` should contain a <ul> tag, so `/name-ideator/` should too"
            )

    def test_template_contains_an_li_tag(self):
        with app.test_client() as client:
            self.assertIn(
                b"<li",
                client.get("/name-ideator/").data,
                "`templates/name-ideator.html` should contain an <li> tag, so `/name-ideator/` should too"
            )



class PS_07_03_Routes(TestCase):
    def test_name_ideator_responds_200_status(self):
        with app.test_client() as client:
            self.assertEqual(client.get("/name-ideator/").status_code, 200)

    def test_name_ideator_either_200_status(self):
        with app.test_client() as client:
            self.assertEqual(client.get("/name-ideator/either/").status_code, 200)

    def test_name_ideator_male_200_status(self):
        with app.test_client() as client:
            self.assertEqual(client.get("/name-ideator/male/").status_code, 200)

    def test_name_ideator_female_200_status(self):
        with app.test_client() as client:
            self.assertEqual(client.get("/name-ideator/female/").status_code, 200)

    def test_name_ideator_either_5_200_status(self):
        with app.test_client() as client:
            self.assertEqual(client.get("/name-ideator/either/5/").status_code, 200)

    def test_name_ideator_male_5_200_status(self):
        with app.test_client() as client:
            self.assertEqual(client.get("/name-ideator/male/5/").status_code, 200)

    def test_name_ideator_female_5_200_status(self):
        with app.test_client() as client:
            self.assertEqual(client.get("/name-ideator/female/5/").status_code, 200)

    def test_name_ideator_either_10_200_status(self):
        with app.test_client() as client:
            self.assertEqual(client.get("/name-ideator/either/10/").status_code, 200)

    def test_name_ideator_male_10_200_status(self):
        with app.test_client() as client:
            self.assertEqual(client.get("/name-ideator/male/10/").status_code, 200)

    def test_name_ideator_female_10_200_status(self):
        with app.test_client() as client:
            self.assertEqual(client.get("/name-ideator/female/10/").status_code, 200)

class PS_07_04_ErrorHandling(TestCase):
    def test_name_ideator_only_three_cases(self):
        with app.test_client() as client:
            self.assertNotEqual(client.get("/name-ideator/10000/"), 200, "We only plan to handle 'male', 'female', or 'either'. However, a 200 response got returned.")

    def test_cannot_handle_non_integer_numbers(self):
        with app.test_client() as client:
            self.assertNotEqual(client.get("/name-ideator/either/dog/"), 200, "The third parameter must be something we can interpret as an integer")


if __name__ == "__main__":
    unittest_main()
