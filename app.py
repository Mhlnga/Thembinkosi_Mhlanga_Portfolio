import streamlit as st
import os
import json

# ==========================================
# PAGE CONFIGURATION & METADATA
# ==========================================
st.set_page_config(
    page_title="T.E Mhlanga | Developer & Engineer Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# MODERN DARK GLASSMORPHISM THEME & STYLES
# ==========================================
st.markdown("""
<style>
    /* Force Deep Dark Background Theme */
    .stApp, [data-testid="stHeader"], [data-testid="stToolbar"] {
        background-color: #090d16 !important;
        color: #f8fafc !important;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }

    /* Hide Sidebar Completely for Top Horizontal Nav Layout */
    [data-testid="stSidebar"], [data-testid="collapsedControl"] {
        display: none !important;
    }

    /* Full Width Container Setup */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 3rem !important;
        max-width: 1350px !important;
    }
    
    /* Top Horizontal Nav Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px !important;
        background-color: rgba(18, 26, 43, 0.85) !important;
        backdrop-filter: blur(16px) !important;
        padding: 8px 12px !important;
        border-radius: 14px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        margin-bottom: 32px !important;
    }

    .stTabs [data-baseweb="tab"] {
        height: 46px !important;
        border-radius: 8px !important;
        color: #94a3b8 !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        border: none !important;
        padding: 0px 20px !important;
        transition: all 0.2s ease !important;
    }

    .stTabs [data-baseweb="tab"]:hover {
        color: #f8fafc !important;
        background-color: rgba(255, 255, 255, 0.05) !important;
    }

    .stTabs [aria-selected="true"] {
        background-color: #6366f1 !important;
        color: #ffffff !important;
        box-shadow: 0 4px 14px rgba(99, 102, 241, 0.4) !important;
    }
    
    /* Headers & Markdown text */
    h1, h2, h3, h4, h5, h6, p, span, label, div {
        color: #f8fafc !important;
    }

    /* Expanders & Forms */
    .stExpander, [data-testid="stForm"], input, textarea, select {
        background-color: #121a2b !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: #f8fafc !important;
        border-radius: 12px !important;
    }
    
    /* Header Gradient Title */
    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        line-height: 1.25;
        color: #f8fafc !important;
        margin-bottom: 12px;
    }
    
    .gradient-text {
        background: linear-gradient(135deg, #6366f1 0%, #06b6d4 50%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(18, 26, 43, 0.85);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.5);
    }
    
    /* Tech Stack Badges */
    .tech-chip {
        display: inline-block;
        background: rgba(99, 102, 241, 0.18);
        border: 1px solid rgba(99, 102, 241, 0.4);
        color: #818cf8 !important;
        padding: 4px 12px;
        border-radius: 6px;
        font-size: 0.825rem;
        font-weight: 600;
        margin-right: 8px;
        margin-bottom: 8px;
    }
    
    /* Stat Metric Cards */
    .stat-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
    }
    .stat-number {
        font-size: 2rem;
        font-weight: 800;
        color: #06b6d4 !important;
    }
    .stat-label {
        font-size: 0.85rem;
        color: #94a3b8 !important;
        font-weight: 500;
    }
    
    /* Contact Provider Cards */
    .contact-card-box {
        background: rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 16px 20px;
        margin-bottom: 12px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# INITIAL DATA DEFINITIONS
# ==========================================
INITIAL_PROJECTS = [
    {
        "id": "proj-attendance",
        "title": "Attendance Management & Sick Note Portal",
        "category": "Video Showcase (NDA)",
        "description": "Digital attendance application featuring role-based authentication (Admin & Student), real-time attendance logging, student sick note upload portal, and admin verification dashboard.",
        "role": "Full-Stack Developer",
        "codeStatus": "5 Video Demos Attached",
        "techStack": ["PHP", "JavaScript", "HTML5/CSS3", "MySQL", "Role-Based Auth", "File Upload API"],
        "videoPlaylist": [
            {"title": "1. Admin Login & Dashboard", "url": "media/attendance/Admin Login - Google Chrome 2024-11-23 23-11-13.mp4"},
            {"title": "2. Student Login & Portal", "url": "media/attendance/Student Login - Google Chrome 2024-11-23 22-56-17.mp4"},
            {"title": "3. Take Attendance Workflow", "url": "media/attendance/Take Attendance - Google Chrome 2024-11-23 23-00-35.mp4"},
            {"title": "4. Upload Sick Note", "url": "media/attendance/Upload Sick Note - Google Chrome 2024-11-23 23-04-05.mp4"},
            {"title": "5. View & Approve Uploads", "url": "media/attendance/View Uploads - Google Chrome 2024-11-23 23-09-56.mp4"}
        ],
        "documents": [],
        "photos": [],
        "problem": "Educational institutions needed to replace paper roll calls and track student medical absence certificates securely.",
        "solution": "Engineered a secure web application supporting multi-role access, instant attendance recording, and document upload verification workflows."
    },
    {
        "id": "proj-advisory-timesheet",
        "title": "Advisory Timesheet & Automated Billing Engine",
        "category": "Enterprise Case Study",
        "description": "Recent enterprise system designed for accurate time capture, manager review/rejection workflows, automated invoice number generation, dynamic reporting, and live executive dashboards.",
        "role": "Lead Systems Architect & Developer",
        "codeStatus": "Recent Project • Spec Document Attached",
        "docUrl": "media/docs/Advisory Timesheet update.docx",
        "techStack": ["VBA", "Apps Script", "Excel DB", "Billing Automation", "Audit Logging", "PDF Export"],
        "videoPlaylist": [],
        "documents": [
            {"name": "Advisory Timesheet System Spec Document (.docx)", "url": "media/docs/Advisory Timesheet update.docx"}
        ],
        "photos": [],
        "modules": [
            {"name": "Timesheet Form", "desc": "Automated Entry ID generation, validation rules against active client/individual/activity drop-down lists."},
            {"name": "Manager Review & Rejection Loop", "desc": "Managers approve or reject with reasons. Rejected records retain original Entry ID for employee resubmission."},
            {"name": "Automated Billing Sheet", "desc": "Approved records auto-route to billing, generate sequential invoice numbers, and prevent duplicate billing."},
            {"name": "Reports & Dashboard Analytics", "desc": "Dynamic filters by client, approval status, week/month with automated visual KPIs and PDF export."},
            {"name": "Master Data & Raw_Data Database", "desc": "Centralized audit trail sheet and active/inactive toggle rules for clients, activities, and employees."}
        ],
        "problem": "Advisory teams required an error-proof time tracking solution to prevent manual database edits, manage rejections transparently, and automate client invoicing.",
        "solution": "Engineered a multi-stage workflow system with strict data validation, Entry ID retention on resubmissions, automated billing generation, and executive reporting."
    }
]

# Initialize Session State
if 'projects' not in st.session_state:
    st.session_state.projects = INITIAL_PROJECTS

# Helper function to render chips
def render_chips(tag_list):
    html = "".join([f'<span class="tech-chip">{t}</span>' for t in tag_list])
    st.markdown(f'<div style="margin-top: 8px; margin-bottom: 16px;">{html}</div>', unsafe_allow_html=True)

# ==========================================
# BRAND HEADER & TOP HORIZONTAL NAVBAR
# ==========================================
col_logo, col_space = st.columns([3, 1])
with col_logo:
    st.markdown("## 💻 T.E Mhlanga-Portfolio.")
    st.caption("Full-Stack Developer & Systems Architect")

# Top Horizontal Navigation Tabs
tab_home, tab_projects, tab_vault, tab_about, tab_contact, tab_add = st.tabs([
    "🏠 Home", 
    "📁 Projects", 
    "🎬 Video Vault", 
    "⚡ About & Process", 
    "📬 Contact", 
    "➕ Add / Edit Project"
])

# ==========================================
# PAGE 1: HOME VIEW
# ==========================================
with tab_home:
    st.markdown('<div class="hero-title">Building Powerful Apps & <br><span class="gradient-text">Showcasing Products That Work</span></div>', unsafe_allow_html=True)
    st.markdown("""
    Welcome! Here you'll find live code repositories, interactive video walkthroughs, and detailed technical case studies of applications I've engineered—including high-impact NDA & client projects.
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="stat-card"><div class="stat-number">12+</div><div class="stat-label">Projects Built</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="stat-card"><div class="stat-number">100%</div><div class="stat-label">Video Walkthroughs</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="stat-card"><div class="stat-number">NDA / Client</div><div class="stat-label">Case Studies Ready</div></div>', unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.info("💡 **Tip:** Click the **📁 Projects** or **🎬 Video Vault** tabs above to watch full video walkthroughs and view attached project files.")

# ==========================================
# PAGE 2: PROJECTS VIEW
# ==========================================
with tab_projects:
    st.header("Featured Projects")
    st.write("Filter by source code availability, video walkthroughs, or client NDA case studies.")
    
    cat_filter = st.selectbox("Category Filter", ["All", "Video Showcase (NDA)", "Enterprise Case Study"])
    
    filtered_list = st.session_state.projects
    if cat_filter != "All":
        filtered_list = [p for p in st.session_state.projects if p.get("category") == cat_filter]
        
    for proj in filtered_list:
        with st.container():
            st.markdown(f"""
            <div class="glass-card">
                <h3>{proj['title']}</h3>
                <p style="color: #06b6d4; font-weight: 600; font-size: 0.9rem;">
                    {proj.get('role', 'Developer')} • {proj.get('codeStatus', 'Active Showcase')}
                </p>
                <p style="color: #94a3b8; font-size: 0.95rem;">{proj['description']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            render_chips(proj.get("techStack", []))
            
            with st.expander("▶️ View Video Demos, Modules & Downloads"):
                # Video Playlist Section
                if proj.get("videoPlaylist"):
                    st.subheader("🎥 Video Feature Clips")
                    titles = [v["title"] for v in proj["videoPlaylist"]]
                    selected_clip_title = st.selectbox("Select Video Clip to Play", titles, key=f"v_sel_{proj['id']}")
                    clip_obj = next(v for v in proj["videoPlaylist"] if v["title"] == selected_clip_title)
                    
                    if os.path.exists(clip_obj["url"]):
                        st.video(clip_obj["url"])
                    else:
                        st.info(f"Video File: {clip_obj['url']}")
                        
                # Single Video
                elif proj.get("videoUrl") and os.path.exists(proj.get("videoUrl")):
                    st.video(proj["videoUrl"])
                    
                # Architecture & System Modules
                if proj.get("modules"):
                    st.subheader("⚙️ System Architecture & Key Modules")
                    for m in proj["modules"]:
                        st.write(f"- **{m['name']}:** {m['desc']}")
                        
                # Downloadable Document Files
                if proj.get("docUrl") and os.path.exists(proj["docUrl"]):
                    st.subheader("📄 Project Document")
                    with open(proj["docUrl"], "rb") as f:
                        st.download_button(
                            label=f"📥 Download {os.path.basename(proj['docUrl'])}",
                            data=f,
                            file_name=os.path.basename(proj["docUrl"]),
                            mime="application/octet-stream"
                        )
                        
                if proj.get("documents"):
                    st.subheader("📁 Attached Files")
                    for doc in proj["documents"]:
                        if os.path.exists(doc.get("url", "")):
                            with open(doc["url"], "rb") as f:
                                st.download_button(
                                    label=f"📥 Download {doc['name']}",
                                    data=f,
                                    file_name=os.path.basename(doc["url"])
                                )

# ==========================================
# PAGE 3: VIDEO VAULT VIEW
# ==========================================
with tab_vault:
    st.header("The Video Showcase Vault")
    st.write("End-to-end screen recordings demonstrating live UI interactions, authentication, and database workflows.")
    
    st.subheader("1. Attendance Management & Sick Note Portal")
    att_proj = next((p for p in st.session_state.projects if p["id"] == "proj-attendance"), None)
    if att_proj and att_proj.get("videoPlaylist"):
        v_title = st.selectbox("Choose Video Clip", [v["title"] for v in att_proj["videoPlaylist"]])
        v_obj = next(v for v in att_proj["videoPlaylist"] if v["title"] == v_title)
        if os.path.exists(v_obj["url"]):
            st.video(v_obj["url"])

# ==========================================
# PAGE 4: ABOUT & PROCESS VIEW
# ==========================================
with tab_about:
    st.header("How I Present Projects Without Source Code")
    st.write("""
    In software engineering, source code is frequently owned by commercial clients or protected under Non-Disclosure Agreements (NDAs). 
    Comprehensive video walkthroughs, system diagrams, and architectural documentation provide 100% empirical evidence of technical delivery.
    """)
    
    st.subheader("Core Technical Skills & Stack")
    skills = ["PHP", "JavaScript / TypeScript", "Python", "VBA / Apps Script", "HTML5 / CSS3", "MySQL / PostgreSQL", "System Architecture", "Automated Billing Engines"]
    render_chips(skills)

# ==========================================
# PAGE 5: CONTACT VIEW
# ==========================================
with tab_contact:
    st.header("Let's Build Something Great Together")
    st.write("Interested in working together or reviewing full video walkthroughs? Contact me directly:")
    
    c_col1, c_col2 = st.columns(2)
    with c_col1:
        st.markdown("""
        <div class="contact-card-box">
            <h4 style="color: #6366f1;">✉️ Primary Email</h4>
            <p><a href="mailto:thembinkosie873@gmail.com" style="color: #f8fafc; font-weight: 600; text-decoration: none;">thembinkosie873@gmail.com</a></p>
        </div>
        <div class="contact-card-box">
            <h4 style="color: #06b6d4;">✉️ Alternative Email</h4>
            <p><a href="mailto:mhlanga03@gmail.com" style="color: #f8fafc; font-weight: 600; text-decoration: none;">mhlanga03@gmail.com</a></p>
        </div>
        """, unsafe_allow_html=True)
        
    with c_col2:
        st.markdown("""
        <div class="contact-card-box">
            <h4 style="color: #10b981;">📞 Contact Number</h4>
            <p><a href="tel:0785681139" style="color: #f8fafc; font-weight: 600; text-decoration: none;">0785681139</a></p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("📬 Send Email via Web Provider (Gmail, Outlook, Yahoo)"):
        st.write("Click your preferred email provider link below to open a pre-filled composer:")
        target_mail = "thembinkosie873@gmail.com"
        subj = "Portfolio Inquiry"
        st.markdown(f"- [🔴 Open Gmail Web](https://mail.google.com/mail/?view=cm&fs=1&to={target_mail}&su={subj})")
        st.markdown(f"- [🔵 Open Outlook / Office365 Web](https://outlook.office.com/mail/deeplink/compose?to={target_mail}&subject={subj})")
        st.markdown(f"- [🟣 Open Yahoo Mail](https://compose.mail.yahoo.com/?to={target_mail}&subject={subj})")

# ==========================================
# PAGE 6: ADD / EDIT PROJECT VIEW
# ==========================================
with tab_add:
    st.header("Project Management Form")
    
    action_mode = st.radio("Form Mode", ["Add New Project", "Edit Existing Project"])
    
    if action_mode == "Add New Project":
        with st.form("add_project_streamlit_form"):
            new_title = st.text_input("Project Title *", placeholder="e.g. Employee Attendance & Leave Portal")
            new_desc = st.text_area("Project Description *", placeholder="Describe core features, user roles, and backend logic...")
            new_tech_str = st.text_input("Languages & Technologies Used *", placeholder="e.g. PHP, JavaScript, Python, C#, HTML/CSS, MySQL, VBA")
            new_role = st.text_input("Your Role (Optional)", placeholder="e.g. Lead Full-Stack Developer")
            
            uploaded_media = st.file_uploader("Upload Media Files (Videos & Photos: .mp4, .mov, .png, .jpg)", accept_multiple_files=True, type=["mp4", "mov", "avi", "png", "jpg", "jpeg"])
            uploaded_docs = st.file_uploader("Upload Project Documents & Files (.pdf, .docx, .xlsx, .accdb, .zip)", accept_multiple_files=True, type=["pdf", "docx", "xlsx", "accdb", "zip"])
            
            submit_btn = st.form_submit_button("Save Project")
            
            if submit_btn and new_title and new_desc:
                tech_list = [t.strip() for t in new_tech_str.split(",") if t.strip()]
                
                v_playlist = []
                docs_list = []
                
                if uploaded_media:
                    for f in uploaded_media:
                        save_path = os.path.join("media", "attendance", f.name)
                        with open(save_path, "wb") as out:
                            out.write(f.getbuffer())
                        v_playlist.append({"title": f.name, "url": save_path})
                        
                if uploaded_docs:
                    for f in uploaded_docs:
                        save_path = os.path.join("media", "docs", f.name)
                        with open(save_path, "wb") as out:
                            out.write(f.getbuffer())
                        docs_list.append({"name": f.name, "url": save_path})
                        
                created_project = {
                    "id": f"proj-{int(os.urandom(4).hex(), 16)}",
                    "title": new_title,
                    "category": "Video Showcase (NDA)",
                    "description": new_desc,
                    "role": new_role or "Full-Stack Developer",
                    "codeStatus": "Custom Added Showcase",
                    "techStack": tech_list if tech_list else ["Full-Stack"],
                    "videoPlaylist": v_playlist,
                    "documents": docs_list,
                    "photos": []
                }
                
                st.session_state.projects.insert(0, created_project)
                st.success(f"Project '{new_title}' successfully saved to your portfolio!")

    elif action_mode == "Edit Existing Project":
        proj_titles = [p["title"] for p in st.session_state.projects]
        selected_edit_title = st.selectbox("Select Project to Edit", proj_titles)
        target_proj = next(p for p in st.session_state.projects if p["title"] == selected_edit_title)
        
        with st.form("edit_project_streamlit_form"):
            edit_title = st.text_input("Project Title", value=target_proj["title"])
            edit_desc = st.text_area("Project Description", value=target_proj["description"])
            edit_tech_str = st.text_input("Languages & Technologies Used", value=", ".join(target_proj.get("techStack", [])))
            edit_role = st.text_input("Your Role", value=target_proj.get("role", "Developer"))
            
            update_btn = st.form_submit_button("Update Project Details")
            
            if update_btn:
                target_proj["title"] = edit_title
                target_proj["description"] = edit_desc
                target_proj["techStack"] = [t.strip() for t in edit_tech_str.split(",") if t.strip()]
                target_proj["role"] = edit_role
                st.success(f"Project '{edit_title}' successfully updated!")
