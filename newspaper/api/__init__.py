from flask import Blueprint
from flask_restful import Api
from reader import ReaderApi
from news_record import NewsRecordApi
from packet_record import RedPacketRecordApi

api_bp = Blueprint('api_bp', __name__, url_prefix='/api')
api = Api(api_bp)

api.add_resource(ReaderApi, '/reader')
api.add_resource(NewsRecordApi, '/news_record')
api.add_resource(RedPacketRecordApi, '/packet_record')