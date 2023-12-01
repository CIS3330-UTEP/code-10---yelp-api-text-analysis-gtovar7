import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from yelpapi import YelpAPI

api_key = "B57qFGNz-e-ucmJvGQLfYZAsOo3xTh9pCxeabRU5m7fSuHlRSTHFC1TggLnf98oGzUr7qEkIYCJfPY289uA4beXkJbEMqDlvM3PxGNFqqS-rXxP2G7tJdFudSGZMZXYx"
yelp_api = YelpAPI(api_key)

# A general insight I want to discover is what can I use to help conclude on how one should start a business with several competitors
# To look further into insights, I want to see specific words from the three recent reviews from the code to determine a burger business's success
# I want to know if people are going to continue going to the business that they reviewed and what makes them stay
# If the customer points out any concerns, I would like to see why they think of their reasoning
# I'm going to search in our local area of El Paso and search for different burger restaurants sorted by rating
# Lastly, I'm going to use the Vader Sentiment analysis to see the impact of the 3 reviews.

search_terms = "burgers"
location_term = "El Paso, TX"

search_results = yelp_api.search_query(
    term=search_terms, location=location_term,
    sort_by='rating', limit=20, offset=20
)

# for business in search_results['businesses']:
#     print('\n')
#     print(business)

id_for_reviews = "west-texas-chophouse-el-paso-5"
review_response = yelp_api.reviews_query(id=id_for_reviews)

for review in review_response['reviews']:
    print('\n')
    print(review['text'])

analyzer = SentimentIntensityAnalyzer()
reviews = open('west-texas-chophouse-el-paso-5_yelpapi_burgers_results.csv')

for review in reviews:
    sentiment_score = analyzer.polarity_scores(review)
    print(review)
    print(sentiment_score)
    print('\n')

# result_df = pd.DataFrame.from_dict(review_response['reviews'])
# print(result_df)
# result_df.to_csv(f"{id_for_reviews}_yelpapi_burgers_results.csv")
# print(review_response)

# result_df = pd.DataFrame.from_dict(search_results['businesses'])
# print(result_df)
# result_df.to_csv('yelpapi_businesses_results.csv')