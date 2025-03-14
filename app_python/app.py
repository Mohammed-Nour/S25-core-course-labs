"""Module providing a function to display
 the current time in Moscow timezone."""

from datetime import datetime
from flask import Flask, render_template
from pytz import timezone


def create_app():
    """
    Create and configure the Flask app.

    Returns:
        Flask app instance.
    """
    app = Flask(__name__)

    @app.route('/')
    def show_moscow_time():
        """
        Function to display the current time in Moscow timezone.

        Returns:
            Rendered HTML template with the current time in Moscow.
        """
        # Get the current time in the Moscow timezone
        moscow_tz = timezone('Europe/Moscow')
        current_time = datetime.now(moscow_tz).strftime("%H:%M:%S")

        # Render the template with the current time
        return render_template('index.html', current_time=current_time)

    return app


# Run the application only if executed directly
if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run()