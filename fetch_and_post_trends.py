import datetime
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)
today = datetime.date.today()

def fetch_trending_searches():
    trending_searches_df = pytrends.trending_searches(pn='kenya')
    return trending_searches_df[0].tolist()

def format_social_post(trends):
    top_trend = trends[0]
    hashtags = " #TrendingInKenya " + " ".join([f"#{t.replace(' ', '')}" for t in trends[:3]])
    message = (
        f"🇰🇪 Top Google Trend today ({today}): {top_trend}\n\n"
        f"Other trending topics: {', '.join(trends[1:5])}\n"
        f"{hashtags}\n"
        f"Stay ahead with the latest trends! 🚀"
    )
    return message

if __name__ == "__main__":
    trends = fetch_trending_searches()
    if trends:
        post = format_social_post(trends)
        print(post)
    else:
        print("Could not fetch Google Trends for Kenya.")
