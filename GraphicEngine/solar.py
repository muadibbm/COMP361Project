'''
Created on 7 janv. 2012

@author: num3ric
'''
from pandac.PandaModules import CollisionNode, CollisionSphere
#from pandac.PandaModules import Vec3, Point2
from panda3d.core import Vec3,Point2,BitMask32

class SphericalDraw(object):
    '''
    Information about a spherical object in the scene graph.
    It also encompasses a collision sphere of identical
    position and size.
    '''
    def __init__(self, SphericalBody, point_path=None):
        self.pos = Vec3(SphericalBody.position)
        self.vel = Vec3()
        self.size = 2*SphericalBody.radius
        
        # Dummy parent paths for both model & collision sphere
        #-----------------------------------------------------
        # root_path: This dummy node copying the parent position
        # is used as a center of orbit. The copy is necessary
        # so that the rotation of the orbiting body does not
        # affect the parent object.
        #
        # point_path: This dummy node path is only used to
        # displace the object, not to scale them. If we were to
        # scale them here, the scaling would propagate to child
        # nodes and make the sizes written set in the model very
        # strange. In short, the POSITIONS ARE RELATIVE but the
        # SCALING IS NOT. (Hence the "point" name.)
        #-----------------------------------------------------
        self.root_path = None
        if point_path == None:
            self.point_path = render.attachNewNode("sphere_node")
        else:
            self.root_path = point_path.attachNewNode("orbit_root_node")
            self.point_path = self.root_path.attachNewNode("sphere_node")
        self.point_path.setPos(self.pos)
        
        # Collision sphere for object picking
        #-----------------------------------------------------
        # As described in the Tut-Chessboard.py sample: "If this model was
        # any more complex than a single polygon, you should set up a collision
        # sphere around it instead."
        self.cnode = CollisionNode("coll_sphere_node")
        #We use no displacement (0,0,0) and no scaling factor (1)
        self.cnode.addSolid(CollisionSphere(0,0,0,1))
        self.cnode.setIntoCollideMask(BitMask32.bit(1))
        self.cnode_path = render.attachNewNode(self.cnode)
        #For temporary testing, display collision sphere.
#        self.cnode_path.show()

class StarDraw(SphericalDraw):
    '''
    Animating and rendering of a 3d star object.
    '''
    
    def __init__(self, star):
        super(StarDraw, self).__init__(star)
        self.star = star
        #Models & textures
        self.star_path = loader.loadModel("models/planet_sphere")
        self.star_tex = loader.loadTexture("models/star_dead_tex.jpg")
        self.star_path.setTexture(self.star_tex, 1)
        self.star_path.reparentTo(self.point_path)
        self.star_path.setScale(self.size)
        self.cnode.setTag('starTag', str(id(self)))
        # Reparenting the collision sphere so that it 
        # matches the star perfectly.
        self.cnode_path.reparentTo(self.star_path)



class PlanetDraw(SphericalDraw):
    '''
    Animating and rendering of a 3d planet object.
    '''
    
    def __init__(self, planet, star_point_path):
        super(PlanetDraw, self).__init__(planet, star_point_path)
        self.planet = planet
        self.orbital_velocity = planet.orbital_velocity
        #Models & textures
        self.planet_path = loader.loadModel("models/planet_sphere")
        self.planet_tex = loader.loadTexture("models/mars_1k_tex.jpg")
        self.planet_path.setTexture(self.planet_tex, 1)
        self.planet_path.reparentTo(self.point_path)
        self.planet_path.setScale(self.size)
        self.cnode.setTag('planetTag', str(id(self)))
        # Reparenting the collision sphere so that it 
        # matches the planet perfectly.
        self.cnode_path.reparentTo(self.planet_path)
    
    
    def startSpin(self):
        self.day_period_mercury = self.planet_path.hprInterval(
                                    self.planet.spin_velocity, Vec3(360, 0, 0))
        self.day_period_mercury.loop()
    
    def startOrbit(self):
        self.planet.orbital_velocity

        self.orbit_period_mercury = self.root_path.hprInterval(
                                    self.planet.orbital_velocity,
                                    Vec3(360, 0, 0))
        self.orbit_period_mercury.loop()
