from enum import Enum
from typing import Set, List, Union

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field


class ProgrammLanguage():
    Name: str = ""
    Librarys: Set[str] = []

    def __init__(self, name, librarys):
        self.Name = name
        self.Librarys = librarys


class Profile(str, Enum):
    Name = "admin"
    Password = "admin"
    Languages: Set[str] = Field(examples=["English", "Russian", "German"])
    ProgrammLanguages: Set[ProgrammLanguage] = Field(examples=[ProgrammLanguage("Python", ["fastapi", "tkinter"])])
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "Name": "admin",
                    "Password": "admin",
                    "Languages": ["English", "Russian"],
                    "ProgrammLanguages": [ProgrammLanguage("Python", ["fastapi"])],
                }
            ]
        }
    }

profile = Profile
app = FastAPI()
@app.get("/")
async def get_model(name: str | None = "", password: str | None = ""):
    if name != profile.Name:
        return "Wrong name"
    elif password != profile.Password:
        return "Wrong password"
    else:
        results = {"Name": profile.Name, "Languages": profile.Languages, "ProgrammLanguages": profile.ProgrammLanguages}
        return results