install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
streamlit :
	streamlit run text_to_sql_app.py
