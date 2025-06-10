#!/usr/bin/env bash
# to make the script executable :  chmod +x run_all.sh

# Activate local Python environment if present
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
fi

EXTERNAL_IP=$(curl -s ifconfig.me)
PORT=8000
echo "Application URL: http://$EXTERNAL_IP:$PORT/"
uvicorn app.backend:app --host 0.0.0.0 --port $PORT &
python app/processor.py &
wait