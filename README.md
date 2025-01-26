# Matching-Jobs-

Project Name:

Job Matching System


---

Project Description:

The Job Matching System is designed to help recruiters and employers efficiently match candidates to job profiles based on their skills, experience, and preferences. This system utilizes Natural Language Processing (NLP) techniques to process job descriptions and candidate profiles, providing a ranked list of candidates for each job opening.


---

Features:

Processes and normalizes job and candidate data.

Matches candidates to jobs using text similarity and ranking techniques.

Considers additional criteria such as location and salary preferences.

Generates a ranked output of candidates for each job.



---

Folder Structure:

Matching-Jobs/
│
├── data/
│   ├── All_Candidates_Data.csv          # Input: Candidate profiles
│   ├── Employer_and_Candidate_Data.csv  # Input: Job profiles
│   └── output.csv                       # Output: Ranked candidate list
│
├── src/
│   ├── main.py                          # Main script to run the application
│   ├── preprocess.py                    # Preprocessing functions
│   ├── matcher.py                       # Matching and ranking functions
│   └── utils.py                         # Helper functions
│
└── README.md                            # Project documentation


---

Setup Instructions:

1. Clone the repository:

git clone <repository-url>
cd Matching-Jobs


2. Install Python and dependencies: Ensure you have Python 3.7 or above installed. Use the following command to install the required libraries:

pip install -r requirements.txt


3. Prepare the data:

Place your input files (All_Candidates_Data.csv and Employer_and_Candidate_Data.csv) in the data/ directory.

Ensure the files are properly formatted according to the column requirements.



4. Run the application: Navigate to the src directory and execute the main script:

python main.py


5. View the results:

The ranked output will be generated as output.csv in the data/ directory.





---

Input File Requirements:

All_Candidates_Data.csv: Contains candidate information with columns like Name, Experience, Skills, Location, and Expected Salary.

Employer_and_Candidate_Data.csv: Contains job descriptions with columns like Job Title, Job Description, Required Skills, Work Location, and Offered Salary.



---

How it Works:

1. Data Preprocessing:

Cleans and normalizes the text fields.

Handles missing data for better accuracy.



2. Matching and Ranking:

Uses NLP-based similarity scoring to match candidates to job descriptions.

Considers additional criteria like salary and location compatibility.



3. Output:

A ranked list of candidates for each job is saved in output.csv.





---

Dependencies:

Python 3.7 or above

Libraries:

pandas

numpy

nltk

scikit-learn




---

Contributing:

Feel free to contribute to this project. Fork the repository, make your changes, and submit a pull request.


---

Contact:

For any issues or suggestions, please reach out to Shreyansh Sharma.