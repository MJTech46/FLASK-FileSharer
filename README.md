# FLASK-FileSharer

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask Version](https://img.shields.io/badge/flask-2.0%2B-green.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A simple, lightweight, and secure web application built with Flask for fast local file sharing. Upload files through a clean user interface and generate shareable download links instantly.

---

## Key Features

- **Secure File Uploads:** Safely upload files directly through the web UI.
- **Link Sharing:** Instantly generate and share direct download links.
- **Multi-Format Support:** Flexible handling for documents, images, archives, and media files.
- **Clean Interface:** Responsive and straightforward UI for effortless file management.
- **Minimalist Architecture:** Fast, readable Flask backend with zero unnecessary bloat.

---

## Prerequisites

Ensure you have the following installed before setting up the project:

- **Python:** `3.8` or higher
- **pip:** Latest package manager for Python

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/MJTech46/FLASK-FileSharer.git
cd FLASK-FileSharer
```

### 2. Set Up a Virtual Environment (Recommended)

```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

Open your browser and navigate to **`http://127.0.0.1:5000`** to start uploading and sharing files.

---

## Project Structure

```text
FLASK-FileSharer/
├── static/          # Static assets (CSS, JS, media)
├── templates/       # Jinja2 HTML templates
├── app.py           # Core application entry point
├── requirements.txt # Project dependencies
└── README.md        # Project documentation
```

---

## Contributing

Contributions make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. **Fork** the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a **Pull Request**

---

## License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more details.1