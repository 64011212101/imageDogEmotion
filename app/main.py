from fastapi import FastAPI , Request

from getimage import process

app = FastAPI()
    
@app.get("/")
def root():
    return {"message": "This is my api"}

@app.get("/api/getpreimg")
async def read_str(request : Request):
    item = await request.json()
    item_str = item['img']
    img = process(item_str)
    
    return {"img":img.tolist()}