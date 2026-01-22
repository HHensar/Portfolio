# This Website – Personal Portfolio
**Source Code** [github.com/HHensar/Portfolio](https://github.com/HHensar/Portfolio)

## Backend
The backend is built with FastAPI and uses Jinja2 templates to render structured data into HTML pages.
FastAPI was selected for its performance, simplicity, and strong integration with Python, enabling a clean and maintainable backend architecture.

## Frontend
The frontend is implemented with HTML and CSS, with content dynamically rendered from JSON and Markdown sources.
AI-assisted design tools were used to accelerate UI iteration, allowing me to focus on layout structure, data flow, and maintainability.

## Content Management
All site content is stored in JSON or Markdown files, making the site easy to update, extend, and scale as new projects are added without modifying backend logic.

## Deployment
The site is deployed on a Linux VPS (Ionos) and served through Cloudflare, providing a straightforward and reliable production setup with DNS management and HTTPS support.

## Example File Structure


    Hensar(dot)com/
    ├── main.py              # FastAPI application
    ├── requirements.txt     # Python dependencies
    ├── data/
    │   └── home.json        # Home page content
    ├── htmls/
    │   ├── home.html        # Home page template
    │   └── project.html     # Project page template
    ├── projects/
    │   └── this_website.md  # Project info file
    └── static/
        └── profile_pic.jpg  # Static assets

