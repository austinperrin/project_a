# Frontend - Project A

This is the React + Vite frontend for Project A.  
It provides the user interface and communicates with the backend API.  
For full project setup, see [Project Root README](../README.md).

---

## Tech Stack
- React
- Vite
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

```env
# ============================================================
# Frontend Configuration
# ============================================================

# Public URL your frontend will call (used by Vite/React)
VITE_API_URL=http://backend:8000
```

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

## Testing (Planned)

Frontend testing will be added using Jest or Vitest in future iterations.