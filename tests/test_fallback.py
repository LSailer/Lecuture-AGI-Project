import pytest

from src.utils.fallback import FallbackModel

DEFAULT_CONFIG = {}

DEFAULT_SYSTEM = "default system prompt"
DEFAULT_USER = "default user prompt"

FAILED_PREDICTIONS = [
    {"agent_id": "agent-1", "action": "UP", "state": "[1,2,3]", "error": "invalid move"},
    {"agent_id": "agent-2", "action": "DOWN", "state": "[3,2,1]", "error": "out of bounds"},
]


@pytest.fixture
def model():
    return FallbackModel(DEFAULT_CONFIG)


# --- _parse_response ---

def test_parse_both_tags(model):
    response = "<SYSTEM_PROMPT>new sys</SYSTEM_PROMPT>\n<USER_PROMPT>new usr</USER_PROMPT>"
    sys, usr = model._parse_response(response, DEFAULT_SYSTEM, DEFAULT_USER)
    assert sys == "new sys"
    assert usr == "new usr"


def test_parse_only_system_tag(model):
    response = "<SYSTEM_PROMPT>only sys</SYSTEM_PROMPT>"
    sys, usr = model._parse_response(response, DEFAULT_SYSTEM, DEFAULT_USER)
    assert sys == "only sys"
    assert usr == DEFAULT_USER


def test_parse_only_user_tag(model):
    response = "<USER_PROMPT>only usr</USER_PROMPT>"
    sys, usr = model._parse_response(response, DEFAULT_SYSTEM, DEFAULT_USER)
    assert sys == DEFAULT_SYSTEM
    assert usr == "only usr"


def test_parse_no_tags(model):
    response = "no tags here at all"
    sys, usr = model._parse_response(response, DEFAULT_SYSTEM, DEFAULT_USER)
    assert sys == DEFAULT_SYSTEM
    assert usr == DEFAULT_USER


# --- _build_meta_prompt ---

def test_meta_prompt_contains_system_section(model):
    result = model._build_meta_prompt(DEFAULT_SYSTEM, DEFAULT_USER, FAILED_PREDICTIONS)
    assert "## Original System Prompt" in result
    assert DEFAULT_SYSTEM in result


def test_meta_prompt_contains_user_section(model):
    result = model._build_meta_prompt(DEFAULT_SYSTEM, DEFAULT_USER, FAILED_PREDICTIONS)
    assert "## Original User Prompt" in result
    assert DEFAULT_USER in result


def test_meta_prompt_contains_failures_section(model):
    result = model._build_meta_prompt(DEFAULT_SYSTEM, DEFAULT_USER, FAILED_PREDICTIONS)
    assert "## Failed Predictions" in result


def test_meta_prompt_contains_agent_info(model):
    result = model._build_meta_prompt(DEFAULT_SYSTEM, DEFAULT_USER, FAILED_PREDICTIONS)
    assert "agent-1" in result
    assert "agent-2" in result
    assert "invalid move" in result
    assert "out of bounds" in result
