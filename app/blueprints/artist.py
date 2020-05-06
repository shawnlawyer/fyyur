from flask import Blueprint, render_template, request, flash, redirect, url_for

from app.controllers import ArtistController

blueprint = Blueprint('artist', __name__)
controller = ArtistController()

@blueprint.route('/artists/create', methods=['GET'])
def create_form_page():

    return controller.create_form_page()

@blueprint.route('/artists/create', methods=['POST'])
def create_action():

    return controller.create_action()

@blueprint.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_form(artist_id):

    return controller.edit_form_page(artist_id)

@blueprint.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_action(artist_id):

    return controller.edit_action(artist_id)

@blueprint.route('/artists/<int:artist_id>')
def detail_page(artist_id):

    return controller.detail_page(artist_id)

@blueprint.route('/artists')
def list_page():

    return controller.list_page()

@blueprint.route('/artists/search', methods=['POST'])
def search_page():

    return controller.search_page()

@blueprint.route('/xhr/artists/name/autocomplete', methods=['POST'] )
def search_feed():

    return controller.search_feed()
