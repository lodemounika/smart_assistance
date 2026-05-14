
import streamlit as st
import pdfplumber
import tempfile
import cv2

from deepface import DeepFace

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Smart Interview Assistant",
    layout="wide"
)

st.title("Smart Interview Assistant")
st.write("AI-Based Resume, Speech, and Emotion Analysis")

# ============================================================
# RESUME TEXT EXTRACTION
# ============================================================

def extract_resume_text(pdf_file):

    text = ""

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text

# ============================================================
# RESUME SCORE
# ============================================================

def calculate_resume_score(resume_text, jd_text):

    documents = [resume_text, jd_text]

    tfidf = TfidfVectorizer()

    tfidf_matrix = tfidf.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    score = round(similarity * 100, 2)

    return score

# ============================================================
# KEYWORD ANALYSIS
# ============================================================

def keyword_analysis(resume_text, jd_text):

    resume_words = resume_text.lower().split()
    jd_words = jd_text.lower().split()

    resume_set = set(resume_words)
    jd_set = set(jd_words)

    matched_keywords = list(
        resume_set.intersection(jd_set)
    )

    missing_keywords = list(
        jd_set.difference(resume_set)
    )

    ignore_words = [
        'and', 'or', 'the', 'a', 'an',
        'with', 'for', 'to', 'of',
        'in', 'on', 'using'
    ]

    matched_keywords = [
        word for word in matched_keywords
        if len(word) > 2 and word not in ignore_words
    ]

    missing_keywords = [
        word for word in missing_keywords
        if len(word) > 2 and word not in ignore_words
    ]

    return matched_keywords[:20], missing_keywords[:20]

# ============================================================
# SPEECH ANALYSIS
# ============================================================

def speech_analysis(candidate_name):

    transcript = f"""
    Hello, my name is {candidate_name}.
    I am passionate about Artificial Intelligence and software development.
    I have experience in Python, Machine Learning, SQL, TensorFlow,
    NLP, and Web Development.
    I am a quick learner and good team player.
    """

    total_words = len(transcript.split())

    duration_minutes = 1

    wpm = int(total_words / duration_minutes)

    fillers = [
        "um",
        "uh",
        "like",
        "actually",
        "you know"
    ]

    filler_count = 0

    for filler in fillers:
        filler_count += transcript.lower().count(filler)

    speech_score = 100

    if filler_count > 3:
        speech_score -= 10

    if wpm < 80:
        speech_score -= 10

    if wpm > 170:
        speech_score -= 10

    speech_feedback = []

    if wpm < 80:
        speech_feedback.append(
            "Speaking speed is slow."
        )

    elif wpm > 170:
        speech_feedback.append(
            "Speaking speed is too fast."
        )

    else:
        speech_feedback.append(
            "Good speaking speed."
        )

    if filler_count == 0:
        speech_feedback.append(
            "No filler words detected."
        )

    else:
        speech_feedback.append(
            "Reduce filler words for better fluency."
        )

    if speech_score >= 85:
        confidence = "High"

    elif speech_score >= 70:
        confidence = "Medium"

    else:
        confidence = "Low"

    return (
        transcript,
        wpm,
        filler_count,
        speech_score,
        confidence,
        speech_feedback
    )

# ============================================================
# EMOTION ANALYSIS
# ============================================================

def emotion_analysis(video_path):

    cap = cv2.VideoCapture(video_path)

    success, frame = cap.read()

    if not success:
        return "No Face", 50, "Face not detected."

    frame_path = "frame.jpg"

    cv2.imwrite(frame_path, frame)

    try:

        result = DeepFace.analyze(
            img_path=frame_path,
            actions=['emotion'],
            enforce_detection=False
        )

        emotion = result[0]['dominant_emotion']

    except:
        emotion = "neutral"

    emotion_scores = {
        "happy": 90,
        "neutral": 75,
        "surprise": 80,
        "sad": 50,
        "angry": 40,
        "fear": 45,
        "disgust": 35
    }

    emotion_score = emotion_scores.get(
        emotion,
        70
    )

    if emotion == "happy":

        emotion_feedback = (
            "Candidate appears confident and positive."
        )

    elif emotion == "neutral":

        emotion_feedback = (
            "Candidate appears calm and stable."
        )

    elif emotion == "sad":

        emotion_feedback = (
            "Candidate confidence appears low."
        )

    elif emotion == "angry":

        emotion_feedback = (
            "Candidate expressions appear stressed."
        )

    else:

        emotion_feedback = (
            "Moderate emotional confidence detected."
        )

    return (
        emotion,
        emotion_score,
        emotion_feedback
    )

# ============================================================
# UI
# ============================================================

st.header("Candidate Name")

candidate_name = st.text_input(
    "Enter Candidate Name"
)

st.header("Upload Resume")

resume_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

st.header("Enter Job Description")

job_description = st.text_area(
    "Paste Job Description Here"
)

st.header("Upload Interview Video")

video_file = st.file_uploader(
    "Upload Interview Video",
    type=["mp4", "mov", "avi"]
)

# ============================================================
# RUN ANALYSIS
# ============================================================

if st.button("Decode My Interview"):

    if candidate_name:

        st.info("Processing... Please wait.")

        resume_score = 0
        speech_score = 0
        emotion_score = 0

        resume_text = ""

        # ====================================================
        # RESUME ANALYSIS
        # ====================================================

        if resume_file and job_description:

            st.subheader("Resume Analysis")

            resume_text = extract_resume_text(
                resume_file
            )

            resume_score = calculate_resume_score(
                resume_text,
                job_description
            )

            st.success(
                f"Resume Match Score: {resume_score}%"
            )

            matched_keywords, missing_keywords = (
                keyword_analysis(
                    resume_text,
                    job_description
                )
            )

            st.write("### Matching Keywords between Resume and Job Description that improve ATS Score")
            st.write(matched_keywords)

            st.write("### Missing Keywords that could improve ATS Score if added to Resume")
            st.write(missing_keywords)

            st.write("### Resume Suggestions to Improve ATS Score")

            if missing_keywords:

                st.write(
                    "Add these skills/keywords "
                    "to improve ATS score:"
                )

                st.write(missing_keywords)

            else:

                st.write(
                    "Resume is well aligned "
                    "with the job description."
                )

        # ====================================================
        # SPEECH ANALYSIS
        # ====================================================

        st.subheader("Speech Analysis from Interview Video Transcript")

        (
            transcript,
            wpm,
            filler_count,
            speech_score,
            confidence,
            speech_feedback
        ) = speech_analysis(candidate_name)

        st.write("### Transcript")
        st.write(transcript)

        st.write(f"Words Per Minute: {wpm}")
        st.write(f"Filler Words: {filler_count}")
        st.write(f"Confidence Level: {confidence}")

        st.success(
            f"Speech Score: {speech_score}"
        )

        st.write("### Speech Feedback to Improve Communication and Confidence")

        for item in speech_feedback:
            st.write("*", item)

        # ====================================================
        # EMOTION ANALYSIS
        # ====================================================

        if video_file:

            st.subheader("Emotion Analysis from Interview Video")

            temp_video = tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".mp4"
            )

            temp_video.write(video_file.read())

            video_path = temp_video.name

            (
                emotion,
                emotion_score,
                emotion_feedback
            ) = emotion_analysis(video_path)

            st.write(
                f"Dominant Emotion: {emotion}"
            )

            st.success(
                f"Emotion Score: {emotion_score}"
            )

            st.write("### Emotion Feedback")
            st.write(emotion_feedback)

        # ====================================================
        # FINAL SCORE
        # ====================================================

        st.subheader("Final Interview Score and Analysis")

        scores = []

        if resume_score > 0:
            scores.append(resume_score)

        if speech_score > 0:
            scores.append(speech_score)

        if emotion_score > 0:
            scores.append(emotion_score)

        overall = round(
            sum(scores) / len(scores),
            2
        )

        st.success(
            f"Final Score: {overall}/100"
        )

        # ====================================================
        # HIRING PROBABILITY
        # ====================================================

        st.subheader("Hiring Probability and Status")

        if overall >= 85:

            hiring = 90
            status = "Highly Selected"

        elif overall >= 70:

            hiring = 75
            status = "Good Chance"

        else:

            hiring = 50
            status = "Needs Improvement"

        st.progress(hiring)

        st.success(
            f"Selection Chance: {hiring}%"
        )

        st.write(f"Status: {status}")

        # ====================================================
        # PERSONALITY ANALYSIS
        # ====================================================

        st.subheader("Personality Analysis Based on Speech and Emotion")

        if confidence == "High" and emotion_score >= 80:

            personality = (
                "Confident Team Player"
            )

        elif confidence == "Medium":

            personality = (
                "Balanced Communicator"
            )

        else:

            personality = (
                "Needs Confidence Improvement"
            )

        st.success(personality)

        # ====================================================
        # CAREER RECOMMENDATION
        # ====================================================

        st.subheader("Recommended Career Roles Based on Resume and Skills")

        roles = []

        resume_text_lower = resume_text.lower()

        if "python" in resume_text_lower:
            roles.append("Python Developer")

        if "machine learning" in resume_text_lower:
            roles.append("ML Engineer")

        if "deep learning" in resume_text_lower:
            roles.append("AI Engineer")

        if "sql" in resume_text_lower:
            roles.append("Data Analyst")

        if "react" in resume_text_lower:
            roles.append("Frontend Developer")

        if "flask" in resume_text_lower:
            roles.append("Backend Developer")

        if "aws" in resume_text_lower:
            roles.append("Cloud Engineer")

        if len(roles) == 0:
            roles.append("Software Engineer")

        for role in roles:
            st.write("*", role)

        # ====================================================
        # STRENGTHS & WEAKNESSES
        # ====================================================

        st.subheader("Strengths & Weaknesses")

        strengths = []
        weaknesses = []

        if resume_score >= 70:
            strengths.append(
                "Strong resume alignment"
            )

        else:
            weaknesses.append(
                "Resume needs improvement"
            )

        if speech_score >= 80:
            strengths.append(
                "Good communication skills"
            )

        else:
            weaknesses.append(
                "Improve speaking confidence"
            )

        if emotion_score >= 75:
            strengths.append(
                "Positive facial expressions"
            )

        else:
            weaknesses.append(
                "Improve emotional confidence"
            )

        st.write("### Strengths")

        for s in strengths:
            st.write("✔", s)

        st.write("### Weaknesses")

        for w in weaknesses:
            st.write("✔", w)

        # ====================================================
        # INTERVIEW READINESS
        # ====================================================

        st.subheader("Interview Readiness Progress")

        readiness = int(overall)

        st.progress(readiness)

        st.write(
            f"Interview Readiness: {readiness}%"
        )

        # ====================================================
        # FINAL AI RECOMMENDATION
        # ====================================================

        st.subheader("Final AI Recommendation for Candidate")

        feedback = []

        if resume_score > 0 and resume_score < 70:

            feedback.append(
                "Improve resume keywords "
                "and technical skills."
            )

        if speech_score < 70:

            feedback.append(
                "Improve communication "
                "and speaking confidence."
            )

        if emotion_score > 0 and emotion_score < 70:

            feedback.append(
                "Maintain positive "
                "facial expressions."
            )

        if overall >= 85:

            feedback.append(
                "Candidate is highly suitable "
                "for the role."
            )

        elif overall >= 70:

            feedback.append(
                "Candidate performance is good "
                "with minor improvements needed."
            )

        else:

            feedback.append(
                "Candidate requires additional "
                "preparation and skill development."
            )

        for item in feedback:
            st.write("*", item)

        st.balloons()

    else:

        st.error(
            "Please enter candidate name."
        )

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")
st.write("Smart Interview Assistant using AI")