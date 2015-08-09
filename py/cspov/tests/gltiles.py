#!/usr/bin/env python
# encoding: utf-8
"""
All coordinates are (y,x) pairs

We assume a mercator projection using a WGS84 geoid
Scene coordinate are meters along the 0 parallel
y range +/- 6356752.3142 * 2 * pi => 39,940,652.742
x range +/- 6378137.0 * 2 * pi => 40,075,016.6856

References
https://bitbucket.org/rndblnch/opengl-programmable/raw/29d0c699c82a2ca961014e7eb5e6cd3a87fe5883/05-shader.py

Layers
    can hold more than one level of detail (LayerRepresentation), only 1-2 of which are activated at any given time
    can belong to multiple GLWidgets
    render GLDrawLists and GLActiveTextures that draw a subset of the overall layer data, with a suitable level of detail

GLDrawLists
    cannot belong to multiple widgets

GLTextures
    later: have a key so they can be shared and properly reference-counted
    can belong to multiple drawlists


Rendering loop
    For each layer
        Is layer current rendering ideal, i.e. well suited for this set of extents?
            No: put it on a dirty list to be re-rendered to a new drawlist
        Is the layer current rendering valid, i.e. is it even worth drawing?
            No: continue on to the next higher layer
        Render the drawlist of this layer with GLDrawList.paintGL()

Idle loop
    For each dirty layer
        Have layer render new draw list






"""
import sys
from collections import namedtuple
from OpenGL.GL import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtOpenGL import *
import numpy as np


DEFAULT_TILE_HEIGHT = 512   # 180°
DEFAULT_TILE_WIDTH = 1024   # 360°


# mercator
MAX_SCENE_Y = 39940660.0
MAX_SCENE_X = 40075020.0

box = namedtuple('box', ('bottom', 'left', 'top', 'right'))
rez = namedtuple('rez', ('dx', 'dy'))
pnt = namedtuple('pnt', ('x', 'y'))
geo = namedtuple('geo', ('lat', 'lon'))


class CoordSystem(object):
    """
    converts (y,x) pixel coordinates to geodetic coordinates in meters or degrees (lat/lon)
    """
    UNKNOWN = 0
    DATA_PIXELS = 1     # storage pixels for a given layer
    SCREEN_PIXELS = 2   # OpenGL pixels
    LATLON_DEGREES = 4  # lat/lon


class Layer(object):
    """
    A Layer
    - has one or more representations available to immediately draw
    - may want to schedule the rendering of other representations during idle time, to get ideal view
    - may have a backing science representation which is pure science data instead of pixel values or RGBA maps
    - typically will cache a "coarsest" single-tile representation for zoom-out events
    - can have probes attached which operate primarily on the science representation
    """
    def paint(self, extent_box, sample_rez):
        """
        draw the most appropriate representation for this layer
        if a better representation could be rendered for later draws, return False and render() will be queued for later idle time
        """
        return True

    def render(self, extent_box, sample_rez):
        """
        cache a rendering (typically a draw-list with textures) that best handles the extents and sampling requested
        return False if resources were too limited and a purge is needed among the layer stack
        """
        return True

    def purge(self):
        """
        release any cached representations that we haven't used lately, leaving at most 1
        return True if any GL resources were released
        """
        return False

    def probe_point_merc(self, xy_point):
        """
        return a value array for the requested point as specified in mercator-meters
        """
        raise NotImplementedError()

    def probe_point_geo(self, geo_point):
        """
        """
        raise NotImplementedError()

    def probe_shape(self, geo_shape):
        """
        given a shapely description of an area, return a masked array of data
        """
        raise NotImplementedError()





class GeoLayer(object):
    """
    A layer that has geospatial projection and follows the geospatial cursor
    """
    pass



class LayerRep(object):
    """
    Layer Representation that can be immediately drawn in OpenGL.
    Layers emit draw lists.
    Draw lists are cache entities that may no longer be valid if their extents or detail level are exceeded.
    When a DrawList is invalid, it gets phased out in favor of a new DrawList.
    """
    extents = (0.0, 0.0)  # view extents which we're able to render
    textures = None  # set of textures we need in order to draw
    layer = None   # layer we correspond to
    list_number = 0  # our draw list number, allocated from OpenGL

    # def __init__(self, number=0):


    def is_ideal_and_valid(self, extents, stride):
        """
        return pair of bools, (ideal, valid)
        ideal: are we able to fully represent this extent/stride?
        valid: are we even relevant for this extent/stride?
        typically, non-ideal will cause an assessment of whether another LOD should be brought in,
          but we might continue to use it temporarily (e.g. during zooms) for responsiveness
        non-valid will prevent the drawlist from being used
        """

    def draw(self, context):
        """
        given a prepared and scaled context, perform drawing
        """




class DataTilesFromFile(object):
    """
    A lazy-loaded image which can be mapped to a texture buffer and drawn on a polygon
    Represents a single x-y coordinate range at a single level of detail
    Will map data into GL texture memory for rendering
    """
    data = None
    tile_shape = None
    path = None
    _active = None     # {(y,x): (buffer,texture), ...}

    def __init__(self, path, element_dtype, shape, zero_point, tile_shape=(DEFAULT_TILE_HEIGHT, DEFAULT_TILE_WIDTH)):
        """
        map the file as read-only
        chop it into data tiles
        tiles are set up such that tile (0,0) starts with zero_point and goes up and to the right

        """
        self.data = np.memmap(path, element_dtype, 'r', shape=shape)
        self.tile_shape = tile_shape
        self.path = path
        self.zero_point = zero_point

    def activate(self, tile_y, tile_x, transform_func=None):
        """
        load a texture map from this data
        """
        buffer_id = glGenBuffers(1)

        # offset within the array
        th,tw = self.tile_shape
        ys = (tile_y*th)*self.zero_point[0]
        xs = (tile_x*tw)*self.zero_point[1]
        ye = ys + th
        xe = xs + tw
        npslice = self.data[ys:ye, xs:xe]

        # # start working with this buffer
        # glBindBuffer(GL_COPY_WRITE_BUFFER, buffer_id)
        # # allocate memory for it
        # glBufferData(GL_COPY_WRITE_BUFFER, , size, )
        # # borrow a writable pointer
        # pgl = glMapBuffer(, )
        # # make a numpy ndarray wrapper that targets that memory location
        #
        # # copy the data from the memory mapped file
        # # if there's not enough data in the file, fill with NaNs first
        # if npslice.shape != npgl.shape:
        #     npgl[:] = np.nan(0)
        #
        # if not transform_func:
        #     # straight copy
        #     np.copyto(npgl, npslice, casting='unsafe')
        # else:
        #     # copy through transform function
        #
        # # let GL push it to the GPU
        glUnmapBuffer(GL_COPY_WRITE_BUFFER)


    def deactivate(self, tile_y, tile_x):
        """
        release a given
        """








class GLGeoLodTileArray(GeoLayer):
    """
    A single level of detail with lazy loading of tiles
    Tiles may or may not be available
    Tiles follow a predictable lookup
    """

    def __init__(self, index, lod):
        """
        index is a mapping which { (0,0): GLTile(), ... }
        """
        pass


    def render(self, glcontext, extents, replacing_drawlist=None):
        """
        we're being activated, optionally using another layer that we want to align to
        for instance, if we're shifting LOD one will activate and the other will deactivate
        obtain any needed GL resources and prefill
        return a GLDrawList that draws us quickly while it's valid; come back
        """

        # make sure we've got all the textures we need

        # create a quad array that puts all the textures onto the screen

        pass


    def tileseq_in_area(self, index_bltr):
        """
        yield the sequence of tiles in a given rectangular tileseq_in_area
        """
        pass

    def tileseq_visible(self, data_bltr): 
        """
        given data coordinates, determine which tiles are on the canvas
        """
        pass




class Layer(object):
    def paintGL(self):
        glColor3f(0.0, 0.0, 1.0)
        glRectf(-5, -5, 5, 5)
        glColor3f(1.0, 0.0, 0.0)
        glBegin(GL_LINES)
        glVertex3f(0, 0, 0)
        glVertex3f(20, 20, 0)





class GeoTiledLayer(Layer):
    """
    We have one or more levels of detail (LOD).
    Provide GLDrawList entities to the main gl context draw loop.
    When enough changes to extents/stride occur, switch LOD and update to a new GLDrawList.
    Manage a tile texture pool
    """

class GeoTestPatternLayer(GeoTiledLayer):
    """
    a layer that shows a colored texture tile pattern
    """





class CsGlWidget(QGLWidget):
    layers = None

    def __init__(self, parent=None):
        super(CsGlWidget, self).__init__(parent)
        self.layers = [Layer()]

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        for layer in self.layers:
            layer.paintGL()

        glEnd()

    def resizeGL(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-50, 50, -50, 50, -50.0, 50.0)
        glViewport(0, 0, w, h)

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)



class MainWindow(QMainWindow):

    significant = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # self.windowTitleChanged.connect(self.onWindowTitleChange)
        self.setWindowTitle("gltiles")
        # layout = QStackedLayout()
        widget = QTabWidget()
        # things = [QDateEdit, QLabel, QDial, QDoubleSpinBox, QSpinBox, QProgressBar, QSlider, QRadioButton, QTimeEdit, QFontComboBox, QLineEdit]
        things = [CsGlWidget, QTextEdit]
        for w in things: 
            if w is QLabel:
                wid = QLabel('hola')
                font = wid.font()
                font.setPointSize(32)
                wid.setFont(font)
                wid.setAlignment(Qt.AlignHCenter)
            elif w is QLineEdit:
                q = QLineEdit()
                q.setPlaceholderText("I am text hear me roar")
                q.returnPressed.connect(self.return_pressed)
                q.selectionChanged.connect(self.selection_changed)
                q.textChanged.connect(self.text_changed)
                q.textEdited.connect(self.text_edited)
                self.line = q
                wid = q
            else:
                wid = w()
            # layout.addWidget(wid)
            widget.addTab(wid, str(w))

        self.setCentralWidget(widget)
        self.significant.connect(self.on_my_signal)

    def contextMenuEvent(self, e):
        print("context menu")
        super(MainWindow, self).contextMenuEvent(e)  # can also use e.accept() or e.ignore()

    def return_pressed(self):
        print('return pressed')
        self.line.setText("BOOM")

    def selection_changed(self):
        print('selection changed')

    def text_edited(self):
        print("text edited to " + repr(self.line.text()))

    def text_changed(self):
        print("text changed to " + repr(self.line.text()))

    def on_golden_pond(self, a):
        print(a)

    def on_button_pressed(self):
        print("bort")
        self.significant.emit('-bort-')

    def on_my_signal(self, s):
        print('there has been {0:s}'.format(s))


    # def onWindowTitleChange(self, s):
    #     print(s)


if __name__=='__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
