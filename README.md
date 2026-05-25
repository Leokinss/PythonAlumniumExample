# Alumnium AI Web UI Automation

Example for Web UI automation using AI prompting with the Python Alumnium library.
Alumnium currently integrates with Playwright, Appium, and Selenium.

## Links
- **Library:** https://alumnium.ai/
- **GitHub:** https://github.com/alumnium-hq/alumnium/blob/main/README.md

## Setup

I am using Google Gemini on a free API key.

Cost per prompt is approximately ~1000 tokens.

Add the following to your `.env` file:
```env
ALUMNIUM_MODEL=google
GOOGLE_API_KEY=...
```

## Running Tests

```bash
pytest
```

## Notes

Performance is quite slow — likely due to scanning the whole page and traversing the element tree to find elements. Takes up to ~10s per prompt. For a test with many prompts/actions, total execution time may be significant.

## Video Demo

https://github.com/user-attachments/assets/b6978062-d9e3-4386-804d-0421ef409bae