from flask import Flask
from flask import render_template, request
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    #orm init
    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    @app.route('/')
    def index():
        return render_template('index.html')

    # 파일 업로드 처리
    # @app.route('/fileUpload', methods=['GET', 'POST'])
    # def upload_file():
    #     if request.method == 'POST':
    #         f = request.files['file']
    #         # 저장할 경로 + 파일명
    #         f.save(secure_filename(f.filename))
    #         return 'uploads 디렉토리 -> 파일 업로드 성공!'

    # data 넣기
    @app.route('/setuser')
    def setuser():
        data = models.car_plate(plate='33누 5948', phone='01054980933')
        db.session.add(data) #위에서 만든 data를 추가해라.
        db.session.commit() #실제 db에다가 commit은 마지막으로 한번만
        return 'ok'

    # data 불러오기
    @app.route('/getuser')
    def getuser():
        data = models.car_plate.query.all() #pk값 1번인거 가져와라.
        return data[0].plate

    return app


# terminal -> set FLASK_APP=패키지 이름 set FLASK_DEBUG=true










