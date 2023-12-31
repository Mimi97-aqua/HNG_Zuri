import datetime
import json

from flask import Flask, request

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def api():
    get_parameters = {
        'slack_name': request.args.get('slack_name'),
        'track': request.args.get('track')
    }

    current_day = datetime.datetime.utcnow().strftime('%A')
    utc_time = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
    github_file_url = 'https://github.com/Mimi97-aqua/HNG_Zuri/blob/main/stage_one_task/main.py'
    github_repo_url = 'https://github.com/Mimi97-aqua/HNG_Zuri.git'
    status_code = 200

    result = {
        'slack_name': list(get_parameters.values())[0],
        'current_day': current_day,
        'utc_time': utc_time,
        'track': list(get_parameters.values())[1],
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': status_code
    }

    result = json.dumps(result, indent=4)

    return result, 200, {'Content-Type': 'application/json'}


if __name__ == '__main__':
    app.run()

