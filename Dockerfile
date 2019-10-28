FROM gyaneshm/selenium-chrome-pip

# Install deps
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Run app
COPY app.py .
CMD python3 app.py

# Disable XvFB
ENV START_XVFB false