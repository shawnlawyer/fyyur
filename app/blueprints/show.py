from flask import Blueprint, render_template, request, flash

from app.controllers import ShowController

blueprint = Blueprint('show', __name__)
controller = ShowController()

@blueprint.route('/shows')
def list_page():

    return controller.list_page()

@blueprint.route('/shows/create')
def create_form_page():

    return controller.create_form_page()


@blueprint.route('/shows/create', methods=['POST'])
def create_action():

    return controller.create_action()
