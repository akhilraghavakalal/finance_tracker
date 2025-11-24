from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.mongodb import connect_to_mongo, close_mongo_connection, get_database

app = FastAPI(title="Finance Tracker API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Startup event - connect to database
@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

# Shutdown event - close database connection
@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

@app.get("/")
def read_root():
    return {"message": "Hello from Finance Tracker API!"}

@app.get("/api/v1/health")
async def health_check():
    db = get_database()
    try:
        # Ping database to check connection
        await db.command("ping")
        return {
            "status": "healthy",
            "message": "API is running",
            "database": "connected"
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "message": "API is running",
            "database": "disconnected",
            "error": str(e)
        }

# Test endpoint to write to database
@app.post("/api/v1/test")
async def test_database(data: dict):
    db = get_database()
    result = await db.test_collection.insert_one(data)
    return {
        "message": "Data inserted successfully!",
        "id": str(result.inserted_id)
    }

# Test endpoint to read from database
@app.get("/api/v1/test")
async def get_test_data():
    db = get_database()
    items = await db.test_collection.find().to_list(100)
    # Convert ObjectId to string
    for item in items:
        item["_id"] = str(item["_id"])
    return {"data": items}