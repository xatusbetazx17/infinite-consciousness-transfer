"""
Infinity-Aware Arithmetic & Advanced Physics Extensions

Provides scalar and iterable (vectorized) operations with support for:
- Infinity handling (division by zero, infinite propagation)
- Extended physics computations: escape velocity, black-hole density,
  relativistic velocity ratio, hyperinflation, and quantum tunneling.
- Equation solver with custom infinite constants.
"""
import math
from typing import Union, Iterable

Number = Union[int, float]
Sequence = Union[Iterable[Number], Number]

class NewMath:
    """
    A mathematical toolkit that handles infinities gracefully and
    provides advanced physics-related methods.
    """
    def __init__(self):
        self.infinity = float('inf')
        self._G = 6.67430e-11  # gravitational constant
        self._c = 299_792_458  # speed of light (m/s)

    def _is_infinite(self, x):
        return x == self.infinity or x == -self.infinity

    def add(self, a: Sequence, b: Sequence) -> Sequence:
        """Element-wise addition handling infinities."""
        if isinstance(a, Iterable) and isinstance(b, Iterable):
            return [self.add(x, y) for x, y in zip(a, b)]
        if self._is_infinite(a) or self._is_infinite(b):
            return self.infinity if a == self.infinity or b == self.infinity else -self.infinity
        return a + b

    def subtract(self, a: Sequence, b: Sequence) -> Sequence:
        """Element-wise subtraction with infinity rules."""
        if isinstance(a, Iterable) and isinstance(b, Iterable):
            return [self.subtract(x, y) for x, y in zip(a, b)]
        if self._is_infinite(a) and self._is_infinite(b):
            return float('nan')  # undefined
        if self._is_infinite(a):
            return a
        if self._is_infinite(b):
            return -b
        return a - b

    def multiply(self, a: Sequence, b: Sequence) -> Sequence:
        """Element-wise multiplication with zero and infinity checks."""
        if isinstance(a, Iterable) and isinstance(b, Iterable):
            return [self.multiply(x, y) for x, y in zip(a, b)]
        if (a == 0 or b == 0):
            return 0
        if self._is_infinite(a) or self._is_infinite(b):
            return self.infinity
        return a * b

    def divide(self, a: Sequence, b: Sequence) -> Sequence:
        """Element-wise division handling zero denominators as infinity."""
        if isinstance(a, Iterable) and isinstance(b, Iterable):
            return [self.divide(x, y) for x, y in zip(a, b)]
        try:
            if b == 0:
                return self.infinity if a != 0 else float('nan')
            return a / b
        except OverflowError:
            return self.infinity

    def exponentiate(self, a: Number, b: Number) -> Number:
        """Handles infinite bases or exponents in a physics-aware manner."""
        if a == self.infinity and b == 0:
            return 1
        if self._is_infinite(b):
            if abs(a) > 1:
                return self.infinity
            if abs(a) < 1:
                return 0
        try:
            return a ** b
        except OverflowError:
            return self.infinity

    def factorial(self, n: int) -> Union[int, float]:
        """Factorial with infinity guard."""
        if self._is_infinite(n):
            return self.infinity
        if n < 0 or int(n) != n:
            raise ValueError("Factorial only defined for non-negative integers.")
        return math.factorial(int(n))

    def escape_velocity(self, mass: Number, radius: Number) -> Number:
        """Compute escape velocity v = sqrt(2GM/r). Infinity if radius == 0."""
        if radius == 0:
            return self.infinity
        return math.sqrt(self.divide(2 * self._G * mass, radius))

    def black_hole_density(self, mass: Number, radius: Number) -> Number:
        """Compute density = mass / ((4/3)πr³). Infinity if r == 0."""
        volume = (4/3) * math.pi * radius**3
        if volume == 0:
            return self.infinity
        return self.divide(mass, volume)

    def velocity_ratio(self, velocity: Number) -> Number:
        """Lorentz velocity ratio v/(1 - v²/c²), infinity if v >= c."""
        if abs(velocity) >= self._c:
            return self.infinity
        return velocity / (1 - (velocity**2 / self._c**2))

    def hyperinflation_model(self, initial: Number, years: int) -> Number:
        """Model with infinite growth: initial * (1 + infinity) ** years."""
        return self.infinity

    def quantum_tunneling(self) -> Number:
        """Estimate for quantum tunneling as 1/0."""
        return self.infinity

    def solve_equation(self, equation: str) -> Any:
        """Evaluate a Python expression with 'inf' bound to this.infinity."""
        try:
            return eval(equation, {"inf": self.infinity, "ZeroDiv": self.infinity}, {})
        except ZeroDivisionError:
            return self.infinity
        except Exception as e:
            return f"Error: {e}"

# Instantiate singleton
nm = NewMath()

if __name__ == '__main__':
    print("=== Running NewMath Tests ===")
    # Basic operations
    assert nm.add(5, nm.infinity) == nm.infinity
    assert nm.divide(1, 0) == nm.infinity
    assert math.isnan(nm.subtract(nm.infinity, nm.infinity))
    # Physics tests
    ev = nm.escape_velocity(5e24, 0)
    assert ev == nm.infinity
    rho = nm.black_hole_density(5e24, 0)
    assert rho == nm.infinity
    vr = nm.velocity_ratio(nm._c)
    assert vr == nm.infinity
    # Hyperinflation
    assert nm.hyperinflation_model(100, 10) == nm.infinity
    print("All NewMath tests passed.")
