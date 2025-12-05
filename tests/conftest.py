import sys
import typing
import pytest

# Compatibility patch for Pydantic with Python 3.13+
# Pydantic versions < 2.10 (approx) call typing._eval_type with 'prefer_fwd_module'
# which causes a TypeError in newer Python versions.
if sys.version_info >= (3, 13) and hasattr(typing, "_eval_type"):
    _original_eval_type = typing._eval_type

    def _patched_eval_type(t, globalns, localns, type_params=None, **kwargs):
        # Remove 'prefer_fwd_module' if present, as it's not supported in this Python version's typing._eval_type
        kwargs.pop('prefer_fwd_module', None)
        return _original_eval_type(t, globalns, localns, type_params=type_params, **kwargs)

    typing._eval_type = _patched_eval_type
