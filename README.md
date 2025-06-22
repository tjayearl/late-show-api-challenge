# Late Show API

This project is a simple backend API built using Flask. It simulates a guest management system for a talk show.

The API allows users to register and log in, then view and manage information about episodes, guests, and appearances on the show.

## How it works

- **Users** can create accounts and log in using a token-based system (JWT).
- **Episodes** and **Guests** are listed using simple GET requests.
- An **Appearance** is when a guest appears in an episode — users can create this record.
- The API uses a SQLite database and provides routes to interact with the data.

The project is designed to help practice backend development with Flask, including routing, models, migrations, and basic authentication.


