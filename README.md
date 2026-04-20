📧 Email Spam Classifier

A machine learning project that classifies emails as spam or ham (not spam) using text preprocessing, feature extraction, and supervised learning. Built for deployment as a lightweight Streamlit app.

🚀 Features

• Preprocesses raw email text (tokenization, stopword removal, vectorization).
• Trained with Naive Bayes for efficient spam detection.
• Includes serialized model (spam_model.pkl) and vectorizer (vectorizer.pkl).
• Interactive Streamlit app (app.py) for live testing.
• Small dataset (spam.csv) included for reproducibility.

🛠 Tech Stack

• Python 
• scikit-learn (ML pipeline)
• pandas / numpy (data handling)
• Streamlit (deployment)

Project Structure

email-spam-classifier-clean/
│── train.py              # Training script
│── app.py                # Streamlit app
│── email_spam_classifier.py # Core logic
│── spam.csv              # Dataset (UCI SMS Spam Collection)
│── spam_model.pkl        # Trained model
│── vectorizer.pkl        # Text vectorizer
│── requirements.txt      # Dependencies
│── .gitignore            # Ignore rules
