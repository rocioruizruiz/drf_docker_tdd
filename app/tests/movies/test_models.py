import pytest

from movies.models import Movie


# Pytest-Django takes a conservative approach to enabling database access in your tests.
# You must explicitly request database access via the @pytest.mark.django_db decorator.
@pytest.mark.django_db
def test_movie_model():
    movie = Movie(title="Raising Arizona", genre="comedy", year="1987")
    movie.save()
    assert movie.title == "Raising Arizona"
    assert movie.genre == "comedy"
    assert movie.year == "1987"
    assert movie.created_date
    assert movie.updated_date
    assert str(movie) == movie.title
