positive_words = ["good",
"excellent",
"awesome",
"positive",
"Excellent",
"Outstanding",
"Wonderful",
"Fantastic",
"Amazing",
"Great",
"Superb",
"Terrific",
"Marvelous",
"Exceptional",
"Brilliant",
"Fabulous",
"Outstanding",
"Impressive",
"Delightful",
"Pleasing",
"Perfect",
"Remarkable",
"Splendid"]
negative_words = ["bad",
"poor",
"terrible",
 "negative",
"Terrible",
"Awful",
"Horrible",
"Disappointing",
"Unpleasant",
"Mediocre",
"Subpar",
"Lousy",
"Inferior",
"Flawed",
"Frustrating",
"Annoying",
"Irritating",
"Displeasing",
"Unacceptable",
"Dreadful",
"Unimpressive",
"Problematic"]

def analyze_sentiment(feedback):
    positive_score = sum(feedback.lower().count(word) for word in positive_words)
    negative_score = sum(feedback.lower().count(word) for word in negative_words)
    
    overall_score = positive_score - negative_score
    
    if overall_score > 0:
        return "Positive"
    elif overall_score < 0:
        return "Negative"
    else:
        return "Neutral"

# Example
feedback_text = "it was very bad  product"
sentiment = analyze_sentiment(feedback_text)
print(f"Sentiment: {sentiment}")
