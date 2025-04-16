import os

import database
import router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from html_router.html_router import html_app
# Initialize the FastAPI app
app = FastAPI(
    title="Welcome to the Multi Model Agentic RAG System API!",
    description="An API for managing Agent, Pinecone and FAISS (VectorDB) integrations, Text and PDF processing, and more.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the database
database.init_db()
if not os.path.exists("media"):
    os.makedirs("media")

app.include_router(html_app, prefix="", tags=["HTML API"])
app.include_router(router.index_router, prefix="/index", tags=["Index API"])
app.include_router(router.agent_router, prefix="/agent", tags=["Agent API"])


# Root endpoint
@app.get("/")
def root():
    """
    Root endpoint providing basic information about the API.
    """
    return {
        "message": "Welcome to the Multi Model Agentic RAG System API!",
        "documentation_url": "/docs",
        "redoc_url": "/redoc",
        "version": "1.0.0",
    }
