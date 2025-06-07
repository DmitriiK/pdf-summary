#!/bin/zsh
# to make the script executable :  chmod +x run_all.sh

# Activate local Python environment if present
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
fi

uvicorn app.backend:app --host 0.0.0.0 --port 8000 &
python app/processor.py &
wait