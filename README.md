# Playlistify

The next level playlist experience

## How to run the app

### Server

Create DB

`docker run -d --name postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -p "5432:5432" postgres`

Create PGAdmin4

`docker run -d --name pgadmin4 -e PGADMIN_DEFAULT_EMAIL=pgadmin4 -e PGADMIN_DEFAULT_PASSWORD=pgadmin4 -p "8880:80" dpage/pgadmin4`

Start server
`npm run start:server`

### UI

Install dependencies:
`npm install`

Build UI:
`npm run build:ui`

Start dev server:
`npm run start:ui`

### Tests
Install Python v3.7.*

Install dependencies:
`pip install -r requirements.txt`

Run Server and WebUI as described above

Run tests from `tests\` directory:  
`pytest` for running all tests  
`pytest <tests_filename>.py` for running specific tests.

