"""
Identity Manager Package

Provides snapshotting, checkpointing, and continuity APIs for
managing conscious context states, versioning, and secure tracking.
"""
import os
import logging

from .snapshot import SnapshotManager
from advanced_modules.consciousness_blockchain import record_transaction, verify_chain
from logic_engine.dynamic_expander import LawEngine
from physics_engine.field_simulator import FieldSimulator
from utilities.newmath import NewMath
from advanced_modules.ethics_firewall import EthicsFirewall
from advanced_modules.memory_shards import MemoryShards

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class IdentityManager:
    """
    Orchestrates context snapshot, restore, branching, and secure tracking
    of identity states across simulations.
    """
    def __init__(
        self,
        snapshot_dir: str = 'snapshots',
        blockchain_enabled: bool = True
    ):
        self.math = NewMath()
        self.law_engine = LawEngine()
        self.physics = FieldSimulator(laws=self.law_engine.laws)
        self.ethics = EthicsFirewall()
        self.shards = MemoryShards()
        self.snapshot_mgr = SnapshotManager(directory=snapshot_dir)
        self.blockchain_enabled = blockchain_enabled
        logger.info(f"Initialized IdentityManager with snapshots at '{snapshot_dir}'")

    def create_snapshot(self, context: dict, metadata: dict = None) -> str:
        """
        Capture and persist a snapshot of the given context, record on blockchain if enabled.

        Returns a snapshot reference string.
        """
        # Optional metadata enrichment
        meta = metadata or {}
        meta.setdefault('timestamp', os.path.getmtime(__file__))
        # Create snapshot
        ref = self.snapshot_mgr.create(context)
        logger.info(f"Snapshot created: {ref}")
        # Blockchain record
        if self.blockchain_enabled:
            tx = record_transaction(context_hash=ref, metadata=meta)
            logger.info(f"Blockchain tx recorded: {tx}")
        return ref

    def restore_snapshot(self, snapshot_ref: str) -> dict:
        """
        Restore context from snapshot reference. Verify integrity via blockchain if enabled.
        """
        context = self.snapshot_mgr.restore(snapshot_ref)
        logger.info(f"Snapshot restored: {snapshot_ref}")
        if self.blockchain_enabled:
            valid = verify_chain()
            if not valid:
                raise RuntimeError("Blockchain verification failed – possible tampering detected.")
            logger.info("Blockchain verification succeeded.")
        return context

    def list_snapshots(self) -> list:
        """
        List all available snapshot references with metadata.
        """
        snaps = self.snapshot_mgr.list_snapshots()
        logger.info(f"Listing {len(snaps)} snapshots.")
        return snaps

    def branch_snapshot(self, original_ref: str, branch_meta: dict) -> str:
        """
        Create a new snapshot branch from an existing one, tagging with branch_meta.
        """
        base_ctx = self.restore_snapshot(original_ref)
        # Merge base context with branch metadata as new context
        new_ctx = {**base_ctx, 'branch_meta': branch_meta}
        new_ref = self.create_snapshot(new_ctx, metadata=branch_meta)
        logger.info(f"Branched snapshot {original_ref} → {new_ref}")
        return new_ref

# Singleton instance for easy import
identity_manager = IdentityManager()

__all__ = [
    'SnapshotManager', 'IdentityManager', 'identity_manager'
]

# Basic smoke tests
if __name__ == '__main__':
    print("=== Identity Manager Package Loaded ===")
    mgr = IdentityManager(snapshot_dir='test_snaps', blockchain_enabled=False)
    # Dummy context	dummy_ctx = {'state': 'test', 'graph': None}
    ref = mgr.create_snapshot(dummy_ctx, metadata={'note': 'initial'})
    assert isinstance(ref, str), "create_snapshot must return a string"
    loaded = mgr.restore_snapshot(ref)
    assert loaded['state'] == 'test', "restore_snapshot returned incorrect context"
    snaps = mgr.list_snapshots()
    assert ref in snaps, "list_snapshots must include created ref"
    branch_ref = mgr.branch_snapshot(ref, branch_meta={'branch': 'test'})
    assert branch_ref != ref, "branch_snapshot must create a new reference"
    print("IdentityManager smoke tests passed.")
