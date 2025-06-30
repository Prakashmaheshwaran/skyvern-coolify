#!/bin/bash
set -e

if [ -f .streamlit/secrets.toml ]; then
  VITE_SKYVERN_API_KEY=$(sed -n 's/.*cred\s*=\s*"\([^"]*\)".*/\1/p' .streamlit/secrets.toml)
  export VITE_SKYVERN_API_KEY
else
  echo "⚠️  .streamlit/secrets.toml not found. Skipping API key export."
fi

npm run start
