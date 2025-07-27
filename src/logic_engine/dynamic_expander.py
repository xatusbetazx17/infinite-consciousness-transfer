"""
Dynamic Law Expander Module

Provides the LawEngine class to register, evaluate, and evolve programmable laws
for transforming simulation contexts in the Infinite Consciousness Transfer Framework.
"""
import logging
from typing import Any, Dict, List
from .law_core import Law

# Configure module logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class LawEngine:
    """
    Engine to manage and apply a set of Laws to simulation contexts,
    and optionally evolve new laws based on technology context.
    """
    def __init__(self):
        self.laws: List[Law] = []
        logger.info("Initialized LawEngine with empty law set.")

    def register_law(self, law: Law) -> None:
        """
        Register a new Law. Raises if law is invalid or duplicate.
        """
        if not isinstance(law, Law):
            raise TypeError("Only Law instances can be registered.")
        if any(existing.id == law.id for existing in self.laws):
            raise ValueError(f"Law '{law.name}' is already registered.")
        self.laws.append(law)
        logger.info(f"Registered law: {law.name} (v{law.version})")

    def evaluate(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Apply all registered laws sequentially to the given context.
        Returns the transformed context.
        """
        ctx = context
        for law in self.laws:
            logger.debug(f"Evaluating law: {law.name}")
            ctx = law.apply(ctx)
        return ctx

    def evolve(self, tech_context: Dict[str, Any]) -> List[Law]:
        """
        Placeholder for AI-driven law synthesis: analyze tech_context
        and generate new Law instances. Returns a list of new laws.
        """
        # TODO: integrate with AI assistant to generate law definitions
        logger.info("Evolving new laws based on technology context...")
        # Example stub: no new laws
        new_laws: List[Law] = []
        return new_laws

__all__ = ["LawEngine"]

# Basic Test Cases
if __name__ == '__main__':
    print("=== Running LawEngine Tests ===")
    engine = LawEngine()
    # Define a simple law that increments 'counter' in context
    def inc_counter(ctx: Dict[str, Any]) -> Dict[str, Any]:
        ctx = ctx.copy()
        ctx['counter'] = ctx.get('counter', 0) + 1
        return ctx
    from .law_core import Law
    law = Law(
        name="IncrementCounter",
        description="Increments counter by 1",
        activation_func=inc_counter
    )
    engine.register_law(law)
    # Evaluate on empty context
    result = engine.evaluate({})
    assert result.get('counter') == 1, f"Expected counter 1, got {result.get('counter')}"
    # Evaluate again
    result2 = engine.evaluate(result)
    assert result2.get('counter') == 2, f"Expected counter 2, got {result2.get('counter')}"
    # Test registration errors
    try:
        engine.register_law(law)
        assert False, "Duplicate law registration should raise ValueError"
    except ValueError:
        pass
    try:
        engine.register_law("not a law")
        assert False, "Registering non-Law should raise TypeError"
    except TypeError:
        pass
    print("LawEngine
