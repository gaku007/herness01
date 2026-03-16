#!/bin/bash

# sayHello Agent
# This script implements the sayHello custom agent
# It creates a hello_output.md file in the project root

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
OUTPUT_FILE="$PROJECT_ROOT/hello_output.md"

# Get current timestamp
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Create the output file with the specified format
cat > "$OUTPUT_FILE" << EOF
# Hello Output

**Time**: $TIMESTAMP
**Message**: さようなら、エージェント呼び出し完了

---
Created by: sayHello Agent
EOF

# Confirm file creation
echo "✓ sayHello agent executed successfully"
echo "✓ File created: $OUTPUT_FILE"
