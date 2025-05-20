# Smart EduBot: AI Chatbot for Educational Support

## Description
Smart EduBot is an AI-based chatbot designed to assist students, parents, and academic staff by answering queries related to academic services such as admissions, fee structure, syllabus, exam schedule, and more. It enhances educational interaction and support using natural language understanding.

## Features
- Answers 20+ commonly asked academic FAQs.
- Greets users and understands help-related queries.
- Fuzzy matching for improved response accuracy.
- Logs all user questions for analysis.
- Easy-to-extend CSV-based FAQ database.

## Dataset
- **Source:** Custom-built dataset of FAQs from academic contexts.
- **Size:** 20 question-answer pairs.
- **Attributes:** `Question Keyword`, `Answer`
- **Label:** N/A (Rule-based model, not supervised learning)
- **Preprocessing:** Lowercasing, keyword matching, fuzzy logic.

## How to Run It
1. Install Python and required libraries: `pandas`, `difflib`
2. Run the script: `python chatbot.py`
3. Type questions in the terminal to get responses.
4. Logs are saved in `user_questions_log.csv`.

## Contributors
- **V.S. Vasanthh** – Lead Developer, Model Building
- **Vetrivel Murugan M.** – Dataset Preparation, UI
- **Thirumalai B.** – Evaluation, Testing
- **Vishvarajan S.** – Documentation, Deployment
