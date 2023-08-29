from fastapi import FastAPI, Request
from branch import create_branch, update_branch, delete_branch, fetch_branches
import uvicorn

app = FastAPI()


@app.post("/create_branch")
async def create_branch_endpoint(request: Request):
    data = await request.json()
    branch_name = data['name']

    # create_branch(name, location)
    return {"message": "Branch created successfully"}


@app.put("/update_branch/{branch_id}")
async def update_branch_endpoint(branch_id: int, name: str, location: str):
    update_branch(branch_id, name, location)
    return {"message": "Branch updated successfully"}


@app.delete("/delete_branch/{branch_id}")
async def delete_branch_endpoint(branch_id: int):
    delete_branch(branch_id)
    return {"message": "Branch deleted successfully"}


@app.get("/get_branch")
async def get_branches_endpoint():
    return fetch_branches()

if _name_ == "_main_":
    uvicorn.run(app, host="127.0.0.1", port=8000)