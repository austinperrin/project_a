# Frontend - Project A

This is the React + Vite frontend for Project A.  
It provides the user interface and communicates with the backend API.  
For full project setup, see [Project Root README](../README.md).

---

## Tech Stack
- React
- Vite
- ESLint (code linting)
- Docker (multi-container networking)

---

## Project Structure

```
frontend/
├── public/
│   └── vite.svg
├── src/
│   ├── assets/
│   ├── App.css
│   ├── App.jsx
│   ├── index.css
│   └── main.jsx
├── .dockerignore
├── Dockerfile
├── eslint.config.js
├── index.html
├── package.json
├── package-lock.json
├── README.md
└── vite.config.js
```

- `src/` contains application source files.
- `public/` contains static assets.
- Configuration is handled via Vite.
- The frontend is fully containerized using Docker.

---

## Environment Variables

These are the backend-specific environment variables.  
See the root README for the full `.env` configuration.

```bash
# React
VITE_API_URL=http://backend:8000
```

Production example:

```bash
# React
VITE_API_URL=https://yourdomain.com/api
```

`VITE_API_URL` should point to the backend API.

---

## Running the Frontend

Run frontend only:

```bash
docker compose -f ../docker-compose.dev.yml up frontend
```

Run full stack (frontend + backend + db):

```bash
docker compose -f ../docker-compose.dev.yml up --build
```

- Frontend → http://localhost:5173  
- Backend → http://localhost:8000

---

## Production Build (for reference)

The production build stage in `frontend/Dockerfile` runs:

```bash
npm install
npm run build
```

and outputs files to `/app/dist`, which are then served by Nginx.

---

## Troubleshooting

| Issue                          | Cause                                  | Fix                                                        |
|----------------------------------|-----------------------------------------|------------------------------------------------------------|
| API requests not working        | Wrong `VITE_API_URL` in `.env`         | Check and correct the API URL                               |
| Port already in use             | Existing service running               | Stop other process or change port in Vite config            |

---

## Testing (Planned)

Frontend testing will be added using Jest or Vitest in future iterations.