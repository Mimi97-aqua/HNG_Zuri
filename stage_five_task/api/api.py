from flask import Blueprint
from flask_cors import CORS
import time
import pyautogui
import os

api = Blueprint("api", __name__)


@api.route('/record', methods=['POST'])
def record_screen():
