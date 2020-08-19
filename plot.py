import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from colour import Color

class Plot() :
    '''
    Plots to be used by the Helix class
    '''
    def __init__( self ) :
        self.x = 0
        self.y = 0
        self.z = 0
        self.m = 0
        self.n = 0

    def set_aspect_equal_3d( self, ax ) :
        '''
        Set the aspect ratio of a Matplotlib 3D plot to 1
        '''
        xl = ax.get_xlim3d()
        yl = ax.get_ylim3d()
        zl = ax.get_zlim3d()
        xm = sum( xl )/len( xl )
        ym = sum( yl )/len( yl )
        zm = sum( zl )/len( zl )
        r = max(
            abs( n - m )
            for l, m in (
                ( xl, xm ), ( yl, ym ), ( zl, zm )
                )
            for n in l
            )
        ax.set_xlim3d( [ xm - r, xm + r ] )
        ax.set_ylim3d( [ ym - r, ym + r ] )
        ax.set_zlim3d( [ zm - r, zm + r ] )
        
    def surface( self, azimuth = 0, elevate = 0,
                 color1 = 'grey', color2 = 'white' ) :
        '''
        Generates a 3D surface plot of the helix
        '''
        color = list(
            Color( color1 ).range_to(
                Color( color2 ),
                2*self.m*( self.n - 1 ) + 2
                )
            )
        x, y, z = self.x, self.y, self.z
        n = self.m*self.n # total points in helix h
        plt.clf() # clear current figure
        fig = plt.figure( 1 )
        ax = Axes3D( fig )
        for h in range( len( x ) // n ) :
            verts = []
            # bottom cap
            verts.append( list( zip(
                x[ h*n : self.m + h*n ],
                y[ h*n : self.m + h*n ],
                z[ h*n : self.m + h*n ]
                ) ) )
            for j in range( self.n - 1 ) :
                for i in range( self.m ) :
                    #polygons /\/
                    verts.extend( [
                        [ # poygon 1 /\
                            # vertex 1
                            ( x[ i + j*self.m + h*n ],
                              y[ i + j*self.m + h*n ],
                              z[ i + j*self.m + h*n ] ),
                            # vertex 2
                            ( x[ ( i + 1 )%self.m + j*self.m + h*n ],
                              y[ ( i + 1 )%self.m + j*self.m + h*n ],
                              z[ ( i + 1 )%self.m + j*self.m + h*n ] ),
                            # vertex 3
                            ( x[ self.m + ( i + 1 )%self.m + j*self.m + h*n ],
                              y[ self.m + ( i + 1 )%self.m + j*self.m + h*n ],
                              z[ self.m + ( i + 1 )%self.m + j*self.m + h*n ] )
                            ],
                        [ # poygon 2 \/
                            # vertex 1
                            ( x[ self.m + i + j*self.m + h*n ],
                              y[ self.m + i + j*self.m + h*n ],
                              z[ self.m + i + j*self.m + h*n ] ),
                            # vertex 2
                            ( x[ i + j*self.m + h*n ],
                              y[ i + j*self.m + h*n ],
                              z[ i + j*self.m + h*n ] ),
                            # vertex 3
                            ( x[ self.m + ( i + 1 )%self.m + j*self.m + h*n ],
                              y[ self.m + ( i + 1 )%self.m + j*self.m + h*n ],
                              z[ self.m + ( i + 1 )%self.m + j*self.m + h*n ] ) ]
                        ] )
            # top cap
            verts.append(
            list( zip( x[ n - self.m  + h*n : n + h*n ],
                       y[ n - self.m  + h*n : n + h*n ],
                       z[ n - self.m  + h*n : n + h*n ] ) )
            )
            i = 0
            for poly in verts:
                ax.add_collection(
                    Poly3DCollection(
                        [ poly ],
                        facecolor = color[ i ].rgb,
                        edgecolor = 'black',
                        linewidths = 0.5
                        )
                    )
                i += 1
        ax.scatter3D( x, y, z, alpha = 0 )
        ax.axis( 'off' )
        ax.grid( b = None )
        self.set_aspect_equal_3d( ax )
        ax.view_init( elevate, azimuth )
        fig.subplots_adjust(
            top = 1, bottom = 0, left = 0,
            right = 1, wspace = 0
            )
        plt.show()
        plt.close()
