from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routes import leads

app = FastAPI(title="BeanSight API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://beansight.co.uk", "http://localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)
app.include_router(leads.router)

@app.get("/")
def root():
    return {"status": "BeanSight API is running"}