# BIG/SMALL Predictor App

This is a simple Flask web app that takes 4 BIG/SMALL inputs and predicts the next outcome.

## Features:
- Input: 4 past results (BIG/SMALL)
- Output: Next predicted result
- Green background UI
- BIG shown in green, SMALL in red

## To run locally:
```bash
pip install -r requirements.txt
python app.py
```

## For Render Deployment:
- Set **Start Command**: `python app.py`
- Add Environment Variable:
  - `PORT=10000`