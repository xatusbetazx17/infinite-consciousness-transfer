"""
Snapshot Manager

Implements capturing, persisting, and restoring simulation context states,
as well as listing available snapshots for branching and continuity.
"""
import os
import pickle
import uuid
t from datetime import datetime

class SnapshotManager:
    """
    Manage storage and retrieval of simulation context snapshots.
    """
    def __init__(self, directory: str = 'snapshots'):
        self.directory = directory
        os.makedirs(self.directory, exist_ok=True)

    def create(self, context: dict) -> str:
        """
        Serialize the given context to disk and return a snapshot reference.
        The reference is a filename in the snapshots directory.
        """
        # Generate a unique reference using timestamp and UUID
        timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        ref_id = f"snapshot_{timestamp}_{uuid.uuid4().hex}.snap"
        path = os.path.join(self.directory, ref_id)
        # Write to disk
        with open(path, 'wb') as f:
            pickle.dump(context, f)
        return ref_id

    def restore(self, ref_id: str) -> dict:
        """
        Load and return the context associated with the given snapshot reference.
        Raises FileNotFoundError if the snapshot does not exist.
        """
        path = os.path.join(self.directory, ref_id)
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Snapshot not found: {ref_id}")
        with open(path, 'rb') as f:
            context = pickle.load(f)
        return context

    def list_snapshots(self) -> list:
        """
        Return a list of snapshot reference filenames (sorted chronologically).
        """
        files = [f for f in os.listdir(self.directory) if f.endswith('.snap')]
        # Sort by timestamp embedded in filename
        try:
            files.sort(key=lambda name: name.split('_')[1])
        except Exception:
            files.sort()
        return files

# Basic test cases
if __name__ == '__main__':
    print("=== Running SnapshotManager Tests ===")
    mgr = SnapshotManager(directory='test_snaps')
    # Clean test directory
    for f in mgr.list_snapshots():
        os.remove(os.path.join(mgr.directory, f))
    # Test create
    ctx = {'foo': 'bar', 'value': 42}
    ref = mgr.create(ctx)
    assert isinstance(ref, str) and ref.endswith('.snap'), "create() must return a .snap filename"
    snaps = mgr.list_snapshots()
    assert ref in snaps, "list_snapshots() must include created snapshot"
    # Test restore
    loaded = mgr.restore(ref)
    assert loaded == ctx, "restore() must return the original context"
    # Test FileNotFoundError
    try:
        mgr.restore('nonexistent.snap')
        assert False, "restore() should raise FileNotFoundError for missing ref"
    except FileNotFoundError:
        pass
    print("SnapshotManager tests passed.")
