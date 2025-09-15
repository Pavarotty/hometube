"""
Simplified and robust pytest configuration.
"""

import pytest
import sys
from pathlib import Path
from unittest.mock import MagicMock

# === MOCK STREAMLIT AT IMPORT TIME ===
# Ensure streamlit is not already loaded
if "streamlit" in sys.modules:
    del sys.modules["streamlit"]

# Create a complete mock
mock_st = MagicMock()

# Simple session_state mock that accepts everything
mock_session_state = MagicMock()
mock_session_state.__contains__ = MagicMock(return_value=False)
mock_st.session_state = mock_session_state

# Mock main functions
mock_st.title = MagicMock(return_value=None)
mock_st.write = MagicMock(return_value=None)
mock_st.text_input = MagicMock(return_value="")
mock_st.button = MagicMock(return_value=False)
mock_st.selectbox = MagicMock(return_value="")
mock_st.checkbox = MagicMock(return_value=False)
mock_st.error = MagicMock(return_value=None)
mock_st.success = MagicMock(return_value=None)
mock_st.warning = MagicMock(return_value=None)
mock_st.info = MagicMock(return_value=None)
mock_st.empty = MagicMock()
mock_st.container = MagicMock()
# FIX: st.columns must return exactly 2 columns
mock_col1, mock_col2 = MagicMock(), MagicMock()
mock_st.columns = MagicMock(return_value=[mock_col1, mock_col2])
mock_st.set_page_config = MagicMock(return_value=None)
mock_st.markdown = MagicMock(return_value=None)

# Install the mock IMMEDIATELY
sys.modules["streamlit"] = mock_st


def pytest_configure(config):
    """Global test configuration."""
    print("\n🧪 Starting HomeTube tests (simplified version)")


def pytest_unconfigure(config):
    """Cleanup after tests."""
    print("\n✅ Tests completed")


@pytest.fixture(scope="session")
def project_root():
    """Project root directory."""
    return Path(__file__).parent.parent


@pytest.fixture(scope="session")
def temp_dir(tmp_path_factory):
    """Temporary directory for tests."""
    return tmp_path_factory.mktemp("hometube_tests")


@pytest.fixture
def mock_streamlit():
    """Simple and robust Streamlit mock."""
    return sys.modules.get("streamlit", MagicMock())
