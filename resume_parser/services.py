import PyPDF2
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the English language model for spaCy
nlp = spacy.load('en_core_web_sm')

def extract_text_from_resume(pdf_file):
    """
    Extracts text content from a PDF file.
    
    Args:
    pdf_file: A file object containing the PDF resume.
    
    Returns:
    A string containing all the text extracted from the PDF.
    """
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def extract_skills(text):
    """
    Extracts potential skills from the given text using spaCy's named entity recognition.
    
    Args:
    text: A string containing the text to analyze.
    
    Returns:
    A set of unique skills extracted from the text.
    """
    doc = nlp(text)
    skills = [ent.text for ent in doc.ents if ent.label_ in ['SKILL', 'ORG', 'WORK_OF_ART']]
    return set(skills)

def calculate_match_score(resume, job):
    """
    Calculates a match score between a resume and a job posting using TF-IDF and cosine similarity.
    
    Args:
    resume: A Resume object containing the candidate's resume.
    job: A JobPosting object containing the job description and required skills.
    
    Returns:
    A float representing the match score as a percentage (0-100).
    """
    vectorizer = TfidfVectorizer()
    resume_text = extract_text_from_resume(resume.file)
    required_skills = job.required_skills
    tfidf_matrix = vectorizer.fit_transform([resume_text, required_skills])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return round(similarity[0][0] * 100, 2)
