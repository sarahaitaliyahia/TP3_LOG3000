# Module static

### Purpose
This module contains static resources for the web application, namely
interface CSS styles.

### Main files and responsibilities
- `style.css`: defines calculator formatting in the page.

### Dependencies and assumptions
- Loaded by `templates/index.html` via `url_for('static', filename='style.css')`.
- Assumes an HTML structure containing classes/ids: `calculator`, `buttons`, `btn`, `operator`, `display`.
