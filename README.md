# Hensar.com - Personal Portfolio

My personal portfolio website showcasing my software engineering projects and skills.

**Live Site:** [hensar.com](https://hensar.com)

## About

A FastAPI-based portfolio application featuring dynamic content rendering from JSON and Markdown files, with a modern dark-themed interface.

## Tech Stack

- **Backend:** FastAPI, Jinja2 Templates
- **Frontend:** HTML, CSS
- **Content:** JSON, Markdown
- **Deployment:** Linux VPS with Cloudflare

## Project Structure

```
Hensar(dot)com/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── data/
│   ├── home.json        # Home page content
│   └── projects.json    # Projects list
├── htmls/
│   ├── home.html        # Home page template
│   ├── project.html     # Project page template
│   ├── projects.html    # Projects list template
│   └── 404.html         # Error page
├── projects/
│   └── *.md             # Project markdown files
└── static/
    └── favicon.ico      # Static assets
```
