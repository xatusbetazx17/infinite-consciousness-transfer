"""
Voxel-Level Neural Net Model Generator

Transforms high-resolution brain scans or simulated data into sparse NeuralGraph models,
applying dynamic logic laws, programmable physics, and ethical validation.
"""
import os
import numpy as np
from scipy.sparse import coo_matrix, csr_matrix

# Optional NIfTI support
try:
    import nibabel as nib
except ImportError:
    nib = None

from logic_engine.dynamic_expander import LawEngine
from physics_engine.field_simulator import FieldSimulator
from utilities.newmath import NewMath
from advanced_modules.ethics_firewall import EthicsFirewall


class NeuralGraph:
    """
    Data structure holding a sparse adjacency matrix and node feature vector.
    """
    def __init__(self, adj_matrix: csr_matrix, node_features: np.ndarray):
        self.adj_matrix = adj_matrix
        self.node_features = node_features

    def num_nodes(self):
        return self.node_features.size

    def num_edges(self):
        return int(self.adj_matrix.nnz)


def generate_model(scan_path: str, config: dict) -> NeuralGraph:
    """
    Build a NeuralGraph from a scan file or simulated data.

    config keys:
      - 'shape': tuple of 3 ints for simulated data if no scan file
      - 'threshold': float, minimum weight to include edge
    """
    nm = NewMath()
    law_engine = LawEngine()
    physics = FieldSimulator(laws=law_engine.laws)
    ethics = EthicsFirewall()

    # Load or simulate 3D data
    if nib and os.path.isfile(scan_path) and scan_path.lower().endswith(('.nii', '.nii.gz')):
        img = nib.load(scan_path)
        data = img.get_fdata()
    else:
        shape = config.get('shape', (16, 16, 16))
        data = np.random.rand(*shape)

    dims = data.shape
    num_voxels = data.size
    features = data.flatten()

    # Build adjacency: connect 6-neighbors when weight > threshold
    threshold = config.get('threshold', 0.1)
    coords = np.stack(np.unravel_index(np.arange(num_voxels), dims), axis=1)

    rows, cols, weights = [], [], []
    for idx, (x, y, z) in enumerate(coords):
        for dx, dy, dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
            nx, ny, nz = x+dx, y+dy, z+dz
            if 0 <= nx < dims[0] and 0 <= ny < dims[1] and 0 <= nz < dims[2]:
                nidx = np.ravel_multi_index((nx,ny,nz), dims)
                # weight: normalized feature ratio
                w = float(nm.divide(features[idx], features[nidx] + 1e-9))
                if abs(w) >= threshold:
                    rows.append(idx)
                    cols.append(nidx)
                    weights.append(w)

    adj_coo = coo_matrix((weights, (rows, cols)), shape=(num_voxels, num_voxels))
    adj = adj_coo.tocsr()
    graph = NeuralGraph(adj, features)

    # Apply dynamic logic laws
    ctx = {'graph': graph}
    ctx = law_engine.evaluate(ctx)
    graph = ctx['graph']

    # Embed programmable physics (no-op if no laws)
    ctx = physics.apply({'graph': graph})
    graph = ctx['graph']

    # Ethics validation: ensure edge count is within limits
    max_edges = config.get('max_edges', num_voxels * 6)
    if graph.num_edges() > max_edges:
        raise ValueError(f"Ethics violation: too many edges ({graph.num_edges()}) > max {max_edges}")

    return graph


# Basic Test Cases
if __name__ == "__main__":
    # Test with simulated data
    conf = {'shape': (8,8,8), 'threshold': 0.05, 'max_edges': 500}
    g = generate_model("nonexistent.nii", conf)
    assert isinstance(g, NeuralGraph), "generate_model did not return NeuralGraph"
    assert g.num_nodes() == 8*8*8, f"Unexpected node count: {g.num_nodes()}"
    assert g.num_edges() > 0, "Graph has no edges"
    print(f"Test passed: nodes={g.num_nodes()}, edges={g.num_edges()}")
