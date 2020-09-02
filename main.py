from fastapi import FastAPI
import uvicorn
app = FastAPI()


@app.get("/")
async def root():
    return {"grade": "good", "url": "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FkIqsC%2FbtqEGT92fDc%2FHdq9Qowhgxvbrn94igvzMK%2Fimg.png"}


@app.get("/1/")
async def good():
    return {"grade": "good", "url": "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fccw0Ec%2FbtqEGT3j7wD%2FRgRM2mESHJ0Jcdij1vQcgK%2Fimg.png"}


@app.get("/2/")
async def moderate():
    return {"grade": "moderate", "url": "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fccw0Ec%2FbtqEGT3j7wD%2FRgRM2mESHJ0Jcdij1vQcgK%2Fimg.png"}


@app.get("/3/")
async def bad():
    return {"grade": "bad", "url": "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FkIqsC%2FbtqEGT92fDc%2FHdq9Qowhgxvbrn94igvzMK%2Fimg.png"}


@app.get("/4/")
async def very_bad():
    return {"grade": "very_bad", "url": "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FkIqsC%2FbtqEGT92fDc%2FHdq9Qowhgxvbrn94igvzMK%2Fimg.png"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
