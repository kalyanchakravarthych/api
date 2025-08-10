from fastapi import FastAPI

app = FastAPI()

@app.get("/kalyan/xyz")
def add(a,b):
    return a+b
add(3,4)
print(add(3,4))


