from food import flask_app

if __name__ == '__main__':
    # Run the app locally for testing
    flask_app.run(host='0.0.0.0', port=5000)

# Use gunicorn as the production WSGI server
else:
    import logging
    import sys
    logging.basicConfig(stream=sys.stderr)
    sys.path.insert(0, '/var/www/gcab_pythonanywhere_com')
    from flask_app import flask_app as application
