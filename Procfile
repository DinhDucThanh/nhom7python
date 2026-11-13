web: python manage.py migrate && python manage.py seed_data && uvicorn study_planner.asgi:application --host 0.0.0.0 --port $PORT
worker: celery -A study_planner worker -l info --pool=threads
beat: celery -A study_planner beat -l info
