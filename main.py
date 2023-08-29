from fastapi import FastAPI, Request
from branch import BranchDatabase
import uvicorn

app = FastAPI()
branch_db = BranchDatabase()


@app.post("/create_branch")
async def create_branch_endpoint(request: Request):
    data = await request.json()
    branch_db.create_branch(branch_name, branch_city, branch_frenchise)
    branch_name = data['name']
    branch_city = data['location']
    branch_frenchise = ['frenchise']

    # create_branch(name, location)
    return {"message": "Branch created successfully"}


@app.post("/update_branch/{branch_id}")
async def update_branch_endpoint(branch_id: int, request: Request):
    data = await request.json()
    branch_db.update_branch(branch_name,branch_city, branch_frenchise)

    branch_name = data['name']
    branch_city = data['location']
    branch_frenchise = ['frenchise']
    return {"message": "Branch updated successfully"}


@app.delete("/delete_branch/{branch_id}")
async def delete_branch_endpoint(branch_id: int, request: Request):
    branch_db.delete_branch(branch_id)
    return {"message": "Branch deleted successfully"}

 
@app.get("/get_branch")
async def get_branches_endpoint():
    branches = branch_db.fetch_branches()
    return branches

if __name__ == "_main_":
    uvicorn.run(app, host="127.0.0.1", port=8000)