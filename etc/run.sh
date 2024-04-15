#!/bin/bash
echo "Current directory: $(pwd)"
echo "Listing the current directory contents:"
ls -l

echo "PYTHONPATH: $PYTHONPATH"

python ragtalk/make_embeddings.py
uvicorn ragtalk.app.server:app --host 0.0.0.0 --port 8080 --reload