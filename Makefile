install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
streamlit :
	streamlit run chatbot_app.py