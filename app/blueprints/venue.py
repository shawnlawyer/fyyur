from flask import Blueprint, render_template, request, flash, redirect, url_for

from app.controllers import VenueController

blueprint = Blueprint('venue', __name__)
controller = VenueController()

@blueprint.route('/venues/create', methods=['GET'])
def create_form_page():

    return controller.create_form_page()

@blueprint.route('/venues/create', methods=['POST'])
def create_action():

    return controller.create_action()

@blueprint.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_form_page(venue_id):

    return controller.edit_form_page(venue_id)

@blueprint.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_action(venue_id):

    return controller.edit_action(venue_id)

@blueprint.route('/venues/<int:venue_id>/delete', methods=['GET', 'POST'])
def delete_action(venue_id):

    return controller.delete_action(venue_id)

@blueprint.route('/venues/<int:venue_id>')
def detail_page(venue_id):

    return controller.detail_page(venue_id)

@blueprint.route('/venues')
def list_page():

    return controller.list_page()

@blueprint.route('/venues/search', methods=['POST'])
def search_page():

    return controller.search_page()

@blueprint.route('/xhr/venues/name/autocomplete', methods=['POST'])
def autocomplete_name_json():

    return controller.autocomplete_name_json()

@blueprint.route('/xhr/venues/hours/autocomplete', methods=['POST'])
def autocomplete_hours_json():

    return controller.autocomplete_hours_json()
