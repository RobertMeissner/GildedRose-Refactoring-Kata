metrics:
	@echo "=== Complexity Report ==="
	uv run radon cc . --min=C --total-average
	@echo "\n=== Maintainability Report ==="
	uv run radon mi . --min=C

# Detailed metrics for code review
metrics-detailed:
	uv run radon cc . --min=A --show-complexity --total-average
	uv run radon mi . --min=A --show
	uv run radon raw . --summary


pre-commit:
	uv run pre-commit run -a
