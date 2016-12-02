import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db
from datetime import datetime


class TestFlutt:
    def test_flutt_creation(self):
        flutt = mixer.blend('flutz.Flutt', body='Llamas')
        assert flutt.id == 1, 'Should save an instance'

    def test_get_exerpt_method_works_good(self):
        flutt = mixer.blend('flutz.Flutt', body="They're good dogs brent.")
        result = flutt.get_exerpt(10)
        expected = "They're go"
        assert result == expected, "Should return first 10 chars only."

    def test_fake_flutt_has_good_str_method(self):
        good_person = mixer.blend('accounts.Member', phone_number='+18456331959')
        flutt = mixer.blend('flutz.Flutt', member=good_person)
        result= "{1} {0}".format(flutt.created, '+18456331959')
        assert str(flutt) == result, 'Something wonderful is happening'
        assert flutt.created < datetime.now(), 'Flutt must be created in the past'
