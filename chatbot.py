import pandas as pd
import difflib
import os
from IPython.display import display
import ipywidgets as widgets

# Step 1: Create and save the FAQ data
data = {
    "Question Keyword": [
        "courses offered", "semester start", "tuition fee", "exam schedule", "academic calendar",
        "admission deadline", "result date", "syllabus", "study material", "fee payment",
        "hostel facilities", "scholarship options", "library access", "placement support",
        "internship support", "transport facility", "department contact", "leave application",
        "attendance rules", "revaluation process"
    ],
    "Answer": [
        "Our college offers B.E, B.Tech, M.E, and MBA programs.",
        "The semester starts on July 15, 2025.",
        "Tuition fee varies by course. For B.E: ₹75,000 per year.",
        "Exam schedule will be available on the college portal.",
        "You can find it at /downloads/academic_calendar.pdf",
        "The last date for admission is June 30, 2025.",
        "Results will be announced in the first week of August.",
        "All course syllabi are available on the student portal.",
        "Study materials are shared by faculty via the LMS portal.",
        "Fees can be paid online through the college payment gateway.",
        "Yes, hostel facilities are available for both boys and girls.",
        "Merit-based and need-based scholarships are available.",
        "Library is open from 8 AM to 8 PM on all working days.",
        "We offer 100% placement assistance through our placement cell.",
        "Students can apply for internships through the college portal.",
        "College buses are available on major city routes.",
        "Department contacts are available on the official website.",
        "Leave applications can be submitted through the student portal.",
        "Minimum 75% attendance is required to appear for exams.",
        "Revaluation forms are available one week after result publication."
    ]
}

faq_df = pd.DataFrame(data)
faq_df.to_csv('faq.csv', index=False)

# Step 2: Load FAQ and prepare
faq_df = pd.read_csv('faq.csv')
faq_df['Question Keyword'] = faq_df['Question Keyword'].str.lower()

log_filename = "user_questions_log.csv"
if not os.path.exists(log_filename):
    pd.DataFrame(columns=["User Question"]).to_csv(log_filename, index=False)

# Greetings and help
greetings = ["hi", "hello", "hey", "good morning", "good afternoon"]
help_text = "You can ask about: " + ", ".join(faq_df['Question Keyword'].tolist())

# Step 3: Define chatbot response logic
def chatbot_response(user_input):
    user_input = user_input.lower()
    log_question(user_input)

    if user_input in greetings:
        return "Hello! I'm Smart EduBot. How can I help you today?"

    if "help" in user_input or "topics" in user_input:
        return help_text

    matches = difflib.get_close_matches(user_input, faq_df['Question Keyword'], n=1, cutoff=0.4)
    if matches:
        matched_row = faq_df[faq_df['Question Keyword'] == matches[0]]
        return matched_row['Answer'].values[0]

    for _, row in faq_df.iterrows():
        if row['Question Keyword'] in user_input:
            return row['Answer']

    return "I'm sorry, I didn't understand that. Type 'help' to see what I can answer."

# Step 4: Logging function
def log_question(question):
    log_df = pd.read_csv(log_filename)
    new_entry = pd.DataFrame({"User Question": [question]})
    log_df = pd.concat([log_df, new_entry], ignore_index=True)
    log_df.to_csv(log_filename, index=False)

# Step 5: Create interface in Colab
input_box = widgets.Textarea(
    placeholder='Type your questions here, one per line...',
    layout=widgets.Layout(width='100%', height='120px')
)
button = widgets.Button(description="Ask Smart EduBot", button_style='success')
output = widgets.Output()

def on_button_click(b):
    output.clear_output()
    questions = input_box.value.strip().split('\n')
    with output:
        for q in questions:
            if q.strip():
                print(f"You: {q}")
                print(f"Smart EduBot: {chatbot_response(q)}\n")

button.on_click(on_button_click)

# Display form
display(input_box, button, output)
