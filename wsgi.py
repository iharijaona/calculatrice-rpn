"""The entry point for the App Server."""

import app as app_factory

#: The default app, exported to be used by gunicorn.
app = app_factory.create_app()

if __name__ == '__main__':

    app.run("0.0.0.0", app_factory.Config.APP_PORT, debug=True)
