import pytest
import json
import os
import shutil
from pathlib import Path
from namo_nexus.evolution.episode_logger import EpisodeLogger
from namo_nexus.api.schemas import ChatRequest

def test_episode_logger_flush(tmp_path):
    # Setup
    logger = EpisodeLogger()
    # Override log file path to a temp file for testing
    log_file = tmp_path / "episodes.jsonl"
    logger._log_file = log_file

    request = ChatRequest(user_id="u1", session_id="s1", message="hello")

    # Action
    logger.log_event(
        trace_id="t1",
        request=request,
        reply="hi",
        emotion={"joy": 0.5},
        dharma={"principle": "truth"},
        safety={"safe": True},
        latency_ms=100
    )

    # Verification
    assert log_file.exists()

    with open(log_file, "r") as f:
        lines = f.readlines()
        assert len(lines) == 1
        data = json.loads(lines[0])
        assert data["trace_id"] == "t1"
        assert data["user_id"] == "u1"

def test_episode_logger_creates_directory(tmp_path):
    # Setup: define a log file in a nested directory that doesn't exist
    log_dir = tmp_path / "subdir" / "logs"
    log_file = log_dir / "episodes.jsonl"

    # Ensure dir doesn't exist
    if log_dir.exists():
        shutil.rmtree(log_dir)

    logger = EpisodeLogger()
    logger._log_file = log_file

    request = ChatRequest(user_id="u1", session_id="s1", message="hello")

    # Action: log event, which triggers flush, which checks dir
    logger.log_event("t1", request, "r", {}, {}, {}, 10)

    # Verification
    assert log_dir.exists()
    assert log_file.exists()

def test_episode_logger_clears_buffer_on_error(tmp_path):
    logger = EpisodeLogger()
    log_file = tmp_path / "readonly" / "episodes.jsonl"
    logger._log_file = log_file

    # Create directory and make it read-only to force error?
    # Or just mock open?
    # Easier: pass a directory as file path
    logger._log_file = tmp_path # Can't open dir for writing

    request = ChatRequest(user_id="u1", session_id="s1", message="hello")

    # Action
    logger.log_event("t1", request, "r", {}, {}, {}, 10)

    # Buffer should be cleared despite error
    assert len(logger._buffer) == 0
