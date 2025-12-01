# AI Brand Studio (Demo - Mock Mode)

This repository contains a minimal runnable demo notebook and mock tools for the AI Brand Studio capstone (Kaggle Agents Intensive). This is a MOCK mode meant for judges to run without API keys. Replace mock tools with real APIs for production.

## Quickstart (Colab or Kaggle)
1. Open `notebooks/brandstudio_demo.ipynb` in Colab or Kaggle.
2. Run all cells. The notebook runs the pipeline in mock mode and produces `/mnt/data/ai-brand-studio/results/brand_package.json` and a sample eval report.

## Repo structure
```
ai-brand-studio/
├─ notebooks/brandstudio_demo.ipynb
├─ src/
│  ├─ agents/
│  └─ tools/
├─ results/
├─ README.md
├─ requirements.txt
```

## Notes
- No API keys required.
- To switch to production, replace tools with real WHOIS / USPTO wrappers and LLM calls.

Reference: project spec (your uploaded capstone spec). See `capstone.txt` for full specification. fileciteturn1file0
