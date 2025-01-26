import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Preprocessing function for text
def preprocess_text(text):
    if isinstance(text, str):
        return text.lower().strip()
    return ""

# Load employer job profiles
try:
    jobs = pd.read_csv(r"C:\Users\ok\Desktop\Job Matching\Matching-Jobs-\data\job_profiles.csv")
    print("Jobs file loaded successfully.")
except FileNotFoundError:
    print("Error: The jobs file could not be found.")
    exit()

# Normalize column names
jobs.columns = jobs.columns.str.strip().str.lower()
print("Normalized Job Columns:", jobs.columns)

# Ensure 'Job Description' exists
if 'job description' not in jobs.columns:
    print("Error: 'Job Description' column is missing from the jobs file!")
    exit()

# Preprocess the 'Job Description' column
jobs['job description'] = jobs['job description'].apply(preprocess_text)

# Load candidate profiles
try:
    candidates = pd.read_csv(r"C:\Users\ok\Desktop\Job Matching\Matching-Jobs-\data\candidate_profiles.csv")
    print("Candidates file loaded successfully.")
except FileNotFoundError:
    print("Error: The candidates file could not be found.")
    exit()

# Normalize column names
candidates.columns = candidates.columns.str.strip().str.lower()
print("Normalized Candidate Columns:", candidates.columns)

# Ensure 'Profile' exists in candidates
if 'profile' not in candidates.columns:
    print("Error: 'Profile' column is missing from the candidates file!")
    exit()

# Preprocess the 'Profile' column
candidates['profile'] = candidates['profile'].apply(preprocess_text)

# TF-IDF Vectorizer for job descriptions and candidate profiles
tfidf = TfidfVectorizer()

# Compute similarity scores
for index, job_row in jobs.iterrows():
    job_desc = job_row['job description']
    tfidf_matrix = tfidf.fit_transform([job_desc] + candidates['profile'].tolist())
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    
    # Rank candidates by similarity
    candidates['similarity'] = cosine_sim.flatten()
    ranked_candidates = candidates.sort_values(by='similarity', ascending=False)

    # Display the ranked results
    print(f"\nJob: {job_desc}")
    print("Ranked Candidates:")
    print(ranked_candidates[['profile', 'similarity']])

# Save the ranked results for each job
ranked_candidates.to_csv(r"C:\Users\ok\Desktop\Job Matching\Matching-Jobs-\data\ranked_candidates.csv", index=False)
print("\nRanked candidates saved to ranked_candidates.csv")