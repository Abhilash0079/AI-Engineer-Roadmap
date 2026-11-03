import pytest
from config import load_config

def test_load_config_with_api_key(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key-123")
    config = load_config()

    assert config['api_key'] == "test-key-123"

def test_load_config_without_api_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    with pytest.raises(
        ValueError,
        match="OPENAI_API_KEY is missing"
    ):
        load_config()
