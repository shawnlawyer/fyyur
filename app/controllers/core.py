from flask import Blueprint, render_template, request, flash, redirect, url_for

class controller(object):

    @staticmethod
    def index_page():
        """Returns the rendered page for the application portal"""

        return render_template('pages/home.html')

    @staticmethod
    def not_found_error_page(error=None):
        """Returns the rendered page for page not found"""

        return render_template('errors/404.html'), 404

    @staticmethod
    def server_error_page(error=None):
        """Returns the rendered page for a server error"""

        return render_template('errors/500.html'), 500
