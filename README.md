# Smart Interview Assistant

An AI-powered interview evaluation system that analyzes resumes, speech communication, and facial emotions to generate candidate performance scores and personalized feedback.

---

# Overview

The Smart Interview Assistant is designed to automate and improve the traditional recruitment process using Artificial Intelligence technologies such as:

* Natural Language Processing (NLP)
* Speech Processing
* Computer Vision
* Machine Learning

The system evaluates candidates by analyzing:

* Resume relevance
* Communication skills
* Facial emotions during interviews

The application generates:

* Resume match percentage
* Speech analysis metrics
* Emotion analysis
* Final candidate score
* Personalized feedback

---

# Features

## Resume Analysis

* Resume PDF text extraction
* Job description matching
* Skill extraction
* Missing skill detection
* Resume score generation

---

## Speech Analysis

* Speech-to-text conversion using Whisper
* Words per minute calculation
* Filler word detection
* Communication analysis
* Speech score generation

---

## Emotion Detection

* Face detection using OpenCV
* Emotion recognition using DeepFace
* Dominant emotion prediction
* Confidence analysis
* Emotion score generation

---

## Final Evaluation

* Weighted score calculation
* Candidate performance analytics
* AI-generated feedback
* Interactive dashboard

---

# System Workflow

```text
User Uploads:
Resume + Job Description + Interview Video
                ↓
         Preprocessing Stage
                ↓
    Parallel AI Processing Modules
 ┌────────────┬────────────┬────────────┐
 │ Resume NLP │ Speech AI  │ Vision AI  │
 └────────────┴────────────┴────────────┘
                ↓
         Score Calculation
                ↓
       Feedback Generation
                ↓
        Results Dashboard
```

---

# Technologies Used

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Core programming language |
| Streamlit    | Frontend dashboard        |
| OpenCV       | Video processing          |
| Whisper AI   | Speech-to-text            |
| DeepFace     | Emotion detection         |
| Scikit-learn | NLP similarity analysis   |
| NLTK         | Text preprocessing        |
| pdfplumber   | Resume text extraction    |
| Plotly       | Data visualization        |

---

# Project Structure

```text
smart-interview-assistant/
│
├── app.py
├── requirements.txt
├── resumes/
├── job_descriptions/
├── videos/
├── outputs/
├── screenshots/
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/smart-interview-assistant.git
```

---

## Navigate to Project Folder

```bash
cd smart-interview-assistant
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Required Libraries

```text
streamlit
pdfplumber
scikit-learn
nltk
moviepy
openai-whisper
opencv-python
deepface
plotly
```

---

# Run the Project

```bash
streamlit run app.py
```

---

# Input Requirements

## Resume

* PDF format

## Job Description

* Text input or `.txt` file

## Interview Video

* MP4 format

---

# Output Generated

The system generates:

* Resume Match Percentage
* Missing Skills
* Transcript
* Speech Metrics
* Emotion Analysis
* Final Candidate Score
* AI Feedback

---

# Example Output

```text
Resume Match: 82%

Speech Analysis:
- WPM: 118
- Filler Words: 5

Emotion:
- Dominant Emotion: Confident

Final Score: 79/100

Feedback:
- Improve Docker skills
- Reduce filler words
- Maintain eye contact
```

---

# Datasets Used

| Dataset                 | Purpose                   |
| ----------------------- | ------------------------- |
| Resume Dataset          | Resume analysis           |
| FER2013                 | Emotion detection         |
| Sample Interview Videos | Speech & emotion analysis |
| Custom Job Descriptions | Resume matching           |

---

# Algorithms and Models

| Module             | Technique                  |
| ------------------ | -------------------------- |
| Resume Matching    | TF-IDF + Cosine Similarity |
| Speech Recognition | Whisper AI                 |
| Emotion Detection  | DeepFace                   |
| Text Processing    | NLP                        |
| Final Scoring      | Weighted Formula           |

---

# Scoring Formula

Final score calculation:

[
Final Score = 0.4(Resume Score) + 0.3(Speech Score) + 0.3(Emotion Score)
]

---

# Advantages

* Automated interview evaluation
* Faster recruitment process
* Objective candidate analysis
* Personalized feedback generation
* AI-based analytics dashboard

---

# Limitations

* Emotion detection depends on video quality
* Background noise affects speech analysis
* Resume formats may vary

---

# Future Enhancements

* Real-time AI interviewer
* Adaptive question generation
* Multi-language support
* Candidate ranking system
* Cloud deployment
* Mobile application

---

# Applications

* Recruitment systems
* Mock interview platforms
* University placement training
* Corporate HR analytics
* Online interview evaluation

---

# Screenshots

```text
screenshots/<img width="1875" height="962" alt="Screenshot 2026-05-14 122146" src="https://github.com/user-attachments/assets/0323bbd7-7962-45aa-ad04-30e442b2fc15" />
<img width="1896" height="992" alt="Screenshot 2026-05-14 122122" src="https://github.com/user-attachments/assets/9d7ac6f6-5540-44cf-a4bf-686741ddc41a" />


# Conclusion

The Smart Interview Assistant demonstrates the integration of NLP, Speech Processing, and Computer Vision technologies into a unified AI-powered recruitment support system. The project automates interview evaluation and provides meaningful insights into candidate performance through intelligent analysis and feedback generation.

---

# References

* OpenCV Documentation
* Whisper AI
* DeepFace
* Scikit-learn
* Streamlit
* NLTK
* TensorFlow
<img width="4" height="4" alt="Screenshot 2026-05-10 061527" src="https://github.com/user-attachments/assets/59cc198c-a591-4253-8ae8-6ccd404c8325" />
<img width="1896" height="992" alt="Screenshot 2026-05-14 122122" src="https://github.com/user-attachments/assets/bc779ab2-f484-43fc-adb0-6fcc96c4d0f5" />


# Author

L Mounika
B.Tech AI & ML
# License

This project is developed for educational and academic purposes.
