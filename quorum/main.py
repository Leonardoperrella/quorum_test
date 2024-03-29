from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from quorum.services.legislator_result_service import legislator_result_context
from quorum.services.bill_result_service import bill_result_context

app = FastAPI()

app.mount("/static", StaticFiles(directory="quorum/static"), name="static")


templates = Jinja2Templates(directory="quorum/templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    legislator_result = legislator_result_context()
    bill_result = bill_result_context()
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "legislator_result": legislator_result,
            "bill_result": bill_result})
