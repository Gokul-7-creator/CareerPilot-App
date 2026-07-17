from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(
    filename,
    email,
    phone,
    github,
    linkedin,
    ats_score,
    resume_match,
    matched_skills,
    missing_skills,
    recruiter_report,
    interview_questions,
    improvements,
    roadmap,
    cover_letter
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Career Assistant Report</b>", styles["Title"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph(f"<b>Email:</b> {email}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Phone:</b> {phone}", styles["BodyText"]))
    story.append(Paragraph(f"<b>GitHub:</b> {github}", styles["BodyText"]))
    story.append(Paragraph(f"<b>LinkedIn:</b> {linkedin}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph(f"<b>ATS Score:</b> {ats_score}/100", styles["Heading2"]))
    story.append(Paragraph(f"<b>Resume Match:</b> {resume_match:.2f}%", styles["Heading2"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Matching Skills</b>", styles["Heading2"]))

    for skill in matched_skills:
        story.append(Paragraph(f"• {skill}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Missing Skills</b>", styles["Heading2"]))

    for skill in missing_skills:
        story.append(Paragraph(f"• {skill}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Recruiter Report</b>", styles["Heading2"]))
    story.append(Paragraph(recruiter_report.replace("\n", "<br/>"), styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Interview Questions</b>", styles["Heading2"]))
    story.append(Paragraph(interview_questions.replace("\n", "<br/>"), styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Resume Improvements</b>", styles["Heading2"]))
    story.append(Paragraph(improvements.replace("\n", "<br/>"), styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Career Roadmap</b>", styles["Heading2"]))
    story.append(Paragraph(roadmap.replace("\n", "<br/>"), styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Cover Letter</b>", styles["Heading2"]))
    story.append(Paragraph(cover_letter.replace("\n", "<br/>"), styles["BodyText"]))

    doc.build(story)