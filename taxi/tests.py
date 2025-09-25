from django.test import TestCase
from taxi.models import Driver, Manufacturer
from taxi.forms import DriverCreationForm, DriverLicenseUpdateForm


class FormTests(TestCase):
    def test_driver_creation_form_with_valid_data(self):
        """Test driver creation form with valid data"""
        form_data = {
            "username": "newdriver",
            "first_name": "Jane",
            "last_name": "Smith",
            "license_number": "XYZ98765",
            "password1": "testpassword123",
            "password2": "testpassword123",
        }
        form = DriverCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_driver_creation_form_with_invalid_license(self):
        """Test driver creation form with invalid license number"""
        form_data = {
            "username": "newdriver",
            "first_name": "Jane",
            "last_name": "Smith",
            "license_number": "invalid",  # Invalid format
            "password1": "testpassword123",
            "password2": "testpassword123",
        }
        form = DriverCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("license_number", form.errors)

    def test_driver_license_update_form_valid(self):
        """Test driver license update form with valid data"""
        driver = Driver.objects.create_user(
            username="testuser",
            password="testpass",
            license_number="OLD12345"
        )
        form_data = {"license_number": "NEW98765"}
        form = DriverLicenseUpdateForm(data=form_data, instance=driver)
        self.assertTrue(form.is_valid())


class ModelTests(TestCase):
    def setUp(self):
        self.manufacturer = Manufacturer.objects.create(
            name="Toyota",
            country="Japan"
        )
        self.driver = Driver.objects.create_user(
            username="testdriver",
            password="testpass123",
            license_number="ABC12345"
        )

    def test_manufacturer_str_method(self):
        """Test manufacturer string representation"""
        self.assertEqual(str(self.manufacturer), "Toyota Japan")

    def test_driver_str_method(self):
        """Test driver string representation"""
        self.assertEqual(str(self.driver), "testdriver ( )")
