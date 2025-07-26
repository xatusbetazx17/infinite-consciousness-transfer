"""
Infinite Consciousness Transfer Framework Core Package

Initializes and integrates all submodules: BCI interface, neural mapping, emulation runtime,
identity management, logic engine, physics simulation, utilities, and advanced modules.
"""

# BCI Interface
from .bci_interface.acquisition import BCIAcquisition
from .bci_interface.config import BCIConfig

# Neural Mapper
from .neural_mapper.model_generator import generate_model, NeuralGraph

# Emulation Runtime
from .emulation_runtime.core import EmulationRuntime

# Identity Manager
from .identity_manager.snapshot import SnapshotManager

# Logic Engine
from .logic_engine.law_core import Law
from .logic_engine.dynamic_expander import LawEngine

# Physics Engine
from .physics_engine.field_simulator import FieldSimulator

# Utilities
from .utilities.newmath import NewMath
from .utilities.serializers import to_yaml, from_yaml, to_json, from_json

# Advanced Modules
from .advanced_modules.ethics_firewall import EthicsFirewall
from .advanced_modules.consciousness_blockchain import record_transaction, verify_chain
from .advanced_modules.memory_shards import MemoryShards
from .advanced_modules.dna_field_translator import translate_dna
from .advanced_modules.quantum_field_layer import QuantumFieldLayer

# Core Singletons
nm = NewMath()
law_engine = LawEngine()
physics_simulator = FieldSimulator(laws=law_engine.laws)
snapshot_manager = SnapshotManager()
ethics = EthicsFirewall()

# Register core physics axioms and logic laws
# Example: create a smoothing law using NewMath

def _register_core_laws():
    def smoothing_law(ctx):
        # Example smoothing operation using NewMath
        return ctx
    law_engine.register_law(Law(
        name="SmoothingLaw",
        description="Applies spatial smoothing to neural signals",
        activation_func=smoothing_law
    ))
    # Enforce ethics rules
    for law in list(law_engine.laws):
        if not ethics.check_law(law):
            law_engine.laws.remove(law)

# Initialize default laws at import time\ _register_core_laws()

__all__ = [
    # BCI
    "BCIAcquisition", "BCIConfig",
    # Neural Mapper
    "generate_model", "NeuralGraph",
    # Emulation
    "EmulationRuntime", "SnapshotManager",
    # Logic Engine
    "Law", "LawEngine",
    # Physics
    "FieldSimulator",
    # Utilities
    "NewMath", "to_yaml", "from_yaml", "to_json", "from_json",
    # Advanced Modules
    "EthicsFirewall", "record_transaction", "verify_chain",
    "MemoryShards", "translate_dna", "QuantumFieldLayer",
    # Singletons
    "nm", "law_engine", "physics_simulator", "snapshot_manager", "ethics"
]
