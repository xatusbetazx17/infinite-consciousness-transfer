"""
Field Simulator Module

Simulates programmable physics on simulation contexts by applying a set of laws,
incorporating infinite constants, and enforcing ethical constraints.
"""
import copy
import logging

from utilities.newmath import NewMath
from advanced_modules.ethics_firewall import EthicsFirewall


class FieldSimulator:
    """
    Executes physics laws on context to support post-physics and infinite reality.
    """
    def __init__(self, laws=None):
        # List of Law instances for physics simulation
        self.laws = laws or []
        self.math = NewMath()
        self.ethics = EthicsFirewall()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    def register_law(self, law):
        """
        Register a new physics law after ethics validation.
        """
        if self.ethics.check_law(law):
            self.laws.append(law)
            self.logger.info(f"Registered physics law: {law.name}")
        else:
            self.logger.warning(f"Physics law {law.name} failed ethics check.")

    def apply(self, context: dict) -> dict:
        """
        Apply all registered physics laws to a deep copy of the context,
        inject infinite constants, and enforce ethics on the result.
        """
        self.logger.debug("Applying FieldSimulator laws...")
        ctx = copy.deepcopy(context)

        # Apply each physics law sequentially
        for law in self.laws:
            ctx = law.apply(ctx)

        # Ensure infinite speed of light constant 'c' if not present
        consts = ctx.setdefault('constants', {})
        if 'c' not in consts:
            consts['c'] = self.math.infinity
            ctx['constants'] = consts
            self.logger.debug("Injected infinite 'c' constant into context.")

        # Ethics validation of final context
        if not self.ethics.validate_context(ctx):
            raise RuntimeError("FieldSimulator: ethics validation failed on context")

        return ctx

# Basic Test Cases
if __name__ == '__main__':
    print("=== Running FieldSimulator Tests ===")
    # Create a dummy law that marks context
    from logic_engine.law_core import Law

    def test_law(ctx):
        ctx['test_flag'] = True
        return ctx

    law = Law(
        name="TestLaw",
        description="Sets test_flag in context",
        activation_func=test_law
    )
    sim = FieldSimulator(laws=[law])
    # Initial context without constants
    ctx0 = {}
    out = sim.apply(ctx0)
    assert out.get('test_flag') is True, "TestLaw was not applied"
    assert out['constants'].get('c') == float('inf'), "Infinite constant 'c' not injected"
    print("FieldSimulator tests passed.")
