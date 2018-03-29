class Bmi(object):
    def __init__(self):
        self.BMI = 'no data'
        self.category = 'no data'

    def get(self, weight, height, sex="male"):
        try:
            # For Python 3.0 and later
            from urllib.request import urlopen
        except ImportError:
            # Fall back to Python 2's urllib2
            from urllib2 import urlopen
        import json

        query =  'weight='+str(weight)
        query += '&height='+str(height)
        query += '&sex='+sex
        response = urlopen('http://127.0.0.1:5000/api?'+query)
        data = response.read()
        data = json.loads(data)
        self.BMI = data["BMI"]
        self.category = data["category"]
