Example for Web UI automation using AI prompting with Python Alumnium library.

Link to library project: https://github.com/alumnium-hq/alumnium/blob/main/README.md

I am using Google Gemini 3.1 Flash Lite on free API key.
Cost per prompt is about ~1000 tokens.
API Key is defined in env variables. Library automatically uses it with MCP.

I notice it is quite slow. Probably scanning whole page and traversing the element tree to find elements. Takes up to ~10s per prompt. For a test with many prompts(actions) it may take long time to execute.

Video Demo:

https://github.com/user-attachments/assets/b6978062-d9e3-4386-804d-0421ef409bae

