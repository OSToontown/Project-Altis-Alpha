from panda3d.core import LVector4f, LVector3f, DecalEffect
import DNAGroup
import DNAError
import DNAUtil

class DNACornice(DNAGroup.DNAGroup):
    COMPONENT_CODE = 12

    def __init__(self, name):
        DNAGroup.DNAGroup.__init__(self, name)
        self.code = ''
        self.color = LVector4f(1)
        
    def getCode(self):
        return self.code
        
    def getColor(self):
        return self.color

    def makeFromDGI(self, dgi, store):
        DNAGroup.DNAGroup.makeFromDGI(self, dgi, store)
        self.code = DNAUtil.dgiExtractString8(dgi)
        self.color = DNAUtil.dgiExtractColor(dgi)

    def traverse(self, np, store):
        parentXScale = np.getParent().getScale().getX()
        parentZScale = np.getScale().getZ()
        scaleRatio = parentXScale / parentZScale
        
        node = store.findNode(self.code)
        if node.isEmpty():
            raise DNAError.DNAError('DNACornice code %d not found in DNAStorage' % self.code)
        
        internalNode = np.attachNewNode("cornice-internal")
        node = node.find("**/*_d")
        
        _np = node.copyTo(internalNode, 0)
        _np.setScale(1, scaleRatio, scaleRatio)
        _np.setEffect(DecalEffect.make())
        
        node = node.getParent().find("**/*_nd")
        np_d = node.copyTo(internalNode, 1)
        np_d.setScale(1, scaleRatio, scaleRatio)
        
        internalNode.setZ(node.getScale().getZ())
        internalNode.setColor(self.color)
        internalNode.flattenStrong()