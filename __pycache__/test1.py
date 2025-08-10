
from fastapi import FastAPI

app = FastAPI()

@app.get("/kalyan/xyz")
def mul(a,b):
    return a*b
mul(3,4)
print(mul(3,4))