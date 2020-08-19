'''
+-------------------------------------------------------+
|                     helix_ops.py                      |
| Mathematical operations to be used by the Helix class |
+-------------------------------------------------------+
'''

from math import cos, sin, pi

def magnitude( v ) :
    '''
    Mangitude of vector v(x,y,z)
    '''
    return ( v[ 0 ]**2 + v[ 1 ]**2 + v[ 2 ]**2 )**0.5

def normalize( v ) :
    '''
    Normalize vector v
    '''
    m = magnitude( v )
    return v[ 0 ] / m, v[ 1 ] / m, v[ 2 ] / m

def rotate( p, u, t ) :
    '''
    Rotate point p(x,y,z) about vector u(x,y,z) by angle t
    '''
    px, py, pz = p
    ux, uy, uz = normalize( u )
    x =   px*( ux**2*( 1 - cos( t ) ) +    cos( t ) ) \
        + py*( ux*uy*( 1 - cos( t ) ) - uz*sin( t ) ) \
        + pz*( ux*uz*( 1 - cos( t ) ) + uy*sin( t ) )
    y =   px*( uy*ux*( 1 - cos( t ) ) + uz*sin( t ) ) \
        + py*( uy**2*( 1 - cos( t ) ) +    cos( t ) ) \
        + pz*( ux*uz*( 1 - cos( t ) ) - ux*sin( t ) )
    z =   px*( uz*ux*( 1 - cos( t ) ) - uy*sin( t ) ) \
        + py*( uz*uy*( 1 - cos( t ) ) + ux*sin( t ) ) \
        + pz*( uz**2*( 1 - cos( t ) ) +    cos( t ) )
    return x, y, z

def circle( r, t ) :
    '''
    The equation of a circle on the x-y plane centered
    at the origin in polar coordinates
    '''
    return r*cos( t ), r*sin( t ), 0

def vector( r, t ) :
    '''
    The helix vector of a helix on the x-y plane
    cetered at the origin
    '''
    return r*cos( t ), r*sin( t ), 0

def helix( r, p, t ) :
    '''
    The equation of a helix on the x-y plane
    centered at the origin
    '''
    return r*cos( t ), r*sin( t ), p*t/(2*pi)

def translate( p, x, y, z ) :
    '''
    Move point p(x',y',z') by x, y and z
    '''
    return p[ 0 ] + x, p[ 1 ] + y, p[ 2 ] + z
