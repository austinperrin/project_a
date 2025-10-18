# Project A — Development Roadmap
This roadmap outlines the planned evolution of **Project A** - a real-world, single-tenant SaaS boilerplate built with **Django (DRF)** and **React (Vite)** in a monorepo architecture.

The objective is to **incrementally deliver a scalable, production-ready SaaS starter** equipped with authentication, role-based access control (RBAC), CI/CD, testing, and modern development tooling.
> **Note:** This roadmap is a living document.  
> Milestones and features may be added, removed, or re-prioritized as the project evolves.

---
# Milestone 1: Backend Foundation (Core API + Auth)

**Objective:** Basic backend up and running with user accounts, authentication, permissions.

## Steps
- [ ] Create Django project in backend/
- [ ] Install and configure:
  - django-rest-framework
  - django-cors-headers
  - djangorestframework-simplejwt (or dj-rest-auth/djoser for quick auth)
- [ ] Set up accounts app:
  - Custom User model (extensible)
  - JWT authentication endpoints (/api/token/, /api/token/refresh/)
  - api/users/me/ endpoint to fetch current user
- [ ] Add role & permission support:
  - Either extend User model with a role field
  - Or create a Role model linked to permissions
- [ ] Enable CORS so your frontend (Vite dev server) can access API
- [ ] Add basic profiles app with /api/profiles/<id>/ endpoint

## Deliverables
- [ ] Working /api with authentication
- [ ] JWT-based login & refresh
- [ ] Role/permission model ready
- [ ] Swagger/OpenAPI docs auto-generated (optional)

---
# Milestone 2: Frontend Foundation (Layout + Routing + Auth Context)

**Objective:** Basic frontend structure with login flow and protected routes.

## Steps
- [ ] Create React + Vite app in frontend/
- [ ] Set up:
  - React Router (v6+)
  - Context API or Zustand/Redux for auth state
  - axios or fetch wrapper for API calls
- [ ] Create folder structure:
  - pages/Login.jsx
  - pages/Dashboard.jsx
  - context/AuthContext.jsx
  - services/api.js
- [ ] Implement:
  - Login page (form → /api/token/)
  - Store JWT token (preferably in HttpOnly cookie or memory)
  - Protect routes with PrivateRoute component
  - Navbar, Sidebar, basic layout

## Deliverables
- [ ] Frontend can log in using the real backend API
- [ ] User is redirected to dashboard after login
- [ ] Basic layout scaffold is in place

---
# Milestone 3: Profile & Account Management

**Objective:** Give users the ability to view/edit their profile and account settings.

## Steps
### Backend:
- [ ] Implement /api/account/ (account info)
- [ ] Implement /api/profile/ (profile info CRUD)
### Frontend:
- [ ] Create pages/Account.jsx and pages/Profile.jsx
- [ ] Add forms for editing account/profile
- [ ] Fetch and update data via API
- [ ] Show data based on user role

## Deliverables
- [ ] Users can view/edit their info
- [ ] Permissions start to shape what users can/can’t see

---
# Milestone 4: Role & Permission Based Access

**Objective:** Lock down routes & components based on user roles (e.g., admin vs. normal user).

## Steps
### Backend:
- [ ] Expand role model or Django’s built-in permissions
- [ ] Add a @permission_classes to API views
- [ ] Return user’s role/permissions in /api/users/me/
### Frontend:
- [ ] Create a helper (e.g., canAccess(role, requiredRole))
- [ ] Protect certain routes/pages based on role
- [ ] Hide/show buttons/UI based on permissions

## Deliverables
- [ ] Role-based access control works end-to-end
- [ ] Admin-only routes are protected both in frontend and backend

---
# Milestone 5: Polish & Extras

## Optional Extras
- [ ] Email verification & password reset
- [ ] Audit logging (when users do actions)
- [ ] Tenant config (even single-tenant apps can use this for branding/env vars)
- [ ] Reusable useAuth() hooks
- [ ] Tests: Django pytest + React testing library
- [ ] Dockerize both backend & frontend
- [ ] Add CI/CD + deploy (e.g., Railway, Fly.io, Render, or Docker on VPS)
