
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = "bugtracker-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bugs.db"
db = SQLAlchemy(app)

# ----------------------------
# Database Model
# ----------------------------
class Bug(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    severity = db.Column(db.String(50), default="Low")
    status = db.Column(db.String(50), default="Open")
    reporter = db.Column(db.String(100), default="Anonymous")
    assignee = db.Column(db.String(100), default="None")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# ----------------------------
# Rule-based AI prediction
# ----------------------------
def predict_severity(title, description):
    text = (title + " " + (description or "")).lower()
    if any(word in text for word in ["crash", "error", "fail", "critical"]):
        return "High"
    elif any(word in text for word in ["slow", "minor", "issue", "ui"]):
        return "Medium"
    return "Low"

# ----------------------------
# Routes
# ----------------------------
@app.route("/")
def index():
    bugs = Bug.query.order_by(Bug.created_at.desc()).all()
    return render_template("index.html", bugs=bugs)

@app.route("/report", methods=["GET", "POST"])
def report_bug():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        reporter = request.form["reporter"] or "Anonymous"
        assignee = request.form["assignee"] or "None"

        # AI Prediction
        severity = predict_severity(title, description)
        status = "Open"

        bug = Bug(
            title=title,
            description=description,
            severity=severity,
            status=status,
            reporter=reporter,
            assignee=assignee,
        )
        db.session.add(bug)
        db.session.commit()
        flash("Bug added successfully!", "success")
        return redirect(url_for("index"))
    return render_template("report.html")

@app.route("/bug/<int:id>")
def bug_details(id):
    bug = Bug.query.get_or_404(id)
    return render_template("bug_details.html", bug=bug)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

# ----------------------------
# Run
# ----------------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
