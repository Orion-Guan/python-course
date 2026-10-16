"""
一、FastAPI框架
fastapi是为python编程语言提供构建web应用API接口的Web框架，类似于Java中的springmvc框架。

二、使用步骤
1. 安装fastapi
    pip install fastapi

2. 创建第一个fastapi应用
    from fastapi import FastAPI
    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

3. 运行fastapi应用
3.1 代码中运行
    if __name__ == "__main__":
        import uvicorn # uvicorn 是fastapi的默认服务器，用于运行fastapi应用
        uvicorn.run(app, host="0.0.0.0", port=80)

3.2 命令行中运行
    fastapi dev "xxxx.py"
    uvicorn xxxx:app --reload

"""
# 导入FastAPI类
from fastapi import FastAPI

# 创建fastapi应用实例
app = FastAPI()

# 定义访问路径
@app.get("/user")
def getUser():
    return {"username": "Orion.Guan", "password": "123456"}

# 运行fastapi应用
if __name__ == "__main__":
    import uvicorn # uvicorn 是fastapi的默认服务器，用于运行fastapi应用
    uvicorn.run(app, host="0.0.0.0", port=1024)

