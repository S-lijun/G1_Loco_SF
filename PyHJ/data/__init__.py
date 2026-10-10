"""Data package."""
# isort:skip_file

from PyHJ.data.batch import Batch
from PyHJ.data.utils.converter import to_numpy, to_torch, to_torch_as
from PyHJ.data.utils.segtree import SegmentTree
from PyHJ.data.buffer.base import ReplayBuffer
from PyHJ.data.buffer.prio import PrioritizedReplayBuffer
from PyHJ.data.buffer.manager import (
    ReplayBufferManager,
    PrioritizedReplayBufferManager,
)
from PyHJ.data.buffer.vecbuf import (
    PrioritizedVectorReplayBuffer,
    VectorReplayBuffer,
)
from PyHJ.data.buffer.cached import CachedReplayBuffer

# Collector imports PyHJ.policy; keep it lazy so policy.base can import
# Batch/ReplayBuffer without circular import (Windows / Python 3.11+).

__all__ = [
    "Batch",
    "to_numpy",
    "to_torch",
    "to_torch_as",
    "SegmentTree",
    "ReplayBuffer",
    "PrioritizedReplayBuffer",
    "ReplayBufferManager",
    "PrioritizedReplayBufferManager",
    "VectorReplayBuffer",
    "PrioritizedVectorReplayBuffer",
    "CachedReplayBuffer",
    "Collector",
    "AsyncCollector",
]


def __getattr__(name: str):
    if name == "Collector":
        from PyHJ.data.collector import Collector

        return Collector
    if name == "AsyncCollector":
        from PyHJ.data.collector import AsyncCollector

        return AsyncCollector
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
