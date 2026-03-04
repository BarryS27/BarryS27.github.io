import json
import os
from pathlib import Path
from typing import Any

from flask import Flask, render_template

app = Flask(__name__)
DATA_FILE = Path(__file__).resolve().parent / "data.json"


def load_portfolio_data(data_file: Path = DATA_FILE) -> dict[str, Any]:
    """Load portfolio content from JSON so content edits stay code-independent."""
    with data_file.open("r", encoding="utf-8") as file:
        return json.load(file)


PORTFOLIO_DATA: dict[str, Any] = load_portfolio_data()


@app.route("/")
def index() -> str:
    return render_template("index.html", data=PORTFOLIO_DATA)


def is_development_mode() -> bool:
    """Toggle debug mode from FLASK_ENV for local iteration."""
    return os.getenv("FLASK_ENV", "production").lower() == "development"


if __name__ == "__main__":
    app.run(debug=is_development_mode(), port=5000)
