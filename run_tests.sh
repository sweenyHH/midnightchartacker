#!/bin/bash

echo "Running tests..."

# optional: virt. env aktivieren
# source venv/bin/activate

pytest -v

EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo "✅ All tests passed!"
else
    echo "❌ Some tests failed!"
fi

exit $EXIT_CODE