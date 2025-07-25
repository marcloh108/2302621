from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

# Validation functions
def is_xss(term):
    xss_patterns = [r"<\s*script", r"on\w+\s*=", r"javascript:", r"&#", r"<.*?>"]
    return any(re.search(p, term, re.IGNORECASE) for p in xss_patterns)

def is_sql_injection(term):
    sqli_patterns = [r"(\bor\b|\band\b).*(=|>|<)", r"(--|#)", r"(\bselect\b|\binsert\b|\bdelete\b|\bupdate\b|\bdrop\b)", r"['\"]\s*(or|and)\s*['\"]"]
    return any(re.search(p, term, re.IGNORECASE) for p in sqli_patterns)

# 👇 THIS is the fix
@app.route("/", methods=["GET"])
def index():
    return redirect(url_for("home"))

@app.route("/home", methods=["GET", "POST"])
def home():
    error = ""
    search_term = ""
    if request.method == "POST":
        search_term = request.form.get("search", "")
        if is_xss(search_term):
            error = "Input detected as XSS attack. Please try again."
            search_term = ""
        elif is_sql_injection(search_term):
            error = "Input detected as SQL injection attack. Please try again."
            search_term = ""
        else:
            return redirect(url_for("result", term=search_term))
    return render_template("home.html", error=error, search=search_term)

@app.route("/result")
def result():
    term = request.args.get("term", "")
    print(f"[DEBUG] Search term received in /result: '{term}'") 
    return render_template("result.html", term=term)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
