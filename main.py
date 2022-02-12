from bottle import run, template, get, request
import os
import joblib

MLModel = joblib.load('MLModel-regressor.sav')


@get('/api')
def hello():
    try:
        param = list(map(float, request.query['param'].split(',')))
        pred = list(MLModel.predict([param]))
        return {'ok': True, 'risk': min(100.0, pred[0])}
    except Exception as e:
        return {'ok': False, 'error': str(e)}


if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)


