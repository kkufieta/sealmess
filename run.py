from backend.src.views import views

APP = views.app

# Default port:
if __name__ == '__main__':
    APP.run(debug=True)