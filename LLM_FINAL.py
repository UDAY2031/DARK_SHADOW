from transformers import pipeline

sentiment_analysis = pipeline("sentiment-analysis")

feedbacks = []

# Prompt the user for feedback
while True:
    user_feedback = input("Enter your feedback : ")
    if user_feedback.lower() == 'exit':
        break
    feedbacks.append(user_feedback)

# Analyze sentiment for each user-provided feedback
for feedback in feedbacks:
    result = sentiment_analysis(feedback)
    print(f"Feedback: {feedback}")
    print(f"Sentiment: {result[0]['label']} (confidence: {result[0]['score']:.4f})")
    print()
