import helix_ops as ops
from plot import Plot
from numpy import arctan, linspace, pi

class Helix( Plot ) :
    '''
    Plot a Helix, Cylindrical Helix or Nested Cylindrical Helix
    +-----------+------------------------------+--------------+
    | Parameter |          Definition          |    Values    |
    +-----------+------------------------------+--------------+
    |    rh1    | outer helical radius         | (-inf, inf)  |
    +-----------+------------------------------+--------------+
    |    rh2    | inner helical radius         | (-inf, inf)  |
    +-----------+------------------------------+--------------+
    |    rc     | cylindrical radius           | (-inf, inf)  |
    +-----------+------------------------------+--------------+
    |     p     | pitch (height after 1 turn)  | (-inf, inf)  |
    +-----------+------------------------------+--------------+
    |    d1     | outer direction of rotation  |   -1 or +1   |
    +-----------+------------------------------+--------------+
    |    d2     | inner direction of rotation  |   -1 or +1   |
    +-----------+------------------------------+--------------+
    |    dc     | rotation of circle           | (-inf, inf)  |
    +-----------+------------------------------+--------------+
    |    t1     | numb. of outer helical turns |  ( 0, inf )  |
    +-----------+------------------------------+--------------+
    |    t2     | numb. of inner helical turns |  ( 0, inf )  |
    +-----------+------------------------------+--------------+
    |     m     | number of points per circle  | Integers > 0 |
    +-----------+------------------------------+--------------+
    |     n     | number of circles in helix   | Integers > 0 |
    +-----------+------------------------------+--------------+
    '''
    def cylindrical( self, rh1, rc, dc, p, t1, m, n ) :
        self.m, self.n = m, n
        self.x, self.y, self.z = zip(
            *[ ops.translate(
                ops.rotate(
                    ops.circle( rc, tc ),
                    ops.vector( rh1, th ),
                    -dc*pi/2 + arctan( p/(2*pi*rh1) )*rh1/abs( rh1 )
                    ),
                *ops.helix( rh1, th )
                )
               for th in linspace( 0, 2*pi*t1, n )
               for tc in linspace( 0, 2*pi*( 1 - 1/m ), m ) ]
            )
        return self.x, self.y, self.z

    def cylindrical_double( self, rh1, rc, p, dca, dcb, t1, m, n ) :
        x1, y1, z1 = self.cylindrical(  rh1, rc, dca, p, t1, m, n )
        x2, y2, z2 = self.cylindrical( -rh1, rc, dcb, p, t1, m, n )
        self.x, self.y, self.z = x1 + x2, y1 + y2, z1 + z2
        return self.x, self.y, self.z

    def cylindrical_nested( self, rh1, rh2, rc, dc, p,
                              d1,  d2,  t1, t2,  m, n ) :
        self.m, self.n = m, n
        # nested helix pitch
        p2 = t1*( p**2 + (2*pi*rh1)**2 )**0.5/t2
        self.x, self.y, self.z = zip(
            *[ ops.translate(
                ops.rotate(
                    ops.translate(
                        ops.rotate(
                            ops.circle( rc, tc ),
                            ops.vector( d2*rh2, th ),
                            d2*( dc*pi/2 - arctan( p2/(2*pi*abs( rh2 )) ) )
                            ),
                        *ops.vector( d2*rh2, th )
                        ),
                    ops.vector( d2*rh1, th*t1/t2  ),
                    d1*( pi/2 + arctan(  d2*p/(2*pi*abs( rh1 )) ) )
                    ),
                *ops.helix( d1*rh1, p, th*t1/t2 )
                )
               for th in linspace( 0, 2*pi*t2, n )
               for tc in linspace( 0, 2*pi*( 1 - 1/m ), m ) ]
            )
        return self.x, self.y, self.z

    def double_cylindrical_nested( self,
                                    rh1, rh2, rc,  p, dca, dcb,
                                     d1,  d2, t1, t2,   m,   n ) :
        x1, y1, z1 = self.cylindrical_nested(
            rh1, -rh2, rc, dca, p, d1, d2, t1, t2, m, n
            )
        x2, y2, z2 = self.cylindrical_nested(
            rh1,  rh2, rc, dcb, p, d1, d2, t1, t2, m, n
            )
        self.x, self.y, self.z = x1 + x2, y1 + y2, z1 + z2
        return self.x, self.y, self.z

    def cylindrical_sextuple( self,
                              rh1a, rh1b, rh2a, rh2b,
                                rc,    p, dc1a, dc1b,
                              dc2a, dc2b,  d1a,  d1b,
                               d2a,  d2b,  t1a,  t1b,
                               t2a,  t2b,    m,    n ) :
        x1, y1, z1 = self.double_cylindrical_nested(
            -rh1a, rh2a, rc, p, dc1a, dc2a, d1a, d2a, t1a, t2a, m, n
            )
        x2, y2, z2 = self.double_cylindrical_nested(
             rh1b, rh2b, rc, p, dc1b, dc2b, d1b, d2b, t1b, t2b, m, n
            )
        self.x, self.y, self.z = x1 + x2, y1 + y2, z1 + z2
        return self.x, self.y, self.z
