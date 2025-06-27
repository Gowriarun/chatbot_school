from flask import Flask, request, jsonify, render_template_string
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

app = Flask(__name__)

# Create chatbot instance
chatbot = ChatBot('SchoolBot')

# Train on general English conversations
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train('chatterbot.corpus.english')

# Custom school-specific conversations
custom_conversations = [
    ["Who is the principal?", "The principal is Fr. Suresh Kumar SDB."],
["Who’s the principal?", "The principal is Fr. Suresh Kumar SDB."],
["Who is the school principal?", "The principal is Fr. Suresh Kumar SDB."],
["Who is principal?", "The principal is Fr. Suresh Kumar SDB."],
["whos the principal", "The principal is Fr. Suresh Kumar SDB."],
["Who heads the school?", "The principal is Fr. Suresh Kumar SDB."],
["Who leads the school?", "The principal is Fr. Suresh Kumar SDB."],
["Can you tell me the principal's name?", "The principal is Fr. Suresh Kumar SDB."],
["May I know who the principal is?", "The principal is Fr. Suresh Kumar SDB."],
["Who runs the school?", "The principal is Fr. Suresh Kumar SDB."],
["Who is in charge of the school?", "The principal is Fr. Suresh Kumar SDB."],
["Please tell me the name of the principal.", "The principal is Fr. Suresh Kumar SDB."],
["Who is the headmaster?", "The principal is Fr. Suresh Kumar SDB."],
["Who is Fr. Suresh Kumar SDB?", "He is the principal of the school."],
["What are the school timings?", "School starts at 7:30 AM and ends at 2:05 PM."],
["What time does school start and end?", "School starts at 7:30 AM and ends at 2:05 PM."],
["What time does school start?", "School starts at 7:30 AM."],
["What time does school finish?", "School ends at 2:05 PM."],
["When does school begin?", "School starts at 7:30 AM."],
["When does school end?", "School ends at 2:05 PM."],
["Can you tell me the school hours?", "School starts at 7:30 AM and ends at 2:05 PM."],
["When do classes start?", "Classes begin at 7:30 AM."],
["When do classes end?", "Classes end at 2:05 PM."],
["At what time should students arrive?", "School starts at 7:30 AM."],
["At what time can students leave?", "School ends at 2:05 PM."],
["What is the daily schedule?", "School starts at 7:30 AM and ends at 2:05 PM, with a break at 10:30 AM."],
["What are the school timings on Friday?", "On Fridays, the school finishes at 11:30 AM."],
["When does school end on Friday?", "On Fridays, the school ends at 11:30 AM."],
["What is the schedule for Fridays?", "On Fridays, school finishes at 11:30 AM."],
["Is Friday a half day?", "On Fridays, school finishes at 11:30 AM."],
["Are Friday timings different?", "Yes, school ends at 11:30 AM on Fridays."],
["How long is school on Friday?", "School is from 7:30 AM to 11:30 AM on Fridays."],
["When do classes finish on Friday?", "On Fridays, classes finish at 11:30 AM."],
["When is the break time?", "There is a 20-minute break at 10:30 AM."],
["What time is the break?", "Break is at 10:30 AM for 20 minutes."],
["When do students have break?", "Students have a break at 10:30 AM."],
["Is there a break during school hours?", "Yes, there is a 20-minute break at 10:30 AM."],
["What time is recess?", "Recess is at 10:30 AM."],
["How long is the break?", "Break lasts for 20 minutes at 10:30 AM."],
["When is recess?", "Recess is at 10:30 AM."],
["Which days are holidays?", "Saturday and Sunday are holidays."],
["What days is the school closed?", "Saturday and Sunday are school holidays."],
["Are there classes on Saturday?", "No, Saturday and Sunday are holidays."],
["Is Saturday a holiday?", "Yes, Saturday and Sunday are holidays."],
["Is Sunday a holiday?", "Yes, Sunday is a holiday."],
["Are weekends off?", "Yes, Saturday and Sunday are school holidays."],
["Are there classes on weekends?", "No, there are no classes on Saturday and Sunday."],
["When is the weekend?", "Saturday and Sunday are holidays."],
["How can I contact the school?", "You can call the school office or visit our contact page on the website."],
["What is the school phone number?", "Please check the school website or contact the school office for the phone number."],
["How do I email the school?", "Please visit our website's contact page to send us an email."],
["How do I reach the school?", "You can contact the school office or use the contact page on our website."],
["Where can I find the school's contact information?", "Please visit the contact page on the school website."],
["I want to call the school. What is the number?", "Please check the contact page on our website for the school phone number."],
["Can you give me the school's contact details?", "Please check our website's contact page for all details."],
["Who do I call for admission info?", "Please contact the school office or visit the admissions page on the website."],
["How do I apply for KG1 or KG2?", "Children enrolling in KG1 or KG2 must be four years old on or before August 31 for schools starting September."],
["How do I get admission in KG1?", "Children enrolling in KG1 must be four years old on or before August 31 for schools starting September."],
["How do I get my child into KG2?", "Children enrolling in KG2 must be four years old on or before August 31 for schools starting September."],
["What is the admission process for KG1?", "Children enrolling in KG1 must be four years old on or before August 31 for schools starting September."],
["How much is the fee for Grade 7?", "The annual tuition fee for Grade 7 is 11,200 AED, payable in three installments."],
["What is the fee for Grade 7?", "The annual tuition fee for Grade 7 is 11,200 AED, payable in three installments."],
["How much is the fee for Grade 8?", "The annual tuition fee for Grade 8 is 11,200 AED, payable in three installments."],
["What is the fee for Grade 8?", "The annual tuition fee for Grade 8 is 11,200 AED, payable in three installments."],
["How much is the fee for Grade 4?", "The annual tuition fee for Grade 4 is 9,100 AED, payable in three installments."],
["How much is the fee for Grade 5?", "The annual tuition fee for Grade 5 is 9,100 AED, payable in three installments."],
["How much is the fee for Grade 6?", "The annual tuition fee for Grade 6 is 9,100 AED, payable in three installments."],
["How much is the fee for Grade 9?", "The annual tuition fee for Grade 9 is 13,100 AED, payable in three installments."],
["How much is the fee for Grade 10?", "The annual tuition fee for Grade 10 is 13,100 AED, payable in three installments."],
["How much is the fee for Grade 11?", "The annual tuition fee for Grade 11 is 15,900 AED, payable in three installments."],
["How much is the fee for Grade 12?", "The annual tuition fee for Grade 12 is 15,900 AED, payable in three installments."],
["How much is the fee for A Level?", "The annual tuition fee for A' Level is 15,900 AED, payable in three installments."],
["How can I get admission to Grade 1?", "Admission is based on an entrance test in English and Mathematics, 1 hour each. Admission is competitive as there are limited seats."],
["How can I get admission to Grade 1 to 9?", "Admission is based on an entrance test in English and Mathematics, 1 hour each. Admission is competitive as there are limited seats."],
["Is there an entrance test for Grade 1?", "Yes, admission is based on an entrance test in English and Mathematics."],
["How do I join A Level?", "A’ level enrollment starts in August after O’ level results. Students should have completed O’ level/Grade 10 with six subjects (including English and Math) and grade A in chosen A’ level subjects."],
["How do I get into Grade 11?", "Enrollment for Grade 11 begins after O' Level results are out and is only for students who passed UK Board Exams with at least A*/A; 9-7."],
["How do I get admission to Grade 12?", "Admission to Grade 12 (Advanced Level) is for students who have completed Advance Subsidiary level in the Edexcel Board with minimum grade A and B."],
["What documents are required for admission?", "Required documents: child’s passport with valid visa, birth certificate, vaccination card, Emirates ID, six passport photos, latest report card, reference letter, original transfer certificate, bonafide certificate, medical record book, and (for UAE nationals) family book."],
["Which documents are needed for admission?", "You will need your child’s passport, valid visa, Emirates ID, photos, transfer certificate, and medical record, among others."],
["What paperwork do I need for admission?", "You need the child's passport, visa, Emirates ID, birth certificate, photos, transfer certificate, medical record, etc."],
["What certificates are needed for admission?", "You need a transfer certificate, birth certificate, Emirates ID, and other documents for admission."],
["Do I need to submit photos for admission?", "Yes, six passport size photos are required."],
["Is a medical record required?", "Yes, a medical record is required for admission."],
["What if I am transferring from another UAE school?", "Certificates must be attested by the Ministry of Education in the concerned Educational Zone."],
["What if I am transferring from abroad?", "Certificates must be attested by the Regional Educational Office in your country, the UAE embassy/consulate, and UAE Ministry of Foreign Affairs."],
["What is the tuition fee for KG1?", "The annual tuition fee for KG1 is 7,270 AED, payable in three installments."],
["How much is the fee for KG1?", "The annual tuition fee for KG1 is 7,270 AED."],
["What is the tuition fee for KG2?", "The annual tuition fee for KG2 is 7,270 AED, payable in three installments."],
["How much is the fee for KG2?", "The annual tuition fee for KG2 is 7,270 AED."],
["What is the tuition fee for Grade 1?", "The annual tuition fee for Grade 1 is 8,100 AED, payable in three installments."],
["How much is the fee for Grade 1?", "The annual tuition fee for Grade 1 is 8,100 AED."],
["What is the tuition fee for Grade 9?", "The annual tuition fee for Grade 9 is 13,100 AED, payable in three installments."],
["What is the tuition fee for A' Level?", "The annual tuition fee for A' Level is 15,900 AED, payable in three installments."],
["How do I pay school fees?", "Fees are payable in three installments. Please contact the school office for payment procedures."],
["When are the fees due?", "Fees are payable in three installments. Please contact the school office for the exact due dates."],
["Can I pay fees online?", "Please contact the school office for information on online fee payment options."],
["Is there a fee discount?", "Please contact the school office for information about any available discounts."],
["How do I apply for KG1 or KG2?", "Children enrolling in KG1 or KG2 must be four years old on or before August 31 for schools starting September."],
["How can I get admission for KG1?", "Children enrolling in KG1 must be four years old on or before August 31 for schools starting September."],
["How can I get admission for KG2?", "Children enrolling in KG2 must be four years old on or before August 31 for schools starting September."],
["What is the age requirement for KG1/KG2?", "Children enrolling in KG1 or KG2 must be four years old on or before August 31 for schools starting September."],
["How do I get admission to Grade 1 to Grade 9?", "Admission is based on an entrance test in English and Mathematics, 1 hour each. Admission is competitive as there are limited seats."],
["What is the admission process for Grade 1 to 9?", "Admission is based on an entrance test in English and Mathematics, 1 hour each. Admission is competitive as there are limited seats."],
["Is there an entrance exam for Grade 1?", "Yes, admission to Grade 1 is based on an entrance test in English and Mathematics, 1 hour each."],
["How do I get admission to Grade 1?", "Admission is based on an entrance test in English and Mathematics, 1 hour each. Admission is competitive as there are limited seats."],
["Are there admissions for Grade 10?", "There will be no new admissions for Grade 10 as students are preparing for the London Board Exams."],
["Can I join in Grade 10?", "There will be no new admissions for Grade 10 as students are preparing for the London Board Exams."],
["Is admission open for Grade 10?", "There will be no new admissions for Grade 10 as students are preparing for the London Board Exams."],
["How do I get admission to Grade 11?", "Enrollment for Grade 11 begins after O' Level results are out and is only for students who passed UK Board Exams with at least A*/A; 9-7."],
["When does admission start for Grade 11?", "Enrollment for Grade 11 begins after O' Level results are out and is only for students who passed UK Board Exams with at least A*/A; 9-7."],
["Can I apply for Grade 11?", "Enrollment for Grade 11 begins after O' Level results are out and is only for students who passed UK Board Exams with at least A*/A; 9-7."],
["What are the requirements for A’ level admissions?", "A’ level enrollment starts in August after O’ level results. Students should have completed O’ level/Grade 10 with six subjects (including English and Math) and grade A in chosen A’ level subjects."],
["How do I join A’ level?", "A’ level enrollment starts in August after O’ level results. Students should have completed O’ level/Grade 10 with six subjects (including English and Math) and grade A in chosen A’ level subjects."],
["How do I get admission to Grade 12?", "Admission to Grade 12 (Advanced Level) is for students who have completed Advance Subsidiary level in the Edexcel Board with minimum grade A and B."],
["What is needed to join Grade 12?", "Admission to Grade 12 (Advanced Level) is for students who have completed Advance Subsidiary level in the Edexcel Board with minimum grade A and B."],
["What documents are required for admission?", "Required documents: child’s passport with valid visa, birth certificate, vaccination card, Emirates ID, six passport photos, latest report card, reference letter, original transfer certificate, bonafide certificate, medical record book, and (for UAE nationals) family book."],
["Which documents are needed for admission?", "Required documents: child’s passport with valid visa, birth certificate, vaccination card, Emirates ID, six passport photos, latest report card, reference letter, original transfer certificate, bonafide certificate, medical record book, and (for UAE nationals) family book."],
["What paperwork do I need for admission?", "Required documents: child’s passport with valid visa, birth certificate, vaccination card, Emirates ID, six passport photos, latest report card, reference letter, original transfer certificate, bonafide certificate, medical record book, and (for UAE nationals) family book."],
["Do I need a transfer certificate?", "Yes, you need a transfer certificate for admission."],
["What if I am transferring from another UAE school?", "Certificates must be attested by the Ministry of Education in the concerned Educational Zone."],
["I'm moving from another UAE school. What do I need?", "Certificates must be attested by the Ministry of Education in the concerned Educational Zone."],
["What if I am transferring from abroad?", "Certificates must be attested by the Regional Educational Office in your country, the UAE embassy/consulate, and UAE Ministry of Foreign Affairs."],
["I'm moving from outside UAE. What do I need?", "Certificates must be attested by the Regional Educational Office in your country, the UAE embassy/consulate, and UAE Ministry of Foreign Affairs."],
["What is the tuition fee for KG1?", "The annual tuition fee for KG1 is 7,270 AED, payable in three installments."],
["How much is the KG1 fee?", "The annual tuition fee for KG1 is 7,270 AED, payable in three installments."],
["What is the tuition fee for KG2?", "The annual tuition fee for KG2 is 7,270 AED, payable in three installments."],
["How much is the KG2 fee?", "The annual tuition fee for KG2 is 7,270 AED, payable in three installments."],
["What is the tuition fee for Grade 1?", "The annual tuition fee for Grade 1 is 8,100 AED, payable in three installments."],
["How much is the Grade 1 fee?", "The annual tuition fee for Grade 1 is 8,100 AED, payable in three installments."],
["What is the tuition fee for Grade 9?", "The annual tuition fee for Grade 9 is 13,100 AED, payable in three installments."],
["How much is the Grade 9 fee?", "The annual tuition fee for Grade 9 is 13,100 AED, payable in three installments."],
["What is the tuition fee for A' Level?", "The annual tuition fee for A' Level is 15,900 AED, payable in three installments."],
["How much is the A' Level fee?", "The annual tuition fee for A' Level is 15,900 AED, payable in three installments."],
["How do I pay school fees?", "Fees are payable in three installments. Please contact the school office for payment procedures."],
["How to pay fees?", "Fees are payable in three installments. Please contact the school office for payment procedures."],
["Can I pay the fees in installments?", "Yes, fees are payable in three installments."],
["How do I pay fees online?", "Please contact the school office for payment procedures."],
["Is it compulsory to take two A' Level subjects?", "Yes, it is compulsory for students enrolling for A' Level to take two subjects. Permission for a third subject is at the principal’s discretion."],
["Do I have to take two A' Level subjects?", "Yes, it is compulsory for students enrolling for A' Level to take two subjects. Permission for a third subject is at the principal’s discretion."],
["Is it required to choose two A' Levels?", "Yes, it is compulsory for students enrolling for A' Level to take two subjects. Permission for a third subject is at the principal’s discretion."],
["Can I register for courses or exams elsewhere while registered at this school?", "No, students registered at this school are not permitted to register elsewhere for courses or exams."],
["Can I take exams at other schools?", "No, students registered at this school are not permitted to register elsewhere for courses or exams."],
["Can I register for external exams?", "No, students registered at this school are not permitted to register elsewhere for courses or exams."],
["How can I contact the school office?", "Please call the school office or visit our contact page on the website."],
["How do I contact the school office?", "Please call the school office or visit our contact page on the website."],
["Who do I call for more information?", "Please call the school office or visit our contact page on the website."],
["Where can I find the school contact number?", "Please call the school office or visit our contact page on the website."],
["Who is the school sponsor?", "The school sponsor is H.E. Dr. Mohamed Saeed Al kindi."],
["Who is the owner of the school?", "His Excellency Bishop Paolo Martinelli is the owner of the school."],
["Who is the managing director?", "The managing director is Mr. Joseph Flynn."],
["Who is the vice principal for UK curriculum?", "Ms. Simmy is the Vice Principal for UK curriculum."],
["Who is the vice principal for CBSE curriculum?", "Mr. Edward Maria is the Vice Principal for CBSE curriculum."],
["Who is the academic supervisor for UK curriculum?", "Mr. Sekar is the Academic Supervisor for UK curriculum."],
["Who is the junior supervisor for UK curriculum?", "Ms. Lissy is the Junior Supervisor for UK curriculum."],
["Who is the KG supervisor?", "Ms. Fathima is the KG Supervisor for both UK and CBSE curriculum."],
["Who is the administrator?", "Fr. Rozario is the Administrator."],
["Who are the counselors?", "The counselors are Ms. Marwa Mostafa, Ms. Hala Walid, and Ms. Silviya Kulandai."],
["Who is the Head of Inclusion?", "Ms. Anjana Warrier is the Head of Inclusion."],
["Who is the special educator?", "Dr. Sruthi Sood is the Special Educator."],
["What are the age requirements for KG1 and KG2?", "Children enrolling in KG1 or KG2 must be four years old on or before August 31 for schools starting September."],
["What is the entrance test for admission to Grade 1 to 9?", "Admission is based on an entrance test in English and Mathematics, each for 1 hour. Entrance is competitive as the number of applicants exceeds available seats."],
["Is admission open for Grade 10?", "There will be no new admissions for Grade 10 as students are preparing for the London Board Exams."],
["How do I get admission to Grade 11?", "Enrollment for Grade 11 begins after O' Level results and is available to students who have passed UK Board Exams with at least A*/A (grades 9–7)."],
["When does A Level admission begin?", "Enrollment for A Level begins in August after the O Level/Grade 10 results are declared."],
["Who is eligible for A Level admission?", "To be eligible for A Level, students must have completed O Level/Grade 10 with six subjects including English language and Mathematics, and have secured Grade A in the subjects chosen for A Level."],
["How do I get admission to Grade 12?", "Admission to Grade 12 (Advanced Level) is for students who have completed Advance Subsidiary level in the Edexcel Board with minimum grades A and B."],
["When will I know the result of the entrance exam?", "Only applicants who have been selected will receive a call informing them of the date and time for registration."],
["Is it compulsory to take two A Level subjects?", "Yes, it is compulsory to take two subjects for A Level. Permission to sit for a third subject is at the discretion of the Principal."],
["Can I register for exams at another school?", "No, students who register at this school are not permitted to register anywhere else for courses or exams of any kind."],
["What documents are required for school admission?", "You need: child's passport with valid visa, birth certificate, vaccination card (for KG and Grade 1), Emirates ID, six passport size photographs, latest report card, reference letter, attested original transfer certificate, bonafide certificate from the previous school (for Grade 1–8), medical record book, and family book (for UAE nationals only)."],
["Do I need to provide a vaccination card for admission?", "Yes, a copy of the child's vaccination card is required for KG and Grade 1 admissions."],
["Do I need a transfer certificate for admission?", "Yes, a duly attested original transfer certificate or school leaving certificate is required from the previous school attended."],
["Is a bonafide certificate needed for admission?", "Yes, for admission to Grade 1–8, a bonafide certificate from the previous school is required."],
["What if I am a UAE national? What extra document do I need?", "UAE nationals must provide a copy of the family book for admission."],
["How much is the tuition fee for KG1 and KG2?", "The tuition fee for KG1 & KG2 is 7,270 AED per year, payable in three installments."],
["How much is the tuition fee for Grade 1 to Grade 3?", "The tuition fee for Grade 1 to Grade 3 is 8,100 AED per year, payable in three installments."],
["How much is the tuition fee for Grade 4 to Grade 6?", "The tuition fee for Grade 4 to Grade 6 is 9,100 AED per year, payable in three installments."],
["How much is the tuition fee for Grade 7 and 8?", "The tuition fee for Grade 7 and 8 is 11,200 AED per year, payable in three installments."],
["How much is the tuition fee for Grade 9 and 10?", "The tuition fee for Grade 9 and 10 is 13,100 AED per year, payable in three installments."],
["How much is the tuition fee for Grade 11, 12, and A Level?", "The tuition fee for Grade 11, 12, and A Level is 15,900 AED per year, payable in three installments."],
["What are the fee payment options?", "Tuition fees are paid in three installments. Please contact the school office for payment options and due dates."],
["Can I pay school fees online?", "Please contact the school office for details about online fee payment options."],
["How do I contact the school for more information?", "Please call the school office or visit our website's contact page for more information."],
["What are the school office timings?", "Please contact the school office or check the website for updated office timings."],
["Where is the school located?", "Please refer to the school website for our full address and location map."],
["What is the school website?", "Please check the school website or search online for the official page."],

]
custom_trainer = ListTrainer(chatbot)
for pair in custom_conversations:
    custom_trainer.train(pair)

# Simple HTML chat interface
HTML_PAGE = """
<!doctype html>
<html>
<head>
    <title>SchoolBot - Your School Chatbot</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f2f4fa; }
        #chatbox { width: 420px; margin: 40px auto; background: #fff; border-radius: 10px; box-shadow: 0 4px 24px #ccc; padding: 20px; }
        #messages { height: 300px; overflow-y: auto; border: 1px solid #eee; padding: 10px; margin-bottom: 15px; background: #fafbff; border-radius: 6px;}
        .msg { margin: 6px 0; }
        .user { color: #0074D9; font-weight: bold; }
        .bot { color: #2ECC40; }
        #inputArea { display: flex; }
        #userInput { flex: 1; padding: 8px; border-radius: 6px; border: 1px solid #ccc; }
        #sendBtn { padding: 8px 18px; margin-left: 8px; border-radius: 6px; border: none; background: #0074D9; color: #fff; font-weight: bold; cursor: pointer;}
        #sendBtn:hover { background: #005fa3; }
    </style>
</head>
<body>
    <div id="chatbox">
        <h2>SchoolBot 🤖</h2>
        <div id="messages"></div>
        <form id="inputArea" onsubmit="sendMessage(); return false;">
            <input type="text" id="userInput" placeholder="Ask me anything about the school..." autocomplete="off" />
            <button id="sendBtn" type="submit">Send</button>
        </form>
    </div>
    <script>
        const messages = document.getElementById("messages");
        function appendMessage(sender, text) {
            let el = document.createElement("div");
            el.className = "msg";
            el.innerHTML = `<span class="${sender}">${sender === 'user' ? 'You' : 'SchoolBot'}:</span> ${text}`;
            messages.appendChild(el);
            messages.scrollTop = messages.scrollHeight;
        }
        function sendMessage() {
            let input = document.getElementById("userInput");
            let msg = input.value.trim();
            if(!msg) return;
            appendMessage("user", msg);
            input.value = "";
            fetch("/chat", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({message: msg})
            })
            .then(resp => resp.json())
            .then(data => {
                appendMessage("bot", data.reply);
            });
        }
        // Send message on Enter key
        document.getElementById("userInput").addEventListener("keyup", function(e) {
            if (e.key === "Enter") sendMessage();
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = chatbot.get_response(user_message)
    # Use confidence fallback
    if hasattr(response, 'confidence') and response.confidence < 0.5:
        bot_response = "I'm sorry, I don't have an answer for that. Please contact the school office for more help."
    else:
        bot_response = str(response)
    return jsonify({'reply': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
