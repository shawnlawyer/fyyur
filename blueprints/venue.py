from flask import Blueprint, render_template, request, flash, redirect, url_for
import datetime

from app import db
from forms import VenueForm
from models import Venue, Show

venue = Blueprint('venue', __name__)

@venue.route('/venues')
def venues():

    areas = Venue.query.distinct(Venue.city, Venue.state).all()

    for area in areas:

        area.venues = [v for v in Venue.query.filter_by(city=area.city, state=area.state).all()]

    return render_template(
        'venue/pages/list.html',
        areas=areas
    )

@venue.route('/venues/search', methods=['POST'])
def search_venues():

    search = request.form.get('search_term', '')

    venues = Venue.query.filter(Venue.name.ilike("%" + search + "%")).all()

    results = {
        "count": len(venues),
        "data": [venue for venue in venues]
    }

    return render_template(
        'venue/pages/search.html',
        results=results,
        search_term=search
    )

@venue.route('/venues/<int:venue_id>')
def show_venue(venue_id):
    venue = Venue.query.filter_by(id=venue_id).first_or_404()
    venue.past_shows = Show.query.filter( Show.start_time < datetime.datetime.now(), Show.venue_id == venue.id).all()
    venue.upcoming_shows = Show.query.filter( Show.start_time > datetime.datetime.now(), Show.venue_id == venue.id ).all()
    venue.past_shows_count = len(venue.past_shows)
    venue.upcoming_shows_count = len(venue.upcoming_shows)
    return render_template(
        'venue/pages/detail.html',
        venue=venue
    )


@venue.route('/venues/create', methods=['GET'])
def create_venue_form():

    form = VenueForm()

    return render_template(
        'venue/forms/new_venue.html',
        form=form
    )

@venue.route('/venues/create', methods=['POST'])
def create_venue_submission():

    form = VenueForm(request.form)

    try:
        kwargs = {
            "name" : form.name.data,
            "city" : form.city.data,
            "state" : form.state.data,
            "address" : form.address.data,
            "phone" : form.phone.data,
            "genres" : form.genres.data,
            "facebook_link" : form.facebook_link.data,
            "image_link" : form.image_link.data,
            "website" : form.website.data,
            "seeking_talent" : form.seeking_talent.data,
            "seeking_description" : form.seeking_description.data
        }

        model = Venue(
            **kwargs
        )

        db.session.add(model)
        db.session.commit()

        flash('Venue ' + form.get('name','') + ' was successfully listed!')

    except ValueError:  # FIXME melhorar essa exception

        flash('Whoops. Venue ' + form.get('name','') + ' could not be listed.')

    finally:

        db.session.close()

    return render_template('venue/pages/list.html')

@venue.route('/venues/<int:venue_id>/delete', methods=['GET', 'POST'])
def delete_venue(venue_id):

    try:

        model = Venue.query.filter_by(id=venue_id).first_or_404()

        db.session.delete(model)
        db.session.commit()

        flash('The venue has been removed together with all of its shows.')

        return render_template('venue/pages/list.html')

    except ValueError:

        flash('Whoops. It\'s not possible to delete this Venue')

    finally:

        db.session.close()

    return None

@venue.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):

    form = VenueForm(request.form)

    venue = Venue.query.filter_by(id=venue_id).first_or_404()

    form.state.process_data(venue.state)
    form.genres.process_data(venue.genres)

    return render_template(
        'venue/forms/edit_venue.html',
        form=form,
        venue=venue
    )

@venue.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):

    form = VenueForm(request.form)

    kwargs = {
            "name" : form.name.data,
            "city" : form.city.data,
            "state" : form.state.data,
            "address" : form.address.data,
            "phone" : form.phone.data,
            "genres" : form.genres.data,
            "facebook_link" : form.facebook_link.data,
            "image_link" : form.image_link.data,
            "website" : form.website.data,
            "seeking_talent" : form.seeking_talent.data,
            "seeking_description" : form.seeking_description.data
        }

    try:

        Venue.query.filter(Venue.id == venue_id).update(kwargs)

        db.session.commit()

        flash('Venue' + form.name.data + ' was successfully updated!')

    except:

        flash('An error occurred. Venue ' + form.name.data + ' could not be updated.')

    finally:

        db.session.close()

    return redirect(url_for('venue.show_venue', venue_id=venue_id))
