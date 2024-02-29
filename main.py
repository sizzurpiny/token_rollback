from fastapi import FastAPI

app = FastAPI()


@app.get("/auth")
async def credit(credit="None"):
    return {"credit": credit}
