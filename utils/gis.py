from django.contrib.gis.geos import GEOSGeometry

def calculate_area(geom_wkt):
    """
    Calculate the area of a geometry given in WKT format.
    Returns area in square meters.
    """
    geom = GEOSGeometry(geom_wkt)
    return geom.area

# Add GIS utility functions here.