import datetime
from server.app import app

@app.route('/ver')
def get_version():
    return {
        'name': 'morpheus',
        'version': '0.0.1',
        'serverTime': datetime.datetime.now().isoformat()
    }