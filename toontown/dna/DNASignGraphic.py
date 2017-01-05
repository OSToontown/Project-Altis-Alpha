from panda3d.core import LVector4f, DecalEffect
import DNAProp
import DNAError
import DNAUtil

class DNASignGraphic(DNAProp.DNAProp):
    COMPONENT_CODE = 8

    def __init__(self, name):
        DNAProp.DNAProp.__init__(self, name)
        self.width = 0
        self.height = 0

    def makeFromDGI(self, dgi, store):
        DNAProp.DNAProp.makeFromDGI(self, dgi, store)
        self.width = dgi.getInt16() / 100.0
        self.height = dgi.getInt16() / 100.0
        dgi.getBool()

    def traverse(self, nodePath, dnaStorage):
        node = dnaStorage.findNode(self.code)
        if node is None:
            raise DNAError.DNAError('DNASignGraphic code ' + self.code + ' not found in storage')
        node = node.copyTo(nodePath)
        node.setScale(self.scale)
        node.setScale(node, self.getParent().scale)
        node.setPosHpr(self.pos, self.hpr)
        node.setDepthWrite(True)
        node.setDepthTest(True)
        #node.setDepthOffset(10)
        
        node.setEffect(DecalEffect.make())
        node.getNode(0).setEffect(DecalEffect.make())
        
        node.setY(node, -0.025)
        self.traverseChildren(node, dnaStorage)