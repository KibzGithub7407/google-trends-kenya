# google-trends-kenya
## Google Trends Kenya Automation

Automatically fetches the latest Google Trends for Kenya and generates social media post content.

## Features

- Fetches daily trending searches in Kenya using [pytrends](https://github.com/GeneralMills/pytrends)
- Formats a social media-ready post
- Can be scheduled via GitHub Actions
- (Optional) Post directly to Twitter/X

## Setup

1. Clone this repo.
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your social media API keys (if posting automatically).
4. Add your secrets to GitHub for automated workflows.

## Automation

Edit `.github/workflows/daily-trends.yml` to customize the schedule or add more steps.
