## Installation
Clone repository:
```bash
git clone 
```
## Requirements
1. Install dependencies
```bash
brew install poetry sox ffmpeg 
```
2. Install required packages
```bash
poetry install
```
3. Create .env file and add OpenAI API key (replace `<your_api_key>` with your actual key)
```bash
echo "OPEN_AI_API_KEY=<your_api_key>" > .env
``` 

## Usage
Start service by running the following command:
```bash
sudo python src/main.py
```

While script is running, press `Cmd + F1` and start speaking. After you stop speaking, the script will transcribe your speech 
and copy it to your clipboard. You can paste it anywhere you want afterward.