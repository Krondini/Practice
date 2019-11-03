from flask import Flask
import time

app = Flask(__name__)


@app.route('/')
def home():
	localtime = time.asctime()	
	return localtime


if __name__ == '__main__':
	app.run()