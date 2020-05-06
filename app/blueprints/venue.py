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
def search_feed():

    return controller.search_feed()

@blueprint.route('/xhr/venues/hours/autocomplete', methods=['POST'])
def hours_feed():

    import datetime
    from flask import jsonify
    times = []
    time = datetime.datetime.strptime("1970-01-01 00:00", "%Y-%m-%d %H:%M")
    end = datetime.datetime.strptime("1970-01-02 00:00", "%Y-%m-%d %H:%M")
    while time < end:
        time_string = str(time.strftime("%-I:%M %p"))
        if time_string.startswith(request.form.get('term', '')):
            times.append(str(time.strftime("%-I:%M %p")))
        time += datetime.timedelta(minutes=30)

    return jsonify(times)
