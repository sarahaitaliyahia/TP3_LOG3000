# Module templates

## Purpose
This module contains HTML templates rendered by Flask. It defines the
structure of the web interface seen by the user.

## Main files and responsibilities
- `index.html`: single calculator page, displays the result returned by
  Flask and contains the minimal JavaScript functions to populate the display
  and clear the input.

## Dependencies and assumptions
- Depends on Flask to render variables/template tags `{{ url_for(...) }}` and `{{ result }}`.
- Depends on `static/style.css` for visual appearance.
- The form sends the `display` value via `POST` to route `/`.
- The user wants to solve expressions with one operator and 2 operands.
