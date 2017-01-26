import unittest;
from statuscheck import functions;

class Test(unittest.TestCase):
    """Unit tests for googlemaps."""

    def test_check_google_analytics(self):
        """Test statuscheck check_google_analytics()."""
        self.assertEqual(functions.check_google_analytics("http://google.com"),False);
        # self.assertEqual(functions.check_google_analytics("http://joehaaga.xyz"),True);
        self.assertEqual(functions.check_google_analytics("http://politico.com/pro"),False);
        self.assertEqual(functions.check_google_analytics("http://ligado.com"),True);

if __name__ == "__main__":
    unittest.main()