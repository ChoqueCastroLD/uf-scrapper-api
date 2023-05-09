import datetime
import unittest
from unittest.mock import patch
from api.uf.uf_service import get_uf_value
from api.util.parse_date import parse_date
from api.error_handling.errors import BadRequestError, NotFoundError


class UFServiceTestCase(unittest.TestCase):
    def test_get_uf_value_valid_date(self):
        # Mock the response from the external API
        mock_response = """
        <!doctype html>
        <html lang="es">
        <body>
            <div class='meses' id='mes_all'>
                <div class='table-responsive'>
                    <table>
                        <thead>
                            <tr></tr>
                        </thead>
                        <tbody>
                            <tr>
                                <th style='text-align:center;'>1</th>
                                <td style='text-align:right;'>1.234,56</td>
                                <td style='text-align:right;'>&nbsp;</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </body>
        </html>
        """
        with patch('requests.get') as mock_get:
            mock_get.return_value.content = mock_response.encode('utf-8')

            date = datetime.datetime(2023, 1, 1)
            uf_value = get_uf_value(date)

            self.assertEqual(uf_value, 1234.56)

    def test_get_uf_value_not_found(self):
        # Mock the response from the external API
        mock_response = """
            <!doctype html>
            <html lang="es">
            ...
            </html>
        """
        with patch('requests.get') as mock_get:
            mock_get.return_value.content = mock_response.encode('utf-8')

            date = datetime.datetime(2023, 5, 15)
            with self.assertRaises(NotFoundError):
                get_uf_value(date)

    def test_parse_date_valid_date(self):
        date_str = "10-05-2023"
        date = parse_date(date_str)
        expected_date = datetime.datetime(2023, 5, 10)
        self.assertEqual(date, expected_date)

    def test_parse_date_invalid_date(self):
        date_str = "2023-05-10"
        with self.assertRaises(BadRequestError):
            parse_date(date_str)

if __name__ == '__main__':
    unittest.main()
