from typing import Annotated

from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from db import dbConn
import pandas as pd

templates = Jinja2Templates(directory="templates")


app = FastAPI()


@app.get("/")
def homepage_get(request: Request):
    donations = getAllDonations()
    return templates.TemplateResponse(
        request=request, name="page.html", context={"donations": donations}
    )


@app.post("/")
def homepage_post(
    name: Annotated[str, Form()],
    amount: Annotated[int, Form()],
    comment: Annotated[str, Form()],
    request: Request,
):
    insertDonation(name, amount, comment)
    donations = getAllDonations()
    return templates.TemplateResponse(
        request=request, name="page.html", context={"donations": donations}
    )


def insertDonation(name, amount, comment):
    cursor = dbConn.cursor()
    cursor.execute(
        "INSERT INTO Donation (name, amount, comment) VALUES (%s, %s, %s)",
        (name, amount, comment),
    )
    dbConn.commit()
    cursor.close()


def getAllDonations():
    cursor = dbConn.cursor()
    cursor.execute("SELECT * FROM Donation")
    results = cursor.fetchall()
    cursor.close()
    df = pd.DataFrame(
        results, columns=["id", "name", "amount", "comment", "createdAt", "updatedAt"]
    )
    df.sort_values(by="createdAt", ascending=False, inplace=True)
    df["createdAt"] = df["createdAt"].dt.strftime("%Y-%m-%d %H:%M:%S")
    df["updatedAt"] = df["updatedAt"].dt.strftime("%Y-%m-%d %H:%M:%S")
    return df.to_dict(orient="records")
