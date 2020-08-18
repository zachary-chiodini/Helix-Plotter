# Cylindrical Nested Helices
Generating 3D plots of cylindrical nested helices using Python and Matplotlib

<!DOCTYPE html>
<html>
  <title>Nested Helical Geometry in Matplotlib</title>
  <body style="background-color:#002240; color:white; padding:30px">
    <h1 style="color:#02FF02">Nested Helical Geometry in Matplotlib</h1>
    <p>
      This page presents some examples of cool 3D surfaces one can plot using Python's inbuilt library Matplotlib. 
      There are many examples of Matplotlib on the web, but none quite like what is shown here.
      The complex geometry of nested cylindrical helices are created purely as structural art pieces 
      that demonstrate the beauty, versatility and creative freedom that exists in the software.
      The points generated to create these structures can be converted to STL files and 3D printed, but that is not shown here.
      The code used to produce the 3D surface plots is shared, but not for the video and animations.
    </p>
    <h1 style="color:#02FF02">Ops Class</h1>
    <p>
      To begin, some simple mathematical operations must be defined in order to create the geometric structures.
      All that is needed is a circle, a helix, the generalized rotation matrix and a translation function.
    </p>
    <table align="center">
      <tr><td>
        <div style="height:300px; width:750px; overflow:auto; font-family:courier">
<table class="table"><tr><td><div class="linenodiv" style="background-color: #454545; padding-right: 10px"><pre style="line-height: 125%"> 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62</pre></div></td><td class="code"><div style="background: #002240"><pre style="line-height: 125%"><span></span><span style="color: #FF8000">from</span> <span style="color: #FFFFFF">math</span> <span style="color: #FF8000">import</span> <span style="color: #FFFFFF">cos</span>, <span style="color: #FFFFFF">sin</span>, <span style="color: #FFFFFF">pi</span>

<span style="color: #FF8000">class</span> <span style="color: #5E5EFF">Ops</span> :
    <span style="color: #02FF02">&#39;&#39;&#39;</span>
<span style="color: #02FF02">    Mathematical operations to be used by the Helix class</span>
<span style="color: #02FF02">    &#39;&#39;&#39;</span> 
    <span style="color: #FF8000">def</span> <span style="color: #5E5EFF">magnitude</span>( <span style="color: #FF69B4">self</span>, <span style="color: #FFFFFF">v</span> ) :
        <span style="color: #02FF02">&#39;&#39;&#39;</span>
<span style="color: #02FF02">        Mangitude of vector v(x,y,z)</span>
<span style="color: #02FF02">        &#39;&#39;&#39;</span>
        <span style="color: #FF8000">return</span> ( <span style="color: #FFFFFF">v</span>[ <span style="color: #FF00FF">0</span> ]<span style="color: #FF8000">**</span><span style="color: #FF00FF">2</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">v</span>[ <span style="color: #FF00FF">1</span> ]<span style="color: #FF8000">**</span><span style="color: #FF00FF">2</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">v</span>[ <span style="color: #FF00FF">2</span> ]<span style="color: #FF8000">**</span><span style="color: #FF00FF">2</span> )<span style="color: #FF8000">**</span><span style="color: #FF00FF">0.5</span>

    <span style="color: #FF8000">def</span> <span style="color: #5E5EFF">normalize</span>( <span style="color: #FF69B4">self</span>, <span style="color: #FFFFFF">v</span> ) :
        <span style="color: #02FF02">&#39;&#39;&#39;</span>
<span style="color: #02FF02">        Normalize vector v</span>
<span style="color: #02FF02">        &#39;&#39;&#39;</span>
        <span style="color: #FFFFFF">m</span> <span style="color: #FF8000">=</span> <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">magnitude</span>( <span style="color: #FFFFFF">v</span> )
        <span style="color: #FF8000">return</span> <span style="color: #FFFFFF">v</span>[ <span style="color: #FF00FF">0</span> ] <span style="color: #FF8000">/</span> <span style="color: #FFFFFF">m</span>, <span style="color: #FFFFFF">v</span>[ <span style="color: #FF00FF">1</span> ] <span style="color: #FF8000">/</span> <span style="color: #FFFFFF">m</span>, <span style="color: #FFFFFF">v</span>[ <span style="color: #FF00FF">2</span> ] <span style="color: #FF8000">/</span> <span style="color: #FFFFFF">m</span>
    
    <span style="color: #FF8000">def</span> <span style="color: #5E5EFF">rotate</span>( <span style="color: #FF69B4">self</span>, <span style="color: #FFFFFF">p</span>, <span style="color: #FFFFFF">u</span>, <span style="color: #FFFFFF">t</span> ) :
        <span style="color: #02FF02">&#39;&#39;&#39;</span>
<span style="color: #02FF02">        Rotate point p(x,y,z) about vector u(x,y,z) by angle t</span>
<span style="color: #02FF02">        &#39;&#39;&#39;</span>
        <span style="color: #FFFFFF">px</span>, <span style="color: #FFFFFF">py</span>, <span style="color: #FFFFFF">pz</span> <span style="color: #FF8000">=</span> <span style="color: #FFFFFF">p</span>
        <span style="color: #FFFFFF">ux</span>, <span style="color: #FFFFFF">uy</span>, <span style="color: #FFFFFF">uz</span> <span style="color: #FF8000">=</span> <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">normalize</span>( <span style="color: #FFFFFF">u</span> )
        <span style="color: #FFFFFF">x</span> <span style="color: #FF8000">=</span>   <span style="color: #FFFFFF">px</span><span style="color: #FF8000">*</span>( <span style="color: #FFFFFF">ux</span><span style="color: #FF8000">**</span><span style="color: #FF00FF">2</span><span style="color: #FF8000">*</span>( <span style="color: #FF00FF">1</span> <span style="color: #FF8000">-</span> <span style="color: #FFFFFF">cos</span>( <span style="color: #FFFFFF">t</span> ) ) <span style="color: #FF8000">+</span>    <span style="color: #FFFFFF">cos</span>( <span style="color: #FFFFFF">t</span> ) ) \
            <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">py</span><span style="color: #FF8000">*</span>( <span style="color: #FFFFFF">ux</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">uy</span><span style="color: #FF8000">*</span>( <span style="color: #FF00FF">1</span> <span style="color: #FF8000">-</span> <span style="color: #FFFFFF">cos</span>( <span style="color: #FFFFFF">t</span> ) ) <span style="color: #FF8000">-</span> <span style="color: #FFFFFF">uz</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">sin</span>( <span style="color: #FFFFFF">t</span> ) ) \
            <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">pz</span><span style="color: #FF8000">*</span>( <span style="color: #FFFFFF">ux</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">uz</span><span style="color: #FF8000">*</span>( <span style="color: #FF00FF">1</span> <span style="color: #FF8000">-</span> <span style="color: #FFFFFF">cos</span>( <span style="color: #FFFFFF">t</span> ) ) <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">uy</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">sin</span>( <span style="color: #FFFFFF">t</span> ) )
        <span style="color: #FFFFFF">y</span> <span style="color: #FF8000">=</span>   <span style="color: #FFFFFF">px</span><span style="color: #FF8000">*</span>( <span style="color: #FFFFFF">uy</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">ux</span><span style="color: #FF8000">*</span>( <span style="color: #FF00FF">1</span> <span style="color: #FF8000">-</span> <span style="color: #FFFFFF">cos</span>( <span style="color: #FFFFFF">t</span> ) ) <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">uz</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">sin</span>( <span style="color: #FFFFFF">t</span> ) ) \
            <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">py</span><span style="color: #FF8000">*</span>( <span style="color: #FFFFFF">uy</span><span style="color: #FF8000">**</span><span style="color: #FF00FF">2</span><span style="color: #FF8000">*</span>( <span style="color: #FF00FF">1</span> <span style="color: #FF8000">-</span> <span style="color: #FFFFFF">cos</span>( <span style="color: #FFFFFF">t</span> ) ) <span style="color: #FF8000">+</span>    <span style="color: #FFFFFF">cos</span>( <span style="color: #FFFFFF">t</span> ) ) \
            <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">pz</span><span style="color: #FF8000">*</span>( <span style="color: #FFFFFF">ux</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">uz</span><span style="color: #FF8000">*</span>( <span style="color: #FF00FF">1</span> <span style="color: #FF8000">-</span> <span style="color: #FFFFFF">cos</span>( <span style="color: #FFFFFF">t</span> ) ) <span style="color: #FF8000">-</span> <span style="color: #FFFFFF">ux</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">sin</span>( <span style="color: #FFFFFF">t</span> ) )
        <span style="color: #FFFFFF">z</span> <span style="color: #FF8000">=</span>   <span style="color: #FFFFFF">px</span><span style="color: #FF8000">*</span>( <span style="color: #FFFFFF">uz</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">ux</span><span style="color: #FF8000">*</span>( <span style="color: #FF00FF">1</span> <span style="color: #FF8000">-</span> <span style="color: #FFFFFF">cos</span>( <span style="color: #FFFFFF">t</span> ) ) <span style="color: #FF8000">-</span> <span style="color: #FFFFFF">uy</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">sin</span>( <span style="color: #FFFFFF">t</span> ) ) \
            <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">py</span><span style="color: #FF8000">*</span>( <span style="color: #FFFFFF">uz</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">uy</span><span style="color: #FF8000">*</span>( <span style="color: #FF00FF">1</span> <span style="color: #FF8000">-</span> <span style="color: #FFFFFF">cos</span>( <span style="color: #FFFFFF">t</span> ) ) <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">ux</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">sin</span>( <span style="color: #FFFFFF">t</span> ) ) \
            <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">pz</span><span style="color: #FF8000">*</span>( <span style="color: #FFFFFF">uz</span><span style="color: #FF8000">**</span><span style="color: #FF00FF">2</span><span style="color: #FF8000">*</span>( <span style="color: #FF00FF">1</span> <span style="color: #FF8000">-</span> <span style="color: #FFFFFF">cos</span>( <span style="color: #FFFFFF">t</span> ) ) <span style="color: #FF8000">+</span>    <span style="color: #FFFFFF">cos</span>( <span style="color: #FFFFFF">t</span> ) )
        <span style="color: #FF8000">return</span> <span style="color: #FFFFFF">x</span>, <span style="color: #FFFFFF">y</span>, <span style="color: #FFFFFF">z</span>

    <span style="color: #FF8000">def</span> <span style="color: #5E5EFF">circle</span>( <span style="color: #FF69B4">self</span>, <span style="color: #FFFFFF">r</span>, <span style="color: #FFFFFF">t</span> ) :
        <span style="color: #02FF02">&#39;&#39;&#39;</span>
<span style="color: #02FF02">        The equation of a circle on the x-y plane centered</span>
<span style="color: #02FF02">        at the origin in polar coordinates</span>
<span style="color: #02FF02">        &#39;&#39;&#39;</span>
        <span style="color: #FF8000">return</span> <span style="color: #FFFFFF">r</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">cos</span>( <span style="color: #FFFFFF">t</span> ), <span style="color: #FFFFFF">r</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">sin</span>( <span style="color: #FFFFFF">t</span> ), <span style="color: #FF00FF">0</span>

    <span style="color: #FF8000">def</span> <span style="color: #5E5EFF">vector</span>( <span style="color: #FF69B4">self</span>, <span style="color: #FFFFFF">r</span>, <span style="color: #FFFFFF">t</span> ) :
        <span style="color: #02FF02">&#39;&#39;&#39;</span>
<span style="color: #02FF02">        The helix vector of a helix on the x-y plane</span>
<span style="color: #02FF02">        cetered at the origin</span>
<span style="color: #02FF02">        &#39;&#39;&#39;</span>
        <span style="color: #FF8000">return</span> <span style="color: #FFFFFF">r</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">cos</span>( <span style="color: #FFFFFF">t</span> ), <span style="color: #FFFFFF">r</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">sin</span>( <span style="color: #FFFFFF">t</span> ), <span style="color: #FF00FF">0</span>

    <span style="color: #FF8000">def</span> <span style="color: #5E5EFF">helix</span>( <span style="color: #FF69B4">self</span>, <span style="color: #FFFFFF">r</span>, <span style="color: #FFFFFF">p</span>, <span style="color: #FFFFFF">t</span> ) :
        <span style="color: #02FF02">&#39;&#39;&#39;</span>
<span style="color: #02FF02">        The equation of a helix on the x-y plane</span>
<span style="color: #02FF02">        centered at the origin</span>
<span style="color: #02FF02">        &#39;&#39;&#39;</span>
        <span style="color: #FF8000">return</span> <span style="color: #FFFFFF">r</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">cos</span>( <span style="color: #FFFFFF">t</span> ), <span style="color: #FFFFFF">r</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">sin</span>( <span style="color: #FFFFFF">t</span> ), <span style="color: #FFFFFF">p</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">t</span><span style="color: #FF8000">/</span>(<span style="color: #FF00FF">2</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">pi</span>)
    
    <span style="color: #FF8000">def</span> <span style="color: #5E5EFF">translate</span>( <span style="color: #FF69B4">self</span>, <span style="color: #FFFFFF">p</span>, <span style="color: #FFFFFF">x</span>, <span style="color: #FFFFFF">y</span>, <span style="color: #FFFFFF">z</span> ) :
        <span style="color: #02FF02">&#39;&#39;&#39;</span>
<span style="color: #02FF02">        Move point p(x&#39;,y&#39;,z&#39;) by x, y and z</span>
<span style="color: #02FF02">        &#39;&#39;&#39;</span>
        <span style="color: #FF8000">return</span> <span style="color: #FFFFFF">p</span>[ <span style="color: #FF00FF">0</span> ] <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">x</span>, <span style="color: #FFFFFF">p</span>[ <span style="color: #FF00FF">1</span> ] <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">y</span>, <span style="color: #FFFFFF">p</span>[ <span style="color: #FF00FF">2</span> ] <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">z</span>
</pre></div>
</td></tr></table>
        </div>
        </td></tr>
    </table>
    <h1 style="color:#02FF02">Plot Class</h1>
    <p>
      Of course, we need to plot the structures. This class uses a list of x, y and z coordinates, the number of
      circles used to construct the cylindrical surface of each helix and the number of points used to construct each circle 
      to find all adjacent polygons. Matplotlib.pyplot is used to generate the plot,
      Axes3D is used for the 3D projection of the plot, 
      Poly3DCollection is used to define the polygons and a library called colour is used to generate a custom colormap.
      I am only interested in the shape of the geometry, so gridlines and axis values are removed.
    </p>
    <table align="center">
      <tr><td>
        <div style="height:300px; width:750px; overflow:auto; font-family:courier">
<table class="table"><tr><td><div class="linenodiv" style="background-color: #454545; padding-right: 10px"><pre style="line-height: 125%">  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
 11
 12
 13
 14
 15
 16
 17
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
 43
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121</pre></div></td><td class="code"><div style="background: #002240"><pre style="line-height: 125%"><span></span><span style="color: #FF8000">import</span> <span style="color: #FFFFFF">matplotlib.pyplot</span> <span style="color: #FF8000">as</span> <span style="color: #FFFFFF">plt</span>
<span style="color: #FF8000">from</span> <span style="color: #FFFFFF">mpl_toolkits.mplot3d</span> <span style="color: #FF8000">import</span> <span style="color: #FFFFFF">Axes3D</span>
<span style="color: #FF8000">from</span> <span style="color: #FFFFFF">mpl_toolkits.mplot3d.art3d</span> <span style="color: #FF8000">import</span> <span style="color: #FFFFFF">Poly3DCollection</span>
<span style="color: #FF8000">from</span> <span style="color: #FFFFFF">colour</span> <span style="color: #FF8000">import</span> <span style="color: #FFFFFF">Color</span>

<span style="color: #FF8000">class</span> <span style="color: #5E5EFF">Plot</span>() :
    <span style="color: #02FF02">&#39;&#39;&#39;</span>
<span style="color: #02FF02">    Plots to be used by the Helix class</span>
<span style="color: #02FF02">    &#39;&#39;&#39;</span>
    <span style="color: #FF8000">def</span> <span style="color: #5E5EFF">__init__</span>( <span style="color: #FF69B4">self</span> ) :
        <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">x</span> <span style="color: #FF8000">=</span> <span style="color: #FF00FF">0</span>
        <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">y</span> <span style="color: #FF8000">=</span> <span style="color: #FF00FF">0</span>
        <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">z</span> <span style="color: #FF8000">=</span> <span style="color: #FF00FF">0</span>
        <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">=</span> <span style="color: #FF00FF">0</span>
        <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">n</span> <span style="color: #FF8000">=</span> <span style="color: #FF00FF">0</span>

    <span style="color: #FF8000">def</span> <span style="color: #5E5EFF">set_aspect_equal_3d</span>( <span style="color: #FF69B4">self</span>, <span style="color: #FFFFFF">ax</span> ) :
        <span style="color: #02FF02">&#39;&#39;&#39;</span>
<span style="color: #02FF02">        Set the aspect ratio of a Matplotlib 3D plot to 1</span>
<span style="color: #02FF02">        &#39;&#39;&#39;</span>
        <span style="color: #FFFFFF">xl</span> <span style="color: #FF8000">=</span> <span style="color: #FFFFFF">ax</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">get_xlim3d</span>()
        <span style="color: #FFFFFF">yl</span> <span style="color: #FF8000">=</span> <span style="color: #FFFFFF">ax</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">get_ylim3d</span>()
        <span style="color: #FFFFFF">zl</span> <span style="color: #FF8000">=</span> <span style="color: #FFFFFF">ax</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">get_zlim3d</span>()
        <span style="color: #FFFFFF">xm</span> <span style="color: #FF8000">=</span> <span style="color: #FF69B4">sum</span>( <span style="color: #FFFFFF">xl</span> )<span style="color: #FF8000">/</span><span style="color: #FF69B4">len</span>( <span style="color: #FFFFFF">xl</span> )
        <span style="color: #FFFFFF">ym</span> <span style="color: #FF8000">=</span> <span style="color: #FF69B4">sum</span>( <span style="color: #FFFFFF">yl</span> )<span style="color: #FF8000">/</span><span style="color: #FF69B4">len</span>( <span style="color: #FFFFFF">yl</span> )
        <span style="color: #FFFFFF">zm</span> <span style="color: #FF8000">=</span> <span style="color: #FF69B4">sum</span>( <span style="color: #FFFFFF">zl</span> )<span style="color: #FF8000">/</span><span style="color: #FF69B4">len</span>( <span style="color: #FFFFFF">zl</span> )
        <span style="color: #FFFFFF">r</span> <span style="color: #FF8000">=</span> <span style="color: #FF69B4">max</span>(
            <span style="color: #FF69B4">abs</span>( <span style="color: #FFFFFF">n</span> <span style="color: #FF8000">-</span> <span style="color: #FFFFFF">m</span> )
            <span style="color: #FF8000">for</span> <span style="color: #FFFFFF">l</span>, <span style="color: #FFFFFF">m</span> <span style="color: #FF8000">in</span> (
                ( <span style="color: #FFFFFF">xl</span>, <span style="color: #FFFFFF">xm</span> ), ( <span style="color: #FFFFFF">yl</span>, <span style="color: #FFFFFF">ym</span> ), ( <span style="color: #FFFFFF">zl</span>, <span style="color: #FFFFFF">zm</span> )
                )
            <span style="color: #FF8000">for</span> <span style="color: #FFFFFF">n</span> <span style="color: #FF8000">in</span> <span style="color: #FFFFFF">l</span>
            )
        <span style="color: #FFFFFF">ax</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">set_xlim3d</span>( [ <span style="color: #FFFFFF">xm</span> <span style="color: #FF8000">-</span> <span style="color: #FFFFFF">r</span>, <span style="color: #FFFFFF">xm</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">r</span> ] )
        <span style="color: #FFFFFF">ax</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">set_ylim3d</span>( [ <span style="color: #FFFFFF">ym</span> <span style="color: #FF8000">-</span> <span style="color: #FFFFFF">r</span>, <span style="color: #FFFFFF">ym</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">r</span> ] )
        <span style="color: #FFFFFF">ax</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">set_zlim3d</span>( [ <span style="color: #FFFFFF">zm</span> <span style="color: #FF8000">-</span> <span style="color: #FFFFFF">r</span>, <span style="color: #FFFFFF">zm</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">r</span> ] )
        
    <span style="color: #FF8000">def</span> <span style="color: #5E5EFF">surface</span>( <span style="color: #FF69B4">self</span>, <span style="color: #FFFFFF">azimuth</span> <span style="color: #FF8000">=</span> <span style="color: #FF00FF">0</span>, <span style="color: #FFFFFF">elevate</span> <span style="color: #FF8000">=</span> <span style="color: #FF00FF">0</span>,
                 <span style="color: #FFFFFF">color1</span> <span style="color: #FF8000">=</span> <span style="color: #02FF02">&#39;purple&#39;</span>, <span style="color: #FFFFFF">color2</span> <span style="color: #FF8000">=</span> <span style="color: #02FF02">&#39;red&#39;</span> ) :
        <span style="color: #02FF02">&#39;&#39;&#39;</span>
<span style="color: #02FF02">        Generates a 3D surface plot of the helix</span>
<span style="color: #02FF02">        &#39;&#39;&#39;</span>
        <span style="color: #FFFFFF">color</span> <span style="color: #FF8000">=</span> <span style="color: #FF69B4">list</span>(
            <span style="color: #FFFFFF">Color</span>( <span style="color: #FFFFFF">color1</span> )<span style="color: #FF8000">.</span><span style="color: #FFFFFF">range_to</span>(
                <span style="color: #FFFFFF">Color</span>( <span style="color: #FFFFFF">color2</span> ),
                <span style="color: #FF00FF">2</span><span style="color: #FF8000">*</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span><span style="color: #FF8000">*</span>( <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">n</span> <span style="color: #FF8000">-</span> <span style="color: #FF00FF">1</span> ) <span style="color: #FF8000">+</span> <span style="color: #FF00FF">2</span>
                )
            )
        <span style="color: #FFFFFF">x</span>, <span style="color: #FFFFFF">y</span>, <span style="color: #FFFFFF">z</span> <span style="color: #FF8000">=</span> <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">x</span>, <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">y</span>, <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">z</span>
        <span style="color: #FFFFFF">n</span> <span style="color: #FF8000">=</span> <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span><span style="color: #FF8000">*</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">n</span> <span style="color: #DD0000"># total points in helix h</span>
        <span style="color: #FFFFFF">plt</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">clf</span>() <span style="color: #DD0000"># clear current figure</span>
        <span style="color: #FFFFFF">fig</span> <span style="color: #FF8000">=</span> <span style="color: #FFFFFF">plt</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">figure</span>( <span style="color: #FF00FF">1</span> )
        <span style="color: #FFFFFF">ax</span> <span style="color: #FF8000">=</span> <span style="color: #FFFFFF">Axes3D</span>( <span style="color: #FFFFFF">fig</span> )
        <span style="color: #FF8000">for</span> <span style="color: #FFFFFF">h</span> <span style="color: #FF8000">in</span> <span style="color: #FF69B4">range</span>( <span style="color: #FF69B4">len</span>( <span style="color: #FFFFFF">x</span> ) <span style="color: #FF8000">//</span> <span style="color: #FFFFFF">n</span> ) :
            <span style="color: #FFFFFF">verts</span> <span style="color: #FF8000">=</span> []
            <span style="color: #DD0000"># bottom cap</span>
            <span style="color: #FFFFFF">verts</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">append</span>( <span style="color: #FF69B4">list</span>( <span style="color: #FF69B4">zip</span>(
                <span style="color: #FFFFFF">x</span>[ <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> : <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> ],
                <span style="color: #FFFFFF">y</span>[ <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> : <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> ],
                <span style="color: #FFFFFF">z</span>[ <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> : <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> ]
                ) ) )
            <span style="color: #FF8000">for</span> <span style="color: #FFFFFF">j</span> <span style="color: #FF8000">in</span> <span style="color: #FF69B4">range</span>( <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">n</span> <span style="color: #FF8000">-</span> <span style="color: #FF00FF">1</span> ) :
                <span style="color: #FF8000">for</span> <span style="color: #FFFFFF">i</span> <span style="color: #FF8000">in</span> <span style="color: #FF69B4">range</span>( <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> ) :
                    <span style="color: #DD0000">#polygons /\/</span>
                    <span style="color: #FFFFFF">verts</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">extend</span>( [
                        [ <span style="color: #DD0000"># poygon 1 /\</span>
                            <span style="color: #DD0000"># vertex 1</span>
                            ( <span style="color: #FFFFFF">x</span>[ <span style="color: #FFFFFF">i</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">j</span><span style="color: #FF8000">*</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> ],
                              <span style="color: #FFFFFF">y</span>[ <span style="color: #FFFFFF">i</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">j</span><span style="color: #FF8000">*</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> ],
                              <span style="color: #FFFFFF">z</span>[ <span style="color: #FFFFFF">i</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">j</span><span style="color: #FF8000">*</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> ] ),
                            <span style="color: #DD0000"># vertex 2</span>
                            ( <span style="color: #FFFFFF">x</span>[ ( <span style="color: #FFFFFF">i</span> <span style="color: #FF8000">+</span> <span style="color: #FF00FF">1</span> )<span style="color: #FF8000">%</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">j</span><span style="color: #FF8000">*</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> ],
                              <span style="color: #FFFFFF">y</span>[ ( <span style="color: #FFFFFF">i</span> <span style="color: #FF8000">+</span> <span style="color: #FF00FF">1</span> )<span style="color: #FF8000">%</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">j</span><span style="color: #FF8000">*</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> ],
                              <span style="color: #FFFFFF">z</span>[ ( <span style="color: #FFFFFF">i</span> <span style="color: #FF8000">+</span> <span style="color: #FF00FF">1</span> )<span style="color: #FF8000">%</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">j</span><span style="color: #FF8000">*</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> ] ),
                            <span style="color: #DD0000"># vertex 3</span>
                            ( <span style="color: #FFFFFF">x</span>[ <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> ( <span style="color: #FFFFFF">i</span> <span style="color: #FF8000">+</span> <span style="color: #FF00FF">1</span> )<span style="color: #FF8000">%</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">j</span><span style="color: #FF8000">*</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> ],
                              <span style="color: #FFFFFF">y</span>[ <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> ( <span style="color: #FFFFFF">i</span> <span style="color: #FF8000">+</span> <span style="color: #FF00FF">1</span> )<span style="color: #FF8000">%</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">j</span><span style="color: #FF8000">*</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> ],
                              <span style="color: #FFFFFF">z</span>[ <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> ( <span style="color: #FFFFFF">i</span> <span style="color: #FF8000">+</span> <span style="color: #FF00FF">1</span> )<span style="color: #FF8000">%</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">j</span><span style="color: #FF8000">*</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> ] )
                            ],
                        [ <span style="color: #DD0000"># poygon 2 \/</span>
                            <span style="color: #DD0000"># vertex 1</span>
                            ( <span style="color: #FFFFFF">x</span>[ <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">i</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">j</span><span style="color: #FF8000">*</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> ],
                              <span style="color: #FFFFFF">y</span>[ <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">i</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">j</span><span style="color: #FF8000">*</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> ],
                              <span style="color: #FFFFFF">z</span>[ <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">i</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">j</span><span style="color: #FF8000">*</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> ] ),
                            <span style="color: #DD0000"># vertex 2</span>
                            ( <span style="color: #FFFFFF">x</span>[ <span style="color: #FFFFFF">i</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">j</span><span style="color: #FF8000">*</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> ],
                              <span style="color: #FFFFFF">y</span>[ <span style="color: #FFFFFF">i</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">j</span><span style="color: #FF8000">*</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> ],
                              <span style="color: #FFFFFF">z</span>[ <span style="color: #FFFFFF">i</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">j</span><span style="color: #FF8000">*</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> ] ),
                            <span style="color: #DD0000"># vertex 3</span>
                            ( <span style="color: #FFFFFF">x</span>[ <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> ( <span style="color: #FFFFFF">i</span> <span style="color: #FF8000">+</span> <span style="color: #FF00FF">1</span> )<span style="color: #FF8000">%</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">j</span><span style="color: #FF8000">*</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> ],
                              <span style="color: #FFFFFF">y</span>[ <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> ( <span style="color: #FFFFFF">i</span> <span style="color: #FF8000">+</span> <span style="color: #FF00FF">1</span> )<span style="color: #FF8000">%</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">j</span><span style="color: #FF8000">*</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> ],
                              <span style="color: #FFFFFF">z</span>[ <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> ( <span style="color: #FFFFFF">i</span> <span style="color: #FF8000">+</span> <span style="color: #FF00FF">1</span> )<span style="color: #FF8000">%</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">j</span><span style="color: #FF8000">*</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> ] ) ]
                        ] )
            <span style="color: #DD0000"># top cap</span>
            <span style="color: #FFFFFF">verts</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">append</span>(
            <span style="color: #FF69B4">list</span>( <span style="color: #FF69B4">zip</span>( <span style="color: #FFFFFF">x</span>[ <span style="color: #FFFFFF">n</span> <span style="color: #FF8000">-</span> <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span>  <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> : <span style="color: #FFFFFF">n</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> ],
                       <span style="color: #FFFFFF">y</span>[ <span style="color: #FFFFFF">n</span> <span style="color: #FF8000">-</span> <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span>  <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> : <span style="color: #FFFFFF">n</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> ],
                       <span style="color: #FFFFFF">z</span>[ <span style="color: #FFFFFF">n</span> <span style="color: #FF8000">-</span> <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span>  <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> : <span style="color: #FFFFFF">n</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">h</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">n</span> ] ) )
            )
            <span style="color: #FFFFFF">i</span> <span style="color: #FF8000">=</span> <span style="color: #FF00FF">0</span>
            <span style="color: #FF8000">for</span> <span style="color: #FFFFFF">poly</span> <span style="color: #FF8000">in</span> <span style="color: #FFFFFF">verts</span>:
                <span style="color: #FFFFFF">ax</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">add_collection</span>(
                    <span style="color: #FFFFFF">Poly3DCollection</span>(
                        [ <span style="color: #FFFFFF">poly</span> ],
                        <span style="color: #FFFFFF">facecolor</span> <span style="color: #FF8000">=</span> <span style="color: #FFFFFF">color</span>[ <span style="color: #FFFFFF">i</span> ]<span style="color: #FF8000">.</span><span style="color: #FFFFFF">rgb</span>,
                        <span style="color: #FFFFFF">edgecolor</span> <span style="color: #FF8000">=</span> <span style="color: #02FF02">&#39;black&#39;</span>,
                        <span style="color: #FFFFFF">linewidths</span> <span style="color: #FF8000">=</span> <span style="color: #FF00FF">0.5</span>
                        )
                    )
                <span style="color: #FFFFFF">i</span> <span style="color: #FF8000">+=</span> <span style="color: #FF00FF">1</span>
        <span style="color: #FFFFFF">ax</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">scatter3D</span>( <span style="color: #FFFFFF">x</span>, <span style="color: #FFFFFF">y</span>, <span style="color: #FFFFFF">z</span>, <span style="color: #FFFFFF">alpha</span> <span style="color: #FF8000">=</span> <span style="color: #FF00FF">0</span> )
        <span style="color: #FFFFFF">ax</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">axis</span>( <span style="color: #02FF02">&#39;off&#39;</span> )
        <span style="color: #FFFFFF">ax</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">grid</span>( <span style="color: #FFFFFF">b</span> <span style="color: #FF8000">=</span> <span style="color: #FF69B4">None</span> )
        <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">set_aspect_equal_3d</span>( <span style="color: #FFFFFF">ax</span> )
        <span style="color: #FFFFFF">ax</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">view_init</span>( <span style="color: #FFFFFF">elevate</span>, <span style="color: #FFFFFF">azimuth</span> )
        <span style="color: #FFFFFF">fig</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">subplots_adjust</span>(
            <span style="color: #FFFFFF">top</span> <span style="color: #FF8000">=</span> <span style="color: #FF00FF">1</span>, <span style="color: #FFFFFF">bottom</span> <span style="color: #FF8000">=</span> <span style="color: #FF00FF">0</span>, <span style="color: #FFFFFF">left</span> <span style="color: #FF8000">=</span> <span style="color: #FF00FF">0</span>,
            <span style="color: #FFFFFF">right</span> <span style="color: #FF8000">=</span> <span style="color: #FF00FF">1</span>, <span style="color: #FFFFFF">wspace</span> <span style="color: #FF8000">=</span> <span style="color: #FF00FF">0</span>
            )
        <span style="color: #FFFFFF">plt</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">show</span>()
        <span style="color: #FFFFFF">plt</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">close</span>()
</pre></div>
</td></tr></table>
        </div>
        </td></tr>
    </table>
    <h1 style="color:#02FF02">Algorithm</h1>
    <p>
      The mathematical formula for a nested helix defines a curve.
      It does not define a cylindrical surface or the orientation of polygons used to construct such a surface.
      Therefore, a simple mathematical formula was not used. Instead, the helices are contructed algorithmically.
      This algoirthm is explained below in excruciating detail. 
      After each iteration of the nested helix angle, 
      the set of points represented by a cursive "L" is added to a total, 
      which defines the entire surface of a cylindrical nested helix.
      If the mathematics are overwhelming, skip to the video and simply observe how it works.
    </p>
    <p>
      These 5 steps can be summarized as (1) Plotting a Circle, (2) Rotating the Circle, (3) Translating the Circle, 
      (4) Rotating the Circle, again, and (5) Translating the Circle, again.
    </p>
    <p align="center"><img style="width:75%; height:75%" src="helix_algorithm.png" /></p>
    <h1 style="color:#02FF02">Video</h1>
    <p>
      Due to the intensity of the details in the algorithm, the process is animated in a video below to aid in understanding.
      If your browser does not support mp4 files, please switch to one that does.
    </p>
    <p align="center">
      <video style="width:55%; height:55%" controls>
        <source src="helix_algorithm.mp4" type="video/mp4">
      </video>
    </p>
    <h1 style="color:#02FF02">Helix Class</h1>
    <p>
      The Helix class is a subclass of the Ops and Plot class.
      This class can create regular cylindrical helices, double cylindrical helices, 
      cylindrical nested helices, double cylindrical nested helices and 
      the cylindrical sextuple helix (double double cylindrical nested helix) 
      using the aforementioned algorithm.
      Additional parameters have been added to provide more control over the shape of the structure.
      The functions can be edited for further control over the structures.
      For example, minute details like the individual height or radius of each cylinder could be controlled by
      editing the cylindrical_double function to call two distinct nested functions,
      rather than two identical ones, and their respective parameters could be edited therein.
      A few functions are imported from numpy to make calculations easier.
    </p>
    <table align="center">
      <tr><td>
        <div style="height:300px; width:750px; overflow:auto; font-family:courier">
<table class="table"><tr><td><div class="linenodiv" style="background-color: #454545; padding-right: 10px"><pre style="line-height: 125%">  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
 11
 12
 13
 14
 15
 16
 17
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
 43
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105</pre></div></td><td class="code"><div style="background: #002240"><pre style="line-height: 125%"><span></span><span style="color: #FF8000">from</span> <span style="color: #FFFFFF">numpy</span> <span style="color: #FF8000">import</span> <span style="color: #FFFFFF">arctan</span>, <span style="color: #FFFFFF">linspace</span>, <span style="color: #FFFFFF">pi</span>

<span style="color: #FF8000">class</span> <span style="color: #5E5EFF">Helix</span>( <span style="color: #FFFFFF">Plot</span>, <span style="color: #FFFFFF">Ops</span> ) :
    <span style="color: #02FF02">&#39;&#39;&#39;</span>
<span style="color: #02FF02">    Plot a Helix, Cylindrical Helix or Nested Cylindrical Helix</span>
<span style="color: #02FF02">    +-----------+------------------------------+--------------+</span>
<span style="color: #02FF02">    | Parameter |          Definition          |    Values    |</span>
<span style="color: #02FF02">    +-----------+------------------------------+--------------+</span>
<span style="color: #02FF02">    |    rh1    | outer helical radius         | (-inf, inf)  |</span>
<span style="color: #02FF02">    +-----------+------------------------------+--------------+</span>
<span style="color: #02FF02">    |    rh2    | inner helical radius         | (-inf, inf)  |</span>
<span style="color: #02FF02">    +-----------+------------------------------+--------------+</span>
<span style="color: #02FF02">    |    rc     | cylindrical radius           | (-inf, inf)  |</span>
<span style="color: #02FF02">    +-----------+------------------------------+--------------+</span>
<span style="color: #02FF02">    |     p     | pitch (height after 1 turn)  | (-inf, inf)  |</span>
<span style="color: #02FF02">    +-----------+------------------------------+--------------+</span>
<span style="color: #02FF02">    |    d1     | outer direction of rotation  |   -1 or +1   |</span>
<span style="color: #02FF02">    +-----------+------------------------------+--------------+</span>
<span style="color: #02FF02">    |    d2     | inner direction of rotation  |   -1 or +1   |</span>
<span style="color: #02FF02">    +-----------+------------------------------+--------------+</span>
<span style="color: #02FF02">    |    dc     | rotation of circle           | (-inf, inf)  |</span>
<span style="color: #02FF02">    +-----------+------------------------------+--------------+</span>
<span style="color: #02FF02">    |    t1     | numb. of outer helical turns |  ( 0, inf )  |</span>
<span style="color: #02FF02">    +-----------+------------------------------+--------------+</span>
<span style="color: #02FF02">    |    t2     | numb. of inner helical turns |  ( 0, inf )  |</span>
<span style="color: #02FF02">    +-----------+------------------------------+--------------+</span>
<span style="color: #02FF02">    |     m     | number of points per circle  | Integers &gt; 0 |</span>
<span style="color: #02FF02">    +-----------+------------------------------+--------------+</span>
<span style="color: #02FF02">    |     n     | number of circles in helix   | Integers &gt; 0 |</span>
<span style="color: #02FF02">    +-----------+------------------------------+--------------+</span>
<span style="color: #02FF02">    &#39;&#39;&#39;</span>
    <span style="color: #FF8000">def</span> <span style="color: #5E5EFF">cylindrical</span>( <span style="color: #FF69B4">self</span>, <span style="color: #FFFFFF">rh1</span>, <span style="color: #FFFFFF">rc</span>, <span style="color: #FFFFFF">dc</span>, <span style="color: #FFFFFF">p</span>, <span style="color: #FFFFFF">t1</span>, <span style="color: #FFFFFF">m</span>, <span style="color: #FFFFFF">n</span> ) :
        <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span>, <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">n</span> <span style="color: #FF8000">=</span> <span style="color: #FFFFFF">m</span>, <span style="color: #FFFFFF">n</span>
        <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">x</span>, <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">y</span>, <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">z</span> <span style="color: #FF8000">=</span> <span style="color: #FF69B4">zip</span>(
            <span style="color: #FF8000">*</span>[ <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">translate</span>(
                <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">rotate</span>(
                    <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">circle</span>( <span style="color: #FFFFFF">rc</span>, <span style="color: #FFFFFF">tc</span> ),
                    <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">vector</span>( <span style="color: #FFFFFF">rh1</span>, <span style="color: #FFFFFF">th</span> ),
                    <span style="color: #FF8000">-</span><span style="color: #FFFFFF">dc</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">pi</span><span style="color: #FF8000">/</span><span style="color: #FF00FF">2</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">arctan</span>( <span style="color: #FFFFFF">p</span><span style="color: #FF8000">/</span>(<span style="color: #FF00FF">2</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">pi</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">rh1</span>) )<span style="color: #FF8000">*</span><span style="color: #FFFFFF">rh1</span><span style="color: #FF8000">/</span><span style="color: #FF69B4">abs</span>( <span style="color: #FFFFFF">rh1</span> )
                    ),
                <span style="color: #FF8000">*</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">helix</span>( <span style="color: #FFFFFF">rh1</span>, <span style="color: #FFFFFF">th</span> )
                )
               <span style="color: #FF8000">for</span> <span style="color: #FFFFFF">th</span> <span style="color: #FF8000">in</span> <span style="color: #FFFFFF">linspace</span>( <span style="color: #FF00FF">0</span>, <span style="color: #FF00FF">2</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">pi</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">t1</span>, <span style="color: #FFFFFF">n</span> )
               <span style="color: #FF8000">for</span> <span style="color: #FFFFFF">tc</span> <span style="color: #FF8000">in</span> <span style="color: #FFFFFF">linspace</span>( <span style="color: #FF00FF">0</span>, <span style="color: #FF00FF">2</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">pi</span><span style="color: #FF8000">*</span>( <span style="color: #FF00FF">1</span> <span style="color: #FF8000">-</span> <span style="color: #FF00FF">1</span><span style="color: #FF8000">/</span><span style="color: #FFFFFF">m</span> ), <span style="color: #FFFFFF">m</span> ) ]
            )
        <span style="color: #FF8000">return</span> <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">x</span>, <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">y</span>, <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">z</span>

    <span style="color: #FF8000">def</span> <span style="color: #5E5EFF">cylindrical_double</span>( <span style="color: #FF69B4">self</span>, <span style="color: #FFFFFF">rh1</span>, <span style="color: #FFFFFF">rc</span>, <span style="color: #FFFFFF">p</span>, <span style="color: #FFFFFF">dca</span>, <span style="color: #FFFFFF">dcb</span>, <span style="color: #FFFFFF">t1</span>, <span style="color: #FFFFFF">m</span>, <span style="color: #FFFFFF">n</span> ) :
        <span style="color: #FFFFFF">x1</span>, <span style="color: #FFFFFF">y1</span>, <span style="color: #FFFFFF">z1</span> <span style="color: #FF8000">=</span> <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">cylindrical</span>(  <span style="color: #FFFFFF">rh1</span>, <span style="color: #FFFFFF">rc</span>, <span style="color: #FFFFFF">dca</span>, <span style="color: #FFFFFF">p</span>, <span style="color: #FFFFFF">t1</span>, <span style="color: #FFFFFF">m</span>, <span style="color: #FFFFFF">n</span> )
        <span style="color: #FFFFFF">x2</span>, <span style="color: #FFFFFF">y2</span>, <span style="color: #FFFFFF">z2</span> <span style="color: #FF8000">=</span> <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">cylindrical</span>( <span style="color: #FF8000">-</span><span style="color: #FFFFFF">rh1</span>, <span style="color: #FFFFFF">rc</span>, <span style="color: #FFFFFF">dcb</span>, <span style="color: #FFFFFF">p</span>, <span style="color: #FFFFFF">t1</span>, <span style="color: #FFFFFF">m</span>, <span style="color: #FFFFFF">n</span> )
        <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">x</span>, <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">y</span>, <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">z</span> <span style="color: #FF8000">=</span> <span style="color: #FFFFFF">x1</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">x2</span>, <span style="color: #FFFFFF">y1</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">y2</span>, <span style="color: #FFFFFF">z1</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">z2</span>
        <span style="color: #FF8000">return</span> <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">x</span>, <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">y</span>, <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">z</span>

    <span style="color: #FF8000">def</span> <span style="color: #5E5EFF">cylindrical_nested</span>( <span style="color: #FF69B4">self</span>, <span style="color: #FFFFFF">rh1</span>, <span style="color: #FFFFFF">rh2</span>, <span style="color: #FFFFFF">rc</span>, <span style="color: #FFFFFF">dc</span>, <span style="color: #FFFFFF">p</span>,
                              <span style="color: #FFFFFF">d1</span>,  <span style="color: #FFFFFF">d2</span>,  <span style="color: #FFFFFF">t1</span>, <span style="color: #FFFFFF">t2</span>,  <span style="color: #FFFFFF">m</span>, <span style="color: #FFFFFF">n</span> ) :
        <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">m</span>, <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">n</span> <span style="color: #FF8000">=</span> <span style="color: #FFFFFF">m</span>, <span style="color: #FFFFFF">n</span>
        <span style="color: #DD0000"># nested helix pitch</span>
        <span style="color: #FFFFFF">p2</span> <span style="color: #FF8000">=</span> <span style="color: #FFFFFF">t1</span><span style="color: #FF8000">*</span>( <span style="color: #FFFFFF">p</span><span style="color: #FF8000">**</span><span style="color: #FF00FF">2</span> <span style="color: #FF8000">+</span> (<span style="color: #FF00FF">2</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">pi</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">rh1</span>)<span style="color: #FF8000">**</span><span style="color: #FF00FF">2</span> )<span style="color: #FF8000">**</span><span style="color: #FF00FF">0.5</span><span style="color: #FF8000">/</span><span style="color: #FFFFFF">t2</span>
        <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">x</span>, <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">y</span>, <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">z</span> <span style="color: #FF8000">=</span> <span style="color: #FF69B4">zip</span>(
            <span style="color: #FF8000">*</span>[ <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">translate</span>(
                <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">rotate</span>(
                    <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">translate</span>(
                        <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">rotate</span>(
                            <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">circle</span>( <span style="color: #FFFFFF">rc</span>, <span style="color: #FFFFFF">tc</span> ),
                            <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">vector</span>( <span style="color: #FFFFFF">d2</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">rh2</span>, <span style="color: #FFFFFF">th</span> ),
                            <span style="color: #FFFFFF">d2</span><span style="color: #FF8000">*</span>( <span style="color: #FFFFFF">dc</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">pi</span><span style="color: #FF8000">/</span><span style="color: #FF00FF">2</span> <span style="color: #FF8000">-</span> <span style="color: #FFFFFF">arctan</span>( <span style="color: #FFFFFF">p2</span><span style="color: #FF8000">/</span>(<span style="color: #FF00FF">2</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">pi</span><span style="color: #FF8000">*</span><span style="color: #FF69B4">abs</span>( <span style="color: #FFFFFF">rh2</span> )) ) )
                            ),
                        <span style="color: #FF8000">*</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">vector</span>( <span style="color: #FFFFFF">d2</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">rh2</span>, <span style="color: #FFFFFF">th</span> )
                        ),
                    <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">vector</span>( <span style="color: #FFFFFF">d2</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">rh1</span>, <span style="color: #FFFFFF">th</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">t1</span><span style="color: #FF8000">/</span><span style="color: #FFFFFF">t2</span>  ),
                    <span style="color: #FFFFFF">d1</span><span style="color: #FF8000">*</span>( <span style="color: #FFFFFF">pi</span><span style="color: #FF8000">/</span><span style="color: #FF00FF">2</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">arctan</span>(  <span style="color: #FFFFFF">d2</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">p</span><span style="color: #FF8000">/</span>(<span style="color: #FF00FF">2</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">pi</span><span style="color: #FF8000">*</span><span style="color: #FF69B4">abs</span>( <span style="color: #FFFFFF">rh1</span> )) ) )
                    ),
                <span style="color: #FF8000">*</span><span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">helix</span>( <span style="color: #FFFFFF">d1</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">rh1</span>, <span style="color: #FFFFFF">p</span>, <span style="color: #FFFFFF">th</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">t1</span><span style="color: #FF8000">/</span><span style="color: #FFFFFF">t2</span> )
                )
               <span style="color: #FF8000">for</span> <span style="color: #FFFFFF">th</span> <span style="color: #FF8000">in</span> <span style="color: #FFFFFF">linspace</span>( <span style="color: #FF00FF">0</span>, <span style="color: #FF00FF">2</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">pi</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">t2</span>, <span style="color: #FFFFFF">n</span> )
               <span style="color: #FF8000">for</span> <span style="color: #FFFFFF">tc</span> <span style="color: #FF8000">in</span> <span style="color: #FFFFFF">linspace</span>( <span style="color: #FF00FF">0</span>, <span style="color: #FF00FF">2</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">pi</span><span style="color: #FF8000">*</span>( <span style="color: #FF00FF">1</span> <span style="color: #FF8000">-</span> <span style="color: #FF00FF">1</span><span style="color: #FF8000">/</span><span style="color: #FFFFFF">m</span> ), <span style="color: #FFFFFF">m</span> ) ]
            )
        <span style="color: #FF8000">return</span> <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">x</span>, <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">y</span>, <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">z</span>

    <span style="color: #FF8000">def</span> <span style="color: #5E5EFF">double_cylindrical_nested</span>( <span style="color: #FF69B4">self</span>,
                                    <span style="color: #FFFFFF">rh1</span>, <span style="color: #FFFFFF">rh2</span>, <span style="color: #FFFFFF">rc</span>,  <span style="color: #FFFFFF">p</span>, <span style="color: #FFFFFF">dca</span>, <span style="color: #FFFFFF">dcb</span>,
                                     <span style="color: #FFFFFF">d1</span>,  <span style="color: #FFFFFF">d2</span>, <span style="color: #FFFFFF">t1</span>, <span style="color: #FFFFFF">t2</span>,   <span style="color: #FFFFFF">m</span>,   <span style="color: #FFFFFF">n</span> ) :
        <span style="color: #FFFFFF">x1</span>, <span style="color: #FFFFFF">y1</span>, <span style="color: #FFFFFF">z1</span> <span style="color: #FF8000">=</span> <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">cylindrical_nested</span>(
            <span style="color: #FFFFFF">rh1</span>, <span style="color: #FF8000">-</span><span style="color: #FFFFFF">rh2</span>, <span style="color: #FFFFFF">rc</span>, <span style="color: #FFFFFF">dca</span>, <span style="color: #FFFFFF">p</span>, <span style="color: #FFFFFF">d1</span>, <span style="color: #FFFFFF">d2</span>, <span style="color: #FFFFFF">t1</span>, <span style="color: #FFFFFF">t2</span>, <span style="color: #FFFFFF">m</span>, <span style="color: #FFFFFF">n</span>
            )
        <span style="color: #FFFFFF">x2</span>, <span style="color: #FFFFFF">y2</span>, <span style="color: #FFFFFF">z2</span> <span style="color: #FF8000">=</span> <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">cylindrical_nested</span>(
            <span style="color: #FFFFFF">rh1</span>,  <span style="color: #FFFFFF">rh2</span>, <span style="color: #FFFFFF">rc</span>, <span style="color: #FFFFFF">dcb</span>, <span style="color: #FFFFFF">p</span>, <span style="color: #FFFFFF">d1</span>, <span style="color: #FFFFFF">d2</span>, <span style="color: #FFFFFF">t1</span>, <span style="color: #FFFFFF">t2</span>, <span style="color: #FFFFFF">m</span>, <span style="color: #FFFFFF">n</span>
            )
        <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">x</span>, <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">y</span>, <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">z</span> <span style="color: #FF8000">=</span> <span style="color: #FFFFFF">x1</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">x2</span>, <span style="color: #FFFFFF">y1</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">y2</span>, <span style="color: #FFFFFF">z1</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">z2</span>
        <span style="color: #FF8000">return</span> <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">x</span>, <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">y</span>, <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">z</span>

    <span style="color: #FF8000">def</span> <span style="color: #5E5EFF">cylindrical_sextuple</span>( <span style="color: #FF69B4">self</span>,
                              <span style="color: #FFFFFF">rh1a</span>, <span style="color: #FFFFFF">rh1b</span>, <span style="color: #FFFFFF">rh2a</span>, <span style="color: #FFFFFF">rh2b</span>,
                                <span style="color: #FFFFFF">rc</span>,    <span style="color: #FFFFFF">p</span>, <span style="color: #FFFFFF">dc1a</span>, <span style="color: #FFFFFF">dc1b</span>,
                              <span style="color: #FFFFFF">dc2a</span>, <span style="color: #FFFFFF">dc2b</span>,  <span style="color: #FFFFFF">d1a</span>,  <span style="color: #FFFFFF">d1b</span>,
                               <span style="color: #FFFFFF">d2a</span>,  <span style="color: #FFFFFF">d2b</span>,  <span style="color: #FFFFFF">t1a</span>,  <span style="color: #FFFFFF">t1b</span>,
                               <span style="color: #FFFFFF">t2a</span>,  <span style="color: #FFFFFF">t2b</span>,    <span style="color: #FFFFFF">m</span>,    <span style="color: #FFFFFF">n</span> ) :
        <span style="color: #FFFFFF">x1</span>, <span style="color: #FFFFFF">y1</span>, <span style="color: #FFFFFF">z1</span> <span style="color: #FF8000">=</span> <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">double_cylindrical_nested</span>(
            <span style="color: #FF8000">-</span><span style="color: #FFFFFF">rh1a</span>, <span style="color: #FFFFFF">rh2a</span>, <span style="color: #FFFFFF">rc</span>, <span style="color: #FFFFFF">p</span>, <span style="color: #FFFFFF">dc1a</span>, <span style="color: #FFFFFF">dc2a</span>, <span style="color: #FFFFFF">d1a</span>, <span style="color: #FFFFFF">d2a</span>, <span style="color: #FFFFFF">t1a</span>, <span style="color: #FFFFFF">t2a</span>, <span style="color: #FFFFFF">m</span>, <span style="color: #FFFFFF">n</span>
            )
        <span style="color: #FFFFFF">x2</span>, <span style="color: #FFFFFF">y2</span>, <span style="color: #FFFFFF">z2</span> <span style="color: #FF8000">=</span> <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">double_cylindrical_nested</span>(
             <span style="color: #FFFFFF">rh1b</span>, <span style="color: #FFFFFF">rh2b</span>, <span style="color: #FFFFFF">rc</span>, <span style="color: #FFFFFF">p</span>, <span style="color: #FFFFFF">dc1b</span>, <span style="color: #FFFFFF">dc2b</span>, <span style="color: #FFFFFF">d1b</span>, <span style="color: #FFFFFF">d2b</span>, <span style="color: #FFFFFF">t1b</span>, <span style="color: #FFFFFF">t2b</span>, <span style="color: #FFFFFF">m</span>, <span style="color: #FFFFFF">n</span>
            )
        <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">x</span>, <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">y</span>, <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">z</span> <span style="color: #FF8000">=</span> <span style="color: #FFFFFF">x1</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">x2</span>, <span style="color: #FFFFFF">y1</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">y2</span>, <span style="color: #FFFFFF">z1</span> <span style="color: #FF8000">+</span> <span style="color: #FFFFFF">z2</span>
        <span style="color: #FF8000">return</span> <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">x</span>, <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">y</span>, <span style="color: #FF69B4">self</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">z</span>
</pre></div>
</td></tr></table>
        </div>
        </td></tr>
    </table>
    <h1 style="color:#02FF02">Examples</h1>
    <p>
      Below are some example plots generated using the Helix class.
      All of these structures are cylindrical sextuple helices (double double cylindrical nested helices).
      These are animated png files. If your browser does not support animated png files, please switch to one that does.
    </p>
    <table align="center">
      <tr><td><h2 style="color:#02FF02" align="center">Slinky Helix</h2></td></tr>
      <tr><td><img src="models/sextuple_1.png" /></td></tr>
      <tr><td><h2 style="color:#02FF02" align="center">Sculpturesque</h2></td></tr>
      <tr><td><img src="models/sextuple_2.png" /></td></tr>
      <tr><td><h2 style="color:#02FF02" align="center">Lazy Helix</h2></td></tr>
      <tr><td><img src="models/sextuple_3.png" /></td></tr>
      <tr><td><h2 style="color:#02FF02" align="center">Snakey Helix</h2></td></tr>
      <tr><td><img src="models/sextuple_4.png" /></td></tr>
      <tr><td><h2 style="color:#02FF02" align="center">Fountain Helix</h2></td></tr>
      <tr><td><img src="models/sextuple_5.png" /></td></tr>
    </table>
    <h1 style="color:#02FF02">Try It</h1>
    <p>
      To start generating your own structures, use the script below and experiment with the parameters.
    </p>
    <table align="center">
      <tr><td>
        <div style="height:300px; width:750px; overflow:auto; font-family:courier">
<table class="table"><tr><td><div class="linenodiv" style="background-color: #454545; padding-right: 10px"><pre style="line-height: 125%"> 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23</pre></div></td><td class="code"><div style="background: #002240"><pre style="line-height: 125%"><span></span><span style="color: #FFFFFF">helix</span> <span style="color: #FF8000">=</span> <span style="color: #FFFFFF">Helix</span>()
<span style="color: #FFFFFF">helix</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">cylindrical_nested</span>(
    <span style="color: #FFFFFF">rh1</span> <span style="color: #FF8000">=</span> <span style="color: #FFFFFF">pi</span><span style="color: #FF8000">/</span><span style="color: #FF00FF">2</span>, <span style="color: #FFFFFF">rh2</span> <span style="color: #FF8000">=</span> <span style="color: #FFFFFF">pi</span><span style="color: #FF8000">/</span><span style="color: #FF00FF">3</span>,
     <span style="color: #FFFFFF">rc</span> <span style="color: #FF8000">=</span> <span style="color: #FFFFFF">pi</span><span style="color: #FF8000">/</span><span style="color: #FF00FF">6</span>,  <span style="color: #FFFFFF">dc</span> <span style="color: #FF8000">=</span> <span style="color: #FF00FF">1</span>,
      <span style="color: #FFFFFF">p</span> <span style="color: #FF8000">=</span> <span style="color: #FF00FF">2</span><span style="color: #FF8000">*</span><span style="color: #FFFFFF">pi</span>,
     <span style="color: #FFFFFF">d1</span> <span style="color: #FF8000">=</span>    <span style="color: #FF00FF">1</span>,  <span style="color: #FFFFFF">d2</span> <span style="color: #FF8000">=</span> <span style="color: #FF00FF">1</span>,
     <span style="color: #FFFFFF">t1</span> <span style="color: #FF8000">=</span>    <span style="color: #FF00FF">1</span>,  <span style="color: #FFFFFF">t2</span> <span style="color: #FF8000">=</span> <span style="color: #FF00FF">5</span>,
      <span style="color: #FFFFFF">m</span> <span style="color: #FF8000">=</span>    <span style="color: #FF00FF">7</span>,   <span style="color: #FFFFFF">n</span> <span style="color: #FF8000">=</span> <span style="color: #FF00FF">37</span>
    ) 
<span style="color: #FFFFFF">helix</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">surface</span>()
<span style="color: #FFFFFF">helix</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">cylindrical_sextuple</span>(
    <span style="color: #FFFFFF">rh1a</span> <span style="color: #FF8000">=</span>   <span style="color: #FF00FF">2</span>, <span style="color: #FFFFFF">rh1b</span> <span style="color: #FF8000">=</span>  <span style="color: #FF00FF">2</span>,
    <span style="color: #FFFFFF">rh2a</span> <span style="color: #FF8000">=</span>   <span style="color: #FF00FF">1</span>, <span style="color: #FFFFFF">rh2b</span> <span style="color: #FF8000">=</span>  <span style="color: #FF00FF">1</span>,
      <span style="color: #FFFFFF">rc</span> <span style="color: #FF8000">=</span> <span style="color: #FF00FF">0.7</span>, <span style="color: #FFFFFF">p</span>    <span style="color: #FF8000">=</span> <span style="color: #FF8000">-</span><span style="color: #FF00FF">9</span>,
    <span style="color: #FFFFFF">dc1a</span> <span style="color: #FF8000">=</span>   <span style="color: #FF00FF">1</span>, <span style="color: #FFFFFF">dc1b</span> <span style="color: #FF8000">=</span>  <span style="color: #FF00FF">1</span>,
    <span style="color: #FFFFFF">dc2a</span> <span style="color: #FF8000">=</span>   <span style="color: #FF00FF">1</span>, <span style="color: #FFFFFF">dc2b</span> <span style="color: #FF8000">=</span>  <span style="color: #FF00FF">1</span>,
     <span style="color: #FFFFFF">d1a</span> <span style="color: #FF8000">=</span>   <span style="color: #FF00FF">1</span>,  <span style="color: #FFFFFF">d1b</span> <span style="color: #FF8000">=</span>  <span style="color: #FF00FF">1</span>,
     <span style="color: #FFFFFF">d2a</span> <span style="color: #FF8000">=</span>   <span style="color: #FF00FF">1</span>,  <span style="color: #FFFFFF">d2b</span> <span style="color: #FF8000">=</span> <span style="color: #FF8000">-</span><span style="color: #FF00FF">1</span>,
     <span style="color: #FFFFFF">t1a</span> <span style="color: #FF8000">=</span>   <span style="color: #FF00FF">1</span>,  <span style="color: #FFFFFF">t1b</span> <span style="color: #FF8000">=</span>  <span style="color: #FF00FF">1</span>,
     <span style="color: #FFFFFF">t2a</span> <span style="color: #FF8000">=</span> <span style="color: #FF00FF">2.5</span>,  <span style="color: #FFFFFF">t2b</span> <span style="color: #FF8000">=</span>  <span style="color: #FF00FF">3</span>,
       <span style="color: #FFFFFF">m</span> <span style="color: #FF8000">=</span>   <span style="color: #FF00FF">3</span>,  <span style="color: #FFFFFF">n</span>   <span style="color: #FF8000">=</span> <span style="color: #FF00FF">50</span>
    )
<span style="color: #FFFFFF">helix</span><span style="color: #FF8000">.</span><span style="color: #FFFFFF">surface</span>( <span style="color: #FFFFFF">color1</span> <span style="color: #FF8000">=</span> <span style="color: #02FF02">&#39;pink&#39;</span>, <span style="color: #FFFFFF">color2</span> <span style="color: #FF8000">=</span> <span style="color: #02FF02">&#39;purple&#39;</span> )
</pre></div>
</td></tr></table>
    </div>
        </td></tr>
    </table>
  </body>
</html>

