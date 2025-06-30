#!/bin/bash
set -e

# Optional debug (remove in prod)
echo "Using API key: ${VITE_SKYVERN_API_KEY:0:8}********"

npm run start
