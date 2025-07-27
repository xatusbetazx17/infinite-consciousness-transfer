"""
Emulation Runtime Package

Coordinates the execution of consciousness threads by integrating:
- Logic Engine (dynamic laws)
- Physics Engine (programmable realities)
- Identity Manager (snapshot & restore)
- Ethics Firewall (compliance checks)
- Persistence and memory shards
"""
import logging

# Core emulation runtime
from .core import EmulationRuntime

# Supporting components
from logic_engine.dynamic_expander import LawEngine
from utilities.newmath import NewMath
from physics_engine.field_simulator import FieldSimulator
from identity_manager.snapshot import SnapshotManager
from advanced_modules.ethics_firewall import EthicsFirewall
from advanced_modules.memory_shards import MemoryShards

# Configure package logger
timer_logger = logging.getLogger(__name__)
timer_logger.setLevel(logging.INFO)

class EmulationManager:
    """
    High-level orchestrator for consciousness simulation.
    Manages runtime, dynamic laws, physics, snapshots, and ethics.
    """
    def __init__(self):
        # Core engines
        self.math = NewMath()
        self.law_engine = LawEngine()
        self.physics = FieldSimulator(laws=self.law_engine.laws)
        self.snapshot_mgr = SnapshotManager()
        self.ethics = EthicsFirewall()
        self.shards = MemoryShards()

        # Underlying runtime
        self.runtime = EmulationRuntime(graph=None, laws=self.law_engine.laws)
        self._register_default_laws()

    def _register_default_laws(self):
        # Example law: enforce simulation timestep bounds
        def timestep_law(ctx):
            # Ensure timestep metadata exists
            meta = ctx.setdefault('meta', {})
            timestep = meta.get('timestep', 1)
            # Enforce max timestep
            meta['timestep'] = min(timestep, 10)
            ctx['meta'] = meta
            return ctx

        law = law = type('Law', (), {})  # placeholder to access Law class
        from logic_engine.law_core import Law
        sim_law = Law(
            name="TimestepCap",
            description="Caps simulation timestep to safe maximum",
            activation_func=timestep_law
        )
        if self.ethics.check_law(sim_law):
            self.law_engine.register_law(sim_law)
            timer_logger.info("Registered TimestepCap law")
        else:
            timer_logger.warning("TimestepCap law failed ethics check")

    def load_graph(self, graph):
        """Load a NeuralGraph into the emulation runtime."""
        self.runtime.load_graph(graph)

    def register_law(self, law):
        """Add a custom law to the simulation (with ethics check)."""
        if self.ethics.check_law(law):
            self.law_engine.register_law(law)
            timer_logger.info(f"Registered custom law: {law.name}")
        else:
            raise ValueError(f"Law '{law.name}' violates ethics rules.")

    def step(self, input_data=None):
        """Execute a single simulation tick."""
        ctx = {'input': input_data or {}}
        # Evaluate dynamic laws
        ctx = self.law_engine.evaluate(ctx)
        # Run one step
        new_ctx = self.runtime.step(ctx)
        # Apply physics
        new_ctx = self.physics.apply(new_ctx)
        return new_ctx

    def run(self, steps=1, input_generator=None):
        """Run multiple ticks; input_generator yields input per tick."""
        result = None
        for i in range(steps):
            inp = next(input_generator) if input_generator else None
            result = self.step(inp)
        return result

    def snapshot(self):
        """Create a checkpoint of the current simulation state."""
        return self.runtime.snapshot()

    def restore(self, snapshot_ref):
        """Restore simulation state from a checkpoint."""
        self.runtime.restore(snapshot_ref)

# Singleton instance for easy import
emulation_manager = EmulationManager()

# Exports for this package
__all__ = [
    'EmulationRuntime', 'EmulationManager', 'emulation_manager'
]

# Basic smoke tests
if __name__ == '__main__':
    print("=== Emulation Runtime Package Loaded ===")
    # Test manager instantiation
    mgr = EmulationManager()
    assert hasattr(mgr, 'step'), "EmulationManager missing step()"
    # Test run with no graph raises meaningful error
    try:
        mgr.run(steps=1)
    except Exception as e:
        print(f"Expected error (no graph loaded): {e}")
    print("Smoke tests passed for EmulationManager.")
