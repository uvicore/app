from acme.appstub.services import bootstrap

# Bootstrap the Uvicore application
app = bootstrap.application(is_console=False)

# Http entrypoint for uvicorn or gunicorn
# uvicorn --port 5000 acme.appstub.http.server:http --reload
# gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b 127.0.0.1:5000 acme.appstub.http.server:http
http = app.http
