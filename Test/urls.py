from pydantic import BaseModel
from fastapi import FastAPI
import pymysql

app = FastAPI()


class Item(BaseModel):
    customerNo: str = None
    customerName: str = None
    mobile: str = None
    taxNo: str = None


@app.post('/test')
def calculate(request_data: Item):
    a = request_data.customerNo
    b = request_data.customerName
    c = request_data.mobile
    d = request_data.taxNo
    print(request_data)

    conn = pymysql.connect('47.103.139.191', user="root", passwd="ZX5201314", db="test")

    cur = conn.cursor()#获取游标
    sql = "insert into test (customerNo,customerName,mobile,taxNo) values(%s,%s,%s,%s)"
    insert = cur.execute(sql,(a,b,c,d))

    cur.close()
    conn.commit()
    conn.close()

    print(insert)
    res = {"res": insert}

    return res


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app,
                host="0.0.0.0",
                port=8080,
                workers=1)

