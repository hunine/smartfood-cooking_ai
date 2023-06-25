from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel
from src.modules.recipes_recommender import RecipeRecommender

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create RecipeRecommender object
recommender = RecipeRecommender()


class RecipeNames(BaseModel):
    user_recipes: Optional[List[str]]


@app.post("/recommend", tags=["recommend"])
async def recommend(requestBody: RecipeNames):
    recipes = requestBody.user_recipes

    data = recommender.get_recommendations(recipes)
    return data


@app.post("/recommend/train", tags=["recommend"])
async def training():
    pass
