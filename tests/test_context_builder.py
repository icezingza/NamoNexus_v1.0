import pytest
from unittest.mock import MagicMock
from app.core.context_builder import ContextBuilder
from app.api.schemas import ChatRequest
from app.memory.hybrid_store import HybridMemoryStore

def test_context_builder_build_context():
    # Setup
    builder = ContextBuilder()
    mock_memory = MagicMock(spec=HybridMemoryStore)
    mock_memory.retrieve.return_value = [{"reflection": "test memory"}]

    req = ChatRequest(
        message="Hello",
        user_id="user1",
        session_id="session1",
        locale="en-GB",
        metadata={"key": "value"}
    )

    # Execute
    context = builder.build_context(req, mock_memory)

    # Verify
    assert context["user_id"] == "user1"
    assert context["session_id"] == "session1"
    assert context["locale"] == "en-GB"
    assert context["metadata"] == {"key": "value"}
    assert context["retrieved_memory"] == [{"reflection": "test memory"}]

    mock_memory.retrieve.assert_called_once()
    call_args = mock_memory.retrieve.call_args
    assert call_args.kwargs["query"] == "Hello"
    assert call_args.kwargs["user_id"] == "user1"
    assert call_args.kwargs["k"] == 5
