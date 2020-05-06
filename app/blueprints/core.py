from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.controllers import CoreController

blueprint = Blueprint('core', __name__)
controller = CoreController()

@blueprint.route('/')
def index_page():

    return controller.index_page()

@blueprint.errorhandler(404)
def not_found_error_page(error=None):

    return controller.not_found_error_page(error)

@blueprint.errorhandler(500)
def server_error_page(error=None):

    return controller.server_error_page(error)
