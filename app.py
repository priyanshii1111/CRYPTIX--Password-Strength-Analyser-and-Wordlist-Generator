from flask import Flask, render_template, request, send_file, abort
from wordlistgenerator import generate_wordlist
from strengthchecker import check_password_strength
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    choice = None
    result = None

    if request.method == "POST":
        choice = request.form.get("choice")

        # --- wordlist generator ---
        if choice == "wordlist":
            name = request.form.get("name")
            year = request.form.get("year")
            extra = request.form.get("extra")

            if name and year:
                # Ensure reports folder exists
                reports_dir = os.path.join(os.getcwd(), "reports")
                os.makedirs(reports_dir, exist_ok=True)

                # Generate file inside reports/
                filepath = generate_wordlist(name, year, extra)

                # Force-save output to a consistent path
                final_path = os.path.join(reports_dir, "custom_wordlist.txt")
                os.replace(filepath, final_path)

                # Read preview
                with open(final_path, "r") as f:
                    lines = f.read().splitlines()

                preview = "\n".join(lines[:20])
                result = (
                    f"Wordlist generated successfully.\n\n"
                    f"Saved at: reports/custom_wordlist.txt\n\n"
                    f"Preview (first 20 lines):\n{preview}\n\n"
                    f"Download full wordlist from the button below."
                )
            else:
                result = "uh oh! Please enter Name and Year!"

        # --- password strength checker ---
        elif choice == "strength":
            password = request.form.get("password")
            if password:
                result = check_password_strength(password)
            else:
                result = "Please enter a password!"

        # --- exit ---
        elif choice == "exit":
            result = "Cheerio! Thanks for using CRYPTIX. See you again!"
            choice = None

    return render_template("index.html", choice=choice, result=result)


# --- DOWNLOAD WORDLIST ROUTE ---
@app.route("/download-wordlist")
def download_wordlist():
    file_path = os.path.join(os.getcwd(), "reports", "custom_wordlist.txt")

    if not os.path.exists(file_path):
        return abort(404, description="Wordlist not found — generate one first.")

    return send_file(file_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
