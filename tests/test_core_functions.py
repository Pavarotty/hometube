"""
Simplified tests for HomeTube main functions.
Focus on non-regression with essential tests.
"""

import tempfile
from pathlib import Path


class TestCoreFunctions:
    """Main utility function tests."""

    def test_sanitize_filename(self):
        """Test sanitize_filename function."""
        from app.utils import sanitize_filename

        # Normal cases
        assert sanitize_filename("normal_file.txt") == "normal_file.txt"
        assert sanitize_filename("file with spaces.mp4") == "file with spaces.mp4"

        # Forbidden characters
        assert sanitize_filename('file<>:"/\\|?*.txt') == "file_________.txt"

        # Edge cases
        assert sanitize_filename("") == ""
        assert (
            sanitize_filename("   ") == "unnamed"
        )  # Function returns "unnamed" for spaces
        assert sanitize_filename("...") == "unnamed"

    def test_parse_time_like(self):
        """Test parse_time_like function."""
        from app.utils import parse_time_like

        # Simple formats
        assert parse_time_like("60") == 60
        assert parse_time_like("1:30") == 90
        assert parse_time_like("1:23:45") == 5025

        # Edge cases
        assert parse_time_like("") == 0
        assert parse_time_like("invalid") == 0

        # Spaces
        assert parse_time_like("  1:30  ") == 90

    def test_fmt_hhmmss(self):
        """Test fmt_hhmmss function."""
        from app.utils import fmt_hhmmss

        assert fmt_hhmmss(0) == "00:00:00"
        assert fmt_hhmmss(60) == "00:01:00"
        assert fmt_hhmmss(3661) == "01:01:01"
        assert fmt_hhmmss(-1) == "00:00:00"

    def test_is_valid_browser(self):
        """Test is_valid_browser function."""
        from app.utils import is_valid_browser

        # Valid browsers
        assert is_valid_browser("chrome") is True
        assert is_valid_browser("firefox") is True
        assert is_valid_browser("CHROME") is True  # Case insensitive

        # Invalid browsers
        assert is_valid_browser("invalid") is False
        assert is_valid_browser("") is False
        assert is_valid_browser("   ") is False

    def test_extract_resolution_value(self):
        """Test extract_resolution_value function."""
        from app.utils import extract_resolution_value

        assert extract_resolution_value("720p") == 720
        assert extract_resolution_value("1080") == 1080
        assert extract_resolution_value("4K") == 4
        assert extract_resolution_value("") == 0
        assert extract_resolution_value("invalid") == 0

    def test_video_id_from_url(self):
        """Test video_id_from_url function."""
        from app.utils import video_id_from_url

        # Valid YouTube URLs
        assert (
            video_id_from_url("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            == "dQw4w9WgXcQ"
        )
        assert video_id_from_url("https://youtu.be/dQw4w9WgXcQ") == "dQw4w9WgXcQ"

        # Invalid URLs
        assert video_id_from_url("") is None
        assert video_id_from_url("https://example.com") is None

    def test_sanitize_url(self):
        """Test sanitize_url function."""
        from app.utils import sanitize_url

        assert sanitize_url("example.com") == "https://example.com"
        assert sanitize_url("https://example.com") == "https://example.com"
        assert sanitize_url("") == ""
        assert sanitize_url("   example.com   ") == "https://example.com"

    def test_invert_segments_basic(self):
        """Basic test of invert_segments function."""
        from app.utils import invert_segments

        # Simple test
        segments = [(10, 20), (30, 40)]
        result = invert_segments(segments, 50)
        expected = [(0, 10), (20, 30), (40, 50)]
        assert result == expected

        # Contiguous segments
        segments = [(0, 10), (10, 20)]
        result = invert_segments(segments, 30)
        expected = [(20, 30)]
        assert result == expected

    def test_invert_segments_empty(self):
        """Test invert_segments with edge cases."""
        from app.utils import invert_segments

        # Empty list
        assert invert_segments([], 100) == [(0, 100)]

        # Zero duration
        assert invert_segments([(10, 20)], 0) == []

    def test_is_valid_cookie_file(self):
        """Test is_valid_cookie_file function."""
        from app.utils import is_valid_cookie_file

        # Basic cases
        assert is_valid_cookie_file("") is False
        assert is_valid_cookie_file("/nonexistent/file.txt") is False

        # Test with temporary file
        with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as tmp:
            tmp.write(b"# Cookie file content")
            tmp.flush()
            assert is_valid_cookie_file(tmp.name) is True

        # Cleanup
        Path(tmp.name).unlink(missing_ok=True)
