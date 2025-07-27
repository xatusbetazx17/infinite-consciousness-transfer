"""
Physics Engine Package

Provides programmable physics support for post-physics and infinite reality simulation.
Integrates dynamic laws, NewMath extensions, and ethical validation.
"""
import logging

from .field_simulator import FieldSimulator
from logic_engine.law_core import Law
from logic_engine.dynamic_expander import LawEngine
from utilities.newmath import NewMath
from advanced_modules.ethics_firewall import EthicsFirewall

# Configure logger for the physics engine package
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class PhysicsEngine:
    """
    Orchestrates programmable physics simulations:
      - Registers core physics axioms as dynamic laws
      - Manages FieldSimulator for context updates
      - Enforces ethical constraints on physics rules
    """
    def __init__(self):
        self.math = NewMath()
        self.law_engine = LawEngine()
        self.ethics = EthicsFirewall()
        # Create simulator that applies laws to context
        self.simulator = FieldSimulator(laws=self.law_engine.laws)
        # Register foundational physics axioms
        self._register_core_axioms()

    def _register_core_axioms(self):
        # Example: Gravity law based on inverse-square
        def gravity_law(ctx):
            # Placeholder: apply gravitational influence on context['phys']
            phys = ctx.setdefault('phys', {})
            phys['gravity'] = phys.get('gravity', 9.81)
            ctx['phys'] = phys
            return ctx

        law = Law(
            name="GravityAxiom",
            description="Applies classical gravity (constant g) to physical context",
            activation_func=gravity_law,
            author="system",
            version="1.0.0"
        )
        if self.ethics.check_law(law):
            self.law_engine.register_law(law)
            logger.info("Registered GravityAxiom law.")
        else:
            logger.warning("GravityAxiom law failed ethics check.")

    def apply(self, context: dict) -> dict:
        """
        Apply all registered physics laws to the given simulation context.
        """
        logger.debug("Applying physics engine laws...")
        # Evaluate dynamic physics laws
        ctx = self.law_engine.evaluate(context)
        # Delegate to FieldSimulator for field computations
        result = self.simulator.apply(ctx)
        return result

# Singleton instance for easy import
physics_engine = PhysicsEngine()

# Exports
__all__ = [
    'FieldSimulator',
    'PhysicsEngine',
    'physics_engine'
]

# Basic smoke test
if __name__ == '__main__':
    print("=== Physics Engine Package Loaded ===")
    # Test singleton
    from neural_mapper.model_generator import NeuralGraph
    import numpy as np
    # Create a dummy context
    dummy_ctx = {'graph': NeuralGraph(csr_matrix(([], ([], [])), shape=(0,0)), np.array([]))}
    ctx_out = physics_engine.apply(dummy_ctx)
    assert 'phys' in ctx_out, "PhysicsEngine.apply must inject 'phys' key"
    assert ctx_out['phys'].get('gravity') == 9.81, "GravityAxiom must set g=9.81"
    print("PhysicsEngine smoke test passed.")
