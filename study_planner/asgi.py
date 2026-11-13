"""
ASGI config for study_planner project.
Mounts FastAPI directly at /api/v1/ and Django ASGI handler at /
"""

import os
from django.core.asgi import get_asgi_application
from starlette.applications import Starlette
from starlette.routing import Mount

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'study_planner.settings')

# Khởi tạo Django ASGI trước khi nạp FastAPI models
django_application = get_asgi_application()

from planner.api import app as fastapi_application

# Composite ASGI application:
# /api/v1/* -> FastAPI (thuật toán tối ưu, AI suggestions, calendar drag-drop sync)
# /*        -> Django 5.x (Templates + HTMX + Auth + Admin Portal)
application = Starlette(
    routes=[
        Mount("/api/v1", app=fastapi_application),
        Mount("/", app=django_application),
    ]
)
