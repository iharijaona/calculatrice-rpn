"""The entry point for the App Server."""

import calculatrice_rpn

#: The default app, exported to be used by gunicorn.
app = calculatrice_rpn.create_app()

if __name__ == '__main__':

    app.run("0.0.0.0", calculatrice_rpn.Config.APP_PORT, debug=True)
