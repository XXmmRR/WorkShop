from fastapi import FastAPI
from .api import router
from .database import engine
from sqladmin import Admin
from .admin import UserAdmin

app = FastAPI()
app.include_router(router)


admin = Admin(app, engine)
admin.add_view(UserAdmin)


@app.get('/')
def root():
    return {'message': 'hello'}
