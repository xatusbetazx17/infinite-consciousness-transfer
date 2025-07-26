"""
Neural Mapper Package

Provides classes and functions to transform brain scan data and live BCI streams
into computational NeuralGraph models, with programmable physics, logic, and ethics integration.
"""
import os
import logging
from .model_generator import generate_model, NeuralGraph
from logic_engine.dynamic_expander import LawEngine
from physics_engine.field_simulator import FieldSimulator
from utilities.newmath import NewMath
from advanced_modules.ethics_firewall import EthicsFirewall
from advanced_modules.memory_shards import MemoryShards

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class NeuralMapper:
    """
    Core orchestrator for mapping scans and BCI data into NeuralGraph models.
    Applies dynamic logic laws, programmable physics, and ethics checks.
    """
    def __init__(self):
        self.math = NewMath()
        self.law_engine = LawEngine()
        self.physics = FieldSimulator(laws=self.law_engine.laws)
        self.ethics = EthicsFirewall()
        self.shards = MemoryShards()
        self._register_default_laws()

    def _register_default_laws(self):
        # Example law: enforce minimal connectivity threshold
        def connectivity_threshold(ctx):
            graph = ctx.get('graph')
            if not isinstance(graph, NeuralGraph):
                return ctx
            # Remove low-weight edges below epsilon
            epsilon = self.math.divide(1, 1000)
            graph.adj_matrix.data = [w for w in graph.adj_matrix.data if abs(w) >= epsilon]
            ctx['graph'] = graph
            return ctx

        law = Law(name="ConnectivityThreshold",
                  description="Prune edges below threshold",
                  activation_func=connectivity_threshold)
        if self.ethics.check_law(law):
            self.law_engine.register_law(law)
            logger.info("Registered ConnectivityThreshold law.")
        else:
            logger.warning("ConnectivityThreshold law failed ethics check.")

    def map_scan(self, scan_path: str, config: dict) -> NeuralGraph:
        """
        Generate and process a NeuralGraph from a brain scan file.
        Applies logic laws and physics simulation before returning.
        """
        if not os.path.isfile(scan_path):
            raise FileNotFoundError(f"Scan file not found: {scan_path}")
        # Step 1: generate raw graph
        graph = generate_model(scan_path, config)
        ctx = {'graph': graph}
        # Step 2: apply dynamic laws
        ctx = self.law_engine.evaluate(ctx)
        # Step 3: physics-driven field embedding
        ctx = self.physics.apply(ctx)
        return ctx['graph']

    def augment_graph(self, graph: NeuralGraph, shard_id: str) -> NeuralGraph:
        """
        Inject and merge a memory shard into an existing graph for enriched context.
        """
        self.shards.inject(graph, shard_id)
        return graph

    def save_graph(self, graph: NeuralGraph, path: str) -> None:
        """
        Serialize NeuralGraph to disk using format inferred from extension (.pkl, .npz).
        """
        ext = os.path.splitext(path)[1].lower()
        if ext == '.pkl':
            import pickle
            with open(path, 'wb') as f:
                pickle.dump(graph, f)
        elif ext == '.npz':
            import numpy as np
            np.savez(path, data=graph.adj_matrix.data, indices=graph.adj_matrix.indices,
                     indptr=graph.adj_matrix.indptr, shape=graph.adj_matrix.shape)
        else:
            raise ValueError(f"Unsupported extension: {ext}")
        logger.info(f"NeuralGraph saved to {path}")

    def load_graph(self, path: str) -> NeuralGraph:
        """
        Load a NeuralGraph from disk (.pkl or .npz).
        """
        ext = os.path.splitext(path)[1].lower()
        if ext == '.pkl':
            import pickle
            with open(path, 'rb') as f:
                graph = pickle.load(f)
        elif ext == '.npz':
            import numpy as np
            arr = np.load(path)
            data, indices, indptr, shape = arr['data'], arr['indices'], arr['indptr'], tuple(arr['shape'])
            from scipy.sparse import csr_matrix
            graph = NeuralGraph(csr_matrix((data, indices, indptr), shape=shape), None)
        else:
            raise ValueError(f"Unsupported extension: {ext}")
        logger.info(f"NeuralGraph loaded from {path}")
        return graph

# Singleton instance
neural_mapper = NeuralMapper()

__all__ = [
    "generate_model", "NeuralGraph",
    "NeuralMapper", "neural_mapper"
]
