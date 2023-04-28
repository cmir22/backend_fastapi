# INSTALL ON LOCAL

pip install fastapi["all"]
pip install "uvicorn[standard]"

# RUN ON LOCAL

uvicorn main:app --reload

# PIP DEPENDENCIES

pip install --upgrade -r requirements.txt
pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U
pip freeze > requirements.txt

# RUN

pm2 start pm2.config.js
pm2 logs fastapi
