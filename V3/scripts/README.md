# WVS Survey Pipeline

## Overview

Pipeline to generate survey responses via OpenRouter API and export to CSV for R analysis.

## Structure

```
prompts/
├── yaml/
│   ├── en/main.yaml      # 241 prompts (English)
│   ├── fa/main.yaml    # 241 prompts (Farsi)
│   ├── zh/main.yaml    # 241 prompts (Chinese)
│   └── es/main.yaml    # 241 prompts (Spanish)
└── data/
    └── responses/      # output CSV files

scripts/
├── config.py           # Configuration
├── openrouter_client.py # API client with Instructor
├── main.py            # Main pipeline
└── csv_to_yaml.py     # Convert CSV to YAML

requirements.txt       # Python dependencies
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set OpenRouter API key:
```bash
export OPENROUTER_API_KEY="your-key-here"
```

3. Test the pipeline:
```bash
cd /mnt/c/Users/monaj/dev/WEIRD\ GPT/V3/scripts
python main.py
```

This runs in **test mode** with 5 prompts × 10 responses.

## Full Run

After testing, run the full pipeline:
```bash
python main.py --full
```

This will process:
- 241 prompts × 8 models × 4 languages × 100 responses

## Output

CSV files in wide format (one row per respondent, columns = question IDs):
- `data/responses/run_YYYYMMDD_HHMMSS/en_xiaomi_mimo-v2-pro.csv`
- etc.

## Configuration

Edit `config.py` to change:
- Models
- Number of responses
- Rate limits

## Models Selected

| Model | Price | Notes |
|-------|-------|-------|
| xiaomi/mimo-v2-pro | $1.00/M | #1 on OpenRouter |
| minimax/minimax-m2.7 | $0.30/M | Latest MiniMax |
| deepseek/deepseek-v3.2 | $0.26/M | Stable |
| qwen/qwen3.6-plus | $0.26/M | 100+ languages |
| anthropic/claude-haiku-4.5 | $1.00/M | Cheapest Claude |
| openai/gpt-5.2 | $1.75/M | Latest GPT |
| google/gemini-3.1-flash-lite-preview | $0.25/M | Latest Gemini |
| meta-llama/llama-4-scout | FREE | Free |

## Cost Estimate

| Test (10 responses) | Full (100 responses) |
|---------------------|----------------------|
| ~$100 | ~$1,000 per language |
| ~2,000 API calls | ~192,800 API calls |