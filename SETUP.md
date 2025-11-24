# Finance Tracker - Setup Steps

## Project Initialization (Milestone 0)

### 1. Project Structure Created
**Date:** 24th Nov 2025

**Commands Used:**
```bash
mkdir finance-tracker
cd finance-tracker
git init
```

### 2. Backend Setup
- Created `backend/` folder with modular structure
- Created Python virtual environment: `python -m venv venv`
- Activated venv: `venv\Scripts\activate` (Windows)
- Installed initial packages: `pip install fastapi uvicorn python-dotenv`
- Generated `requirements.txt`: `pip freeze > requirements.txt`

**Backend Structure:**
```
backend/
├── venv/                    # Python virtual environment
├── app/
│   ├── __init__.py
│   ├── main.py             # FastAPI app entry point
│   ├── api/
│   │   └── v1/
│   │       └── endpoints/  # API route handlers
│   ├── core/               # Config, security
│   ├── crud/               # Database operations
│   ├── database/           # DB connection
│   ├── middleware/         # Custom middleware
│   ├── models/             # Database models
│   ├── schemas/            # Pydantic schemas
│   ├── utils/              # Helper functions
│   └── tests/              # Test files
└── requirements.txt
```

### 3. Frontend Setup
- Created React app with Vite: `npm create vite@latest frontend -- --template react`
- Installed dependencies: `npm install`
- Added packages: `npm install axios react-router-dom`
- Created folder structure: components, pages, services, utils, types

**Frontend Structure:**
```
frontend/
├── node_modules/
├── src/
│   ├── components/         # React components
│   ├── pages/              # Page components
│   ├── services/           # API calls
│   ├── utils/              # Helper functions
│   ├── types/              # TypeScript types (future)
│   ├── App.jsx
│   └── main.jsx
├── package.json
└── vite.config.js
```

### 4. Configuration Files Created

**.env.example** - Environment variables template
- Contains: MongoDB URL, JWT secrets, CORS origins
- Actual `.env` file (not committed) will be based on this

**.gitignore** - Files to exclude from Git
- Python: venv/, __pycache__, *.pyc
- Node: node_modules/, dist/
- Secrets: .env files
- IDE: .vscode/, .idea/

**README.md** - Project overview

---

## Important Concepts Learned

### Why `__init__.py` Files?
- Make Python folders into importable packages
- Allow: `from app.core.config import settings`
- Usually empty, but their presence is essential

### Why `api/v1/endpoints/` Structure?
- **api/** - Separates API code from business logic
- **v1/** - API versioning (can add v2 later without breaking v1)
- **endpoints/** - Organize routes by feature (auth.py, transactions.py, etc.)

### Why `.env.example`?
- Template for other developers
- Shows what environment variables are needed
- Real `.env` is in .gitignore (secrets stay secret)

### Virtual Environment (venv)
- Isolated Python dependencies per project
- Prevents package conflicts between projects
- Activate before running: `venv\Scripts\activate`

---

## Next Steps (Milestone 1)
- [ ] Create first FastAPI endpoint
- [ ] Test with Postman
- [ ] Connect frontend to backend
- [ ] See "Hello World" in browser

---

## Git Workflow
**Current branch:** main
**Commits made:** 
1. Initial project structure

**To replicate this project:**
1. Clone repo: `git clone <repo-url>`
2. Backend: `cd backend` → `python -m venv venv` → activate → `pip install -r requirements.txt`
3. Frontend: `cd frontend` → `npm install`
4. Copy `.env.example` to `.env` and fill in values
5. Run backend: `uvicorn app.main:app --reload`
6. Run frontend: `npm run dev`

---

## Milestone 1: Hello FARM Stack ✅ COMPLETED

### What Was Built
- Basic FastAPI backend with 2 endpoints
- React frontend that fetches from backend
- CORS configured for frontend-backend communication
- Tested with browser, Postman, and frontend

### Backend Code (`app/main.py`)
- Created FastAPI app
- Added CORS middleware (allows frontend at localhost:5173)
- Created 2 endpoints:
  - `GET /` - Returns welcome message
  - `GET /api/v1/health` - Health check endpoint

### Frontend Code (`src/App.jsx`)
- Used `useState` and `useEffect` hooks
- Fetched data from both backend endpoints
- Displayed results in browser

### Commands to Run
**Backend:**
```bash
cd backend
venv\Scripts\activate
uvicorn app.main:app --reload
```
Runs at: http://localhost:8000

**Frontend:**
```bash
cd frontend
npm run dev
```
Runs at: http://localhost:5173

### Testing
- ✅ Browser: http://localhost:8000 shows JSON
- ✅ Swagger Docs: http://localhost:8000/docs (interactive API docs)
- ✅ Postman: Successfully tested health endpoint
- ✅ Frontend: Displays backend data

### Key Concepts Learned
- **FastAPI basics**: Routes, decorators (@app.get)
- **CORS**: Cross-Origin Resource Sharing for frontend-backend
- **React hooks**: useState (state), useEffect (side effects)
- **fetch()**: Making HTTP requests from JavaScript
- **Uvicorn**: ASGI server with hot reload (--reload flag)
- **Automatic docs**: FastAPI generates Swagger UI at /docs

---

---

## Milestone 2: MongoDB Connection ✅ COMPLETED

### What Was Built
- Connected FastAPI to MongoDB using Motor (async driver)
- Created database connection utilities
- Added startup/shutdown events for connection lifecycle
- Tested CRUD operations with test endpoints

### Database Configuration
- **Driver:** Motor (async MongoDB driver)
- **Connection:** mongodb://localhost:27017
- **Database Name:** finance_tracker
- **File:** `app/database/mongodb.py`

### Code Changes
**database/mongodb.py:**
- MongoDB class for connection management
- `connect_to_mongo()` - Establishes connection
- `close_mongo_connection()` - Closes connection
- `get_database()` - Returns database instance

**main.py updates:**
- Added startup event to connect on app start
- Added shutdown event to disconnect on app stop
- Updated health check to ping database
- Created test endpoints: POST/GET `/api/v1/test`

### Testing Completed
- ✅ Health endpoint shows database connected
- ✅ POST data to MongoDB successful
- ✅ GET data from MongoDB returns inserted items
- ✅ MongoDB Compass shows data (if GUI installed)

### Key Concepts Learned
- **Motor**: Async MongoDB driver for Python
- **Async/Await**: Asynchronous database operations
- **Startup/Shutdown Events**: FastAPI lifecycle events
- **Collections**: MongoDB's equivalent of SQL tables
- **ObjectId**: MongoDB's unique identifier (_id field)

---

## Current Project Status

### ✅ Completed Milestones
1. Project structure and Git setup
2. Backend (FastAPI) and Frontend (React) created
3. CORS configured for communication
4. MongoDB connected and tested

### 🎯 Ready for Next Session
- Basic infrastructure complete
- Can start building actual features (transactions, auth, etc.)
- All tools installed and working

### Quick Start Commands
```bash
# Terminal 1 - Backend
cd backend
venv\Scripts\activate
uvicorn app.main:app --reload

# Terminal 2 - Frontend
cd frontend
npm run dev

# Terminal 3 - MongoDB (if not running as service)
mongod
```

### URLs
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Frontend: http://localhost:5173
- MongoDB: mongodb://localhost:27017