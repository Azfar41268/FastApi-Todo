from fastapi import FastAPI
from sqlalchemy import create_engine, text
from sqlalchemy.engine.base import Engine

db_url = "postgresql://azfarsikander33:t2mwbLdBS9RE@ep-withered-bar-a5adq13x.us-east-2.aws.neon.tech/todos?sslmode=require"

engine: Engine = create_engine(db_url)


app: FastAPI = FastAPI()

@app.get("/api/python")
def hello():
    with engine.connect() as conn:
        todo = conn.execute(text("create table if not exists todo (id serial primary key, title varchar(255), completed boolean)"))
        todoInput = conn.execute(text("insert into todo (title, completed) values ('Learn Python', True)"))
        result = conn.execute(text("select * from todo"))
        print(result.all())
        a = result.all()
        print(len(a))
        return {"msg": a}

