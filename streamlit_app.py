from pdb import post_mortem
import streamlit as st
import altair as alt
import pandas as pd
from feedback import feedback_form, save_feedback_to_csv
data = pd.DataFrame({
    'Category': ['Core Subjects', 'Coding Practice', 'Project Work', 'Mock Interviews', 'Research Companies', 'Resume Building', 'Soft Skills', 'Interview Practice', 'Stay Updated'],
    'Importance': [8, 9, 7, 7, 6, 6, 5, 9, 8]
})


def home_page():
    
    st.write("Preparing for interviews at service-based and product-based companies requires careful planning and practice. Here's a guide to help you get started:")

    st.subheader("Understand Company Types")
    st.write("Service-Based Companies offer IT services to other businesses, while Product-Based Companies develop and sell their own software products.")

    st.subheader("Build Strong Foundations")
    st.write("Review core subjects like Operating System, DBMS, Computer Networks, Data Structures, and Algorithms. Utilize online platforms for in-depth learning.")

    st.subheader("Coding Practice")
    st.write("Engage in competitive programming and focus on mastering key data structures and algorithms.")

    st.subheader("Project Work")
    st.write(
        "Build real projects that demonstrate your skills and creativity to potential employers.")

    st.subheader("Practice Mock Interviews")
    st.write("Practice mock interviews with peers, platforms like Pramp, and seek mentor guidance. Prepare for behavioral questions as well.")

    st.subheader("Research Companies")
    st.write("Research companies of interest, understand their products, services, culture, and align your skills accordingly.")

    st.subheader("Resume Building")
    st.write("Craft a well-structured resume highlighting key skills, projects, and relevant work experience.")

    st.subheader("Soft Skills")
    st.write("Work on communication, critical thinking, and problem-solving skills to excel in interviews.")

    st.subheader("Interview Practice")
    st.write(
        "Be prepared for common interview topics, solve technical problems under time constraints.")

    st.subheader("Stay Updated")
    st.write("Keep up with industry trends, follow technical blogs, forums, and news sources to stay informed.")

    st.subheader("Visualizing Importance")
    st.write("Visual representation of the importance of each category:")

    chart = alt.Chart(data).mark_bar().encode(
        x='Category',
        y='Importance'
    ).properties(width=600, height=300)

    st.altair_chart(chart)

def about_page():
    st.title("About Us")
    
    st.image("about.png", caption="PinnaclePath Logo", use_column_width=True)

    st.write(
        "Welcome to PinnaclePath, your trusted partner in navigating the path to placement success. "
        "Our mission is to guide and empower students and professionals on their journey toward "
        "achieving their career aspirations."
    )

    st.write(
        "At PinnaclePath, we understand that the journey to placement can be both exciting and "
        "challenging. That's why we provide a comprehensive range of services and resources to "
        "support you every step of the way."
    )

    st.write(
        "Our team consists of industry experts, career coaches, and educators who are passionate "
        "about helping you unlock your potential. From resume building and interview preparation "
        "to networking strategies and skill development, we're here to ensure you're well-equipped "
        "to excel in your placement endeavors."
    )

    st.write(
        "Whether you're a recent graduate entering the job market or a professional looking to "
        "advance your career, PinnaclePath is your compass for navigating the competitive world "
        "of placements. Join us on this exciting journey, and together, let's chart a course "
        "toward your placement success!"
    )

def computer_Science():
    st.title("Computer Science Page")

    st.write("Welcome to the Computer Science page. Explore the exciting and ever-evolving world of Computer Science.")

    st.subheader("Core Concepts")
    st.write("Computer Science is built on foundational concepts that drive technological advancements:")

    st.markdown("- **Algorithms:** Study of efficient problem-solving methods.")
    st.markdown("- **Data Structures:** Organizing and storing data for efficient access and manipulation.")
    st.markdown("- **Programming Languages:** Creating instructions for computers to execute tasks.")
    st.markdown("- **Operating Systems:** Software managing hardware and software interaction.")
    st.markdown("- **Software Engineering:** Development of robust and scalable software applications.")
    st.markdown("- **Computer Architecture:** Designing hardware components of a computer system.")

    st.subheader("Specializations")
    st.write("Computer Science offers a wide range of exciting specializations:")

    st.markdown("- **Artificial Intelligence:** Creating intelligent systems that simulate human intelligence.")
    st.markdown("- **Software Development:** Crafting applications and systems for various purposes.")
    st.markdown("- **Database Management:** Designing and managing data storage solutions.")
    st.markdown("- **Computer Graphics:** Generating visual content using algorithms and techniques.")
    st.markdown("- **Cybersecurity:** Protecting digital assets from cyber threats and attacks.")

    st.subheader("Career Opportunities")
    st.write("Computer Science graduates enjoy diverse and rewarding career paths:")

    st.markdown("- **Software Developer:** Creating software applications and systems.")
    st.markdown("- **Data Scientist:** Extracting insights from large datasets.")
    st.markdown("- **Machine Learning Engineer:** Developing AI models and algorithms.")
    st.markdown("- **Web Developer:** Designing and building interactive websites.")
    st.markdown("- **Computer Scientist:** Conducting research to advance the field.")

    # ... Continue adding more subheaders and content relevant to Computer Science


def Information_Technology():
    st.title("Information Technology Page")

    st.write("Welcome to the Information Technology page. Explore the dynamic and ever-evolving realm of IT.")

    st.subheader("Overview")
    st.write("Information Technology (IT) is a multifaceted field that deals with the management, processing, and distribution of information through technology solutions. It plays a critical role in modern society and businesses.")

    st.subheader("Key Aspects of IT")
    st.write("IT encompasses a wide range of domains and activities, including:")

    st.markdown("- **Network Infrastructure:** Setting up and managing networks to enable seamless communication.")
    st.markdown("- **Cybersecurity:** Protecting digital assets and data from unauthorized access or cyber threats.")
    st.markdown("- **System Administration:** Managing and maintaining hardware, software, and servers.")
    st.markdown("- **Cloud Computing:** Utilizing cloud services to store and process data.")
    st.markdown("- **IT Support:** Providing technical assistance to users and resolving issues.")
    st.markdown("- **Data Management:** Handling, storing, and analyzing large volumes of data.")

    st.subheader("Role in Business")
    st.write("In the business world, IT has become integral for various reasons:")

    st.markdown("- **Efficiency:** IT streamlines operations, automates tasks, and enhances efficiency.")
    st.markdown("- **Innovation:** IT fosters innovation through software development and technological advancements.")
    st.markdown("- **Decision Making:** Data-driven decisions are empowered by IT systems and analytics.")
    st.markdown("- **Global Reach:** IT facilitates global communication and collaboration.")

    # ... Continue adding more subheaders and content specific to Information Technology


def Artificial_Intelligence():
    st.title("Artificial Intelligence Page")

    st.write("Welcome to the Artificial Intelligence page. Embark on a journey to explore the fascinating field of AI.")

    st.subheader("Introduction to AI")
    st.write("Artificial Intelligence (AI) involves creating intelligent agents capable of mimicking human-like cognitive functions. AI aims to enable machines to learn, reason, and make decisions.")

    st.subheader("Applications")
    st.write("AI finds application in various domains, driving innovation and automation:")

    st.markdown("- **Natural Language Processing:** Enabling machines to understand and generate human language.")
    st.markdown("- **Computer Vision:** Empowering computers to interpret visual information from images and videos.")
    st.markdown("- **Machine Learning:** Training algorithms to improve performance over time.")
    st.markdown("- **Autonomous Systems:** Developing self-driving cars and unmanned aerial vehicles.")
    st.markdown("- **Healthcare and Medicine:** Assisting in medical diagnosis and drug discovery.")

    st.subheader("Ethics and Challenges")
    st.write("As AI advances, ethical considerations and challenges come to the forefront:")

    st.markdown("- **Bias and Fairness:** Ensuring AI systems are unbiased and fair across diverse populations.")
    st.markdown("- **Transparency:** Making AI decisions interpretable and transparent to users.")
    st.markdown("- **Job Disruption:** Addressing concerns about AI impacting job markets.")
    st.markdown("- **Data Privacy:** Safeguarding personal information used in AI models.")

    # ... Continue adding more subheaders and content relevant to Artificial Intelligence


def InterNet_of_Things():
    st.title("Internet of Things Page")
    
    st.write("Welcome to the Internet of Things page. Learn about the interconnected world of IoT.")
    
    st.subheader("What is IoT?")
    st.write("Discover the concept of IoT and how everyday objects are connected to the internet.")
    
    st.subheader("Smart Devices")
    st.write("Explore smart devices like smart homes, wearable tech, and industrial IoT applications.")
    
    st.subheader("Challenges and Opportunities")
    st.write("Understand the challenges and opportunities in the IoT landscape.")
    
    # You can add more subheaders and content related to Internet of Things...

def Data_Science():
    st.title("Data Science Page")
    
    st.write("Welcome to the Data Science page. Dive into the world of data analysis and modeling.")
    
    st.subheader("Data Analysis")
    st.write("Learn about techniques for collecting, cleaning, and analyzing data to extract insights.")
    
    st.subheader("Machine Learning")
    st.write("Explore machine learning algorithms and their applications in predictive modeling.")
    
    st.subheader("Big Data")
    st.write("Discover how data science handles large datasets and leverages distributed computing.")
    
   

def Cyber_Security():
    st.title("Cyber Security Page")

    st.write("Welcome to the Cyber Security page. Dive deep into the crucial field of protecting digital assets and information from evolving cyber threats.")

    st.subheader("Understanding Cyber Security")
    st.write("Cyber Security encompasses strategies and practices designed to safeguard digital systems, networks, and data from cyber attacks. It's a multidisciplinary field that plays a pivotal role in maintaining privacy, data integrity, and operational continuity in the digital age.")

    st.subheader("The Significance of Cyber Security")
    st.write("Cyber Security is integral due to the following reasons:")

    st.markdown("- **Data Protection:** Preventing unauthorized access and theft of sensitive information.")
    st.markdown("- **Privacy Preservation:** Safeguarding personal and confidential data from breaches.")
    st.markdown("- **Business Continuity:** Ensuring uninterrupted operations in the face of cyber incidents.")
    st.markdown("- **Trust Building:** Establishing trust with customers, partners, and stakeholders.")
    st.markdown("- **Financial Security:** Mitigating potential financial losses caused by cyber attacks.")

    st.subheader("Diverse Cyber Threat Landscape")
    st.write("Cyber threats come in various forms, each with unique characteristics and risks:")

    st.markdown("- **Malware:** Malicious software including viruses, worms, trojans, and ransomware.")
    st.markdown("- **Phishing:** Deceptive emails, messages, or websites aiming to steal sensitive information.")
    st.markdown("- **Hacking:** Unauthorized intrusion into systems, networks, and databases.")
    st.markdown("- **DDoS Attacks:** Overwhelming networks or websites with excessive traffic, causing downtime.")
    st.markdown("- **Insider Threats:** Malicious actions or negligence by internal personnel.")

    st.subheader("Effective Defensive Measures")
    st.write("Implementing robust Cyber Security measures is essential for mitigating risks:")

    st.markdown("- **Firewalls:** Deploying firewalls to filter and block unauthorized network traffic.")
    st.markdown("- **Encryption:** Protecting data by converting it into an unreadable format that requires a decryption key.")
    st.markdown("- **Multi-Factor Authentication (MFA):** Requiring multiple forms of identification for user verification.")
    st.markdown("- **Regular Updates:** Keeping software and systems up to date to patch vulnerabilities.")
    st.markdown("- **Security Awareness Training:** Educating users about potential threats and best practices.")

    st.subheader("Promising Cyber Security Careers")
    st.write("The field of Cyber Security offers a plethora of career opportunities:")

    st.markdown("- **Ethical Hacker:** Identifying vulnerabilities by simulating cyber attacks to improve security.")
    st.markdown("- **Security Analyst:** Monitoring networks, identifying threats, and responding to incidents.")
    st.markdown("- **Security Engineer:** Designing and implementing security solutions for organizations.")
    st.markdown("- **Incident Responder:** Investigating and mitigating the impact of cyber incidents.")
    st.markdown("- **Chief Information Security Officer (CISO):** Overseeing an organization's security posture and strategy.")

    st.subheader("Ethics and Challenges in Cyber Security")
    st.write("Ethical considerations and challenges are integral to the practice of Cyber Security:")

    st.markdown("- **Ethical Hacking:** Ethical hackers uncover vulnerabilities to strengthen defenses without malicious intent.")
    st.markdown("- **Legal and Regulatory Compliance:** Navigating regulations such as GDPR and HIPAA to protect user data.")
    st.markdown("- **Constant Adaptation:** Staying updated with evolving cyber threats and technologies.")
    st.markdown("- **Balancing Act:** Balancing the need for strong security measures with user convenience.")

    st.subheader("The Future of Cyber Security")
    st.write("The landscape of Cyber Security continues to evolve with technological advancements:")

    st.markdown("- **AI and Machine Learning:** Utilizing AI to detect and respond to threats more efficiently.")
    st.markdown("- **IoT Security:** Addressing the security challenges arising from the proliferation of connected devices.")
    st.markdown("- **Quantum Computing and Cryptography:** Developing new cryptographic methods to secure data in the quantum computing era.")
    st.markdown("- **Remote Work Security:** Adapting security measures to the remote work environment.")
    st.markdown("- **Public-Private Collaboration:** Enhancing collaboration between governments, organizations, and security experts.")

    st.subheader("Conclusion")
    st.write("As technology continues to advance, Cyber Security remains a cornerstone in ensuring the safety of digital systems and data. By implementing effective strategies, staying informed about evolving threats, and upholding ethical standards, we can collectively build a more secure digital future.")

   

def main():
    st.title("Placement Guider 🐱‍👤")
   
    st.sidebar.title("Navigation")
    menu_options = ["Home", "About","computer_Science","Information_Technology"
                    ,"Artificial_Intelligence","InterNet_of_Things","Data_Science",
                    "Cyber_Security","Feedback"]
    selected_option = st.sidebar.selectbox("Select an option:", menu_options)

    if selected_option == "Home":
        home_page()
    if selected_option == "computer_Science":
        computer_Science()
    if selected_option == "Information_Technology":
        Information_Technology()
    if selected_option == "Artificial_Intelligence":
       Artificial_Intelligence()
    if selected_option == "InterNet_of_Things":
        InterNet_of_Things()
    if selected_option == "Data_Science":
       Data_Science()
    if selected_option == "Cyber_Security":
       Cyber_Security()
    elif selected_option == "Feedback":
       feedback_form()
    elif selected_option == "About":
        about_page()


if __name__ == "__main__":
    main()
