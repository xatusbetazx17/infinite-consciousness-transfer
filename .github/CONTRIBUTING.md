# Contributing to Infinite Consciousness Transfer Framework

Thank you for your interest in contributing! We welcome all kinds of improvements: bug fixes, new features, documentation updates, and more. Please follow these guidelines to help us maintain a smooth workflow.

## 1. Code of Conduct

Please read and adhere to our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

## 2. Getting Started

1. Fork the repository on GitHub:

   ```
   https://github.com/xatusbetazx17/infinite-consciousness-transfer.git
   ```
2. Clone your fork locally:

   ```bash
   git clone https://github.com/xatusbetazx17/infinite-consciousness-transfer.git
   cd infinite-consciousness-transfer
   ```

   git clone [https://github.com/xatatusbetazx17/infinite-consciousness-transfer.git](https://github.com/xatatusbetazx17/infinite-consciousness-transfer.git)
   cd infinite-consciousness-transfer

   ```
   ```
3. Create a new branch for your work:

   ```bash
   git checkout -b feature/your-feature-name
   ```
4. Install dependencies and set up your environment:

   ```bash
   pip install -r requirements.txt
   ```

## 3. Development Guidelines

* **Branch Naming:** Use descriptive prefixes:

  * `feature/` for new features
  * `bugfix/` for bug fixes
  * `docs/` for documentation changes

* **Commit Messages:** Write clear, concise messages following the format:

  ```
  type(scope): short description

  Detailed explanation of the change (if necessary).
  ```

  * *type*: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
  * *scope*: area of the code (e.g., `logic_engine`, `bci_interface`)

* **Code Style:** Follow PEP8 conventions. We recommend using [Black](https://github.com/psf/black) to auto-format your code.

* **Imports:** Group imports in the order: standard library, third-party, local modules.

* **Testing:** Write or update unit tests for new functionality. Tests live in the `tests/` directory and should pass locally:

  ```bash
  pytest
  ```

## 4. Pull Request Process

1. Push your branch to your fork:

   ```bash
   git push origin feature/your-feature-name
   ```
2. Open a Pull Request against the `main` branch of the upstream repository.
3. Fill out the PR template, describing:

   * What problem does this change address?
   * How did you implement your solution?
   * Any additional notes or considerations.
4. Ensure all checks (linters, tests, CI) pass before requesting a review.
5. Address review feedback by pushing additional commits to the same branch.

## 5. Documentation

* Update or add relevant documentation under the `docs/` directory.
* Use clear examples and code snippets where applicable.

## 6. Issues

* Before opening a new issue, search existing issues to avoid duplicates.
* Submit issues to the [Issues page](https://github.com/xatatusbetazx17/infinite-consciousness-transfer/issues) with:

  * A descriptive title
  * Steps to reproduce (for bugs)
  * Expected vs. actual behavior
  * Environment details (OS, Python version, etc.)

## 7. License

By contributing, you agree that your contributions will be licensed under the project’s [MIT License](LICENSE.md).

---

Thank you for helping build and improve this framework! We look forward to your contributions. 🎉
