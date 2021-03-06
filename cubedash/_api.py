import logging

from flask import Blueprint, abort

from . import _model
from ._utils import as_geojson

_LOG = logging.getLogger(__name__)
bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/datasets/<product_name>')
@bp.route('/datasets/<product_name>/<int:year>')
@bp.route('/datasets/<product_name>/<int:year>/<int:month>')
@bp.route('/datasets/<product_name>/<int:year>/<int:month>/<int:day>')
def datasets_geojson(
        product_name: str,
        year: int = None,
        month: int = None,
        day: int = None,
):
    return as_geojson(_model.get_datasets_geojson(product_name, year, month, day))


@bp.route('/footprint/<product_name>')
@bp.route('/footprint/<product_name>/<int:year>')
@bp.route('/footprint/<product_name>/<int:year>/<int:month>')
@bp.route('/footprint/<product_name>/<int:year>/<int:month>/<int:day>')
def footprint_geojson(
        product_name: str,
        year: int = None,
        month: int = None,
        day: int = None,
):
    return as_geojson(_model.get_footprint_geojson(product_name, year, month, day))


@bp.route('/regions/<product_name>')
@bp.route('/regions/<product_name>/<int:year>')
@bp.route('/regions/<product_name>/<int:year>/<int:month>')
@bp.route('/regions/<product_name>/<int:year>/<int:month>/<int:day>')
def regions_geojson(
        product_name: str,
        year: int = None,
        month: int = None,
        day: int = None,
):
    regions = _model.get_regions_geojson(product_name, year, month, day)
    if regions is None:
        abort(404, f"{product_name} does not have regions")
    return as_geojson(regions)
