Example for Web UI automation using AI prompting with Python Alumnium library.
Alumnium currently integrates with Playwright, Appium, and Selenium

Link to library project: https://alumnium.ai/
GitHub: https://github.com/alumnium-hq/alumnium/blob/main/README.md

I am using Google Gemini 3.1 Flash Lite on free API key.
Cost per prompt is about ~1000 tokens.
API Key is defined in .env files like this:
ALUMNIUM_MODEL=google
GOOGLE_API_KEY=...

I notice it is quite slow. Probably scanning whole page and traversing the element tree to find elements. Takes up to ~10s per prompt. For a test with many prompts(actions) it may take long time to execute.

Video Demo:

https://github.com/user-attachments/assets/b6978062-d9e3-4386-804d-0421ef409bae

run command: pytest