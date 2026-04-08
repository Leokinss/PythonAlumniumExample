Example for Web UI automation using AI with Python Alumnium library.

I am using Google Gemini 3.1 Flash Lite on free API key.
Cost per prompt is about ~1000 tokens.
API Key is defined in env variables. Library automatically uses it with MCP.

I notice it is quite slow. Probably scanning whole page to find elements. Takes about ~10s per prompt. For a test with many prompts(actions) it may take long time to execute.
