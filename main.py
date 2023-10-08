from fastapi import FastAPI

import os
import time

app = FastAPI()


@app.get("/")
async def root(request):
    my_var = request.session.get("my_var", None)
    if not my_var:
        request.session["my_var"] = "1234"
    return {"my-node": os.getenv("node_name", "Not Found"), "my_var": str(my_var)}