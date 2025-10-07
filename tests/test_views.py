import pytest
from django.test import TestCase
from unittest.mock import patch, MagicMock
import os
from config import get_telegram_bot_token, _read_config_parameter


class ConfigTest(TestCase):
    """Test cases for configuration functionality."""

    @pytest.mark.timeout(30)
    def test_read_config_parameter_from_env(self):
        """
        Test that _read_config_parameter reads from environment variables.
        """
        with patch.dict(os.environ, {'TEST_PARAM': 'test_value'}):
            result = _read_config_parameter('TEST_PARAM')
            self.assertEqual(result, 'test_value')

    @pytest.mark.timeout(30)
    def test_read_config_parameter_case_insensitive(self):
        """
        Test that _read_config_parameter is case insensitive.
        """
        with patch.dict(os.environ, {'TEST_PARAM': 'test_value'}):
            result = _read_config_parameter('test_param')
            self.assertEqual(result, 'test_value')

    @pytest.mark.timeout(30)
    def test_get_telegram_bot_token_raises_error_when_missing(self):
        """
        Test that get_telegram_bot_token raises ValueError when token is missing.
        """
        with patch('config._read_config_parameter', return_value=None):
            with self.assertRaises(ValueError) as context:
                get_telegram_bot_token()
            self.assertIn("TELEGRAM_BOT_TOKEN is required", str(context.exception))

    @pytest.mark.timeout(30)
    def test_get_telegram_bot_token_returns_token_when_available(self):
        """
        Test that get_telegram_bot_token returns token when available.
        """
        with patch('config._read_config_parameter', return_value='test_token'):
            result = get_telegram_bot_token()
            self.assertEqual(result, 'test_token')