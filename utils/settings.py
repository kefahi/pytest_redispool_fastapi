from pydantic import BaseSettings  # BaseModel,

class Settings(BaseSettings):
    redis_host: str = "127.0.0.1"
    redis_port: int = 6379
    redis_password: str = ""
    redis_pool_max: int = 200

 
settings = Settings()
