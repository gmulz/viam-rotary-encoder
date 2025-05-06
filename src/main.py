import asyncio
from viam.module.module import Module
try:
    from models.ky_040 import Ky040
except ModuleNotFoundError:
    # when running as local module with run.sh
    from .models.ky_040 import Ky040


if __name__ == '__main__':
    asyncio.run(Module.run_from_registry())
