Example using Python Alumnium AI UI Automation library.

I am using Google Gemini 3.1 Flash Lite on free API key.
Cost per prompt is about ~1000 tokens.

I notice it is quite slow. Probably scanning whole page and traversing the element tree to find elements. Takes about ~10s per prompt. For a test with many prompts(actions) it may take long time to execute. My test_login.py file takes 70s to run.