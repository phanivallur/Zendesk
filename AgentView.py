class ZDView:
      def setRawTitle(self, value):
          self.rawTitle=value
      def setRestriction(self, value):
          self.restriction=value
      def setDescription(self, value):
          self.description=value
      def setTitle(self, value):
          self.title=value
      def setUrl(self, value):
          self.url=value
      def setHighlights(self, value):
          self.highlights=value
      def setCreatedAt(self, value):
          self.createdAt=value
      def setUpdatedAt(self, value):
          self.updatedAt=value
      def setCountable(self, value):
          self.countable=value
      def setActive(self, value):
          self.active=value
      def setPosition(self, value):
          self.position=value
      def setId(self, value):
          self.id=value
 
      def getRawTitle(self):
          print("RawTitle:   "+str(self.rawTitle))
      def getRestriction(self):
          print("Restriction:   "+str(self.restriction))
      def getDescription(self):
          print("Description:   "+str(self.description))
      def getTitle(self):
          print("Title: "+str(self.title))
      def getUrl(self):
          print("URL:   "+str(self.url))
      def getHighlights(self):
          print("Highlights:   "+str(self.highlights))
      def getCreatedAt(self):
          print("Created at:   "+str(self.createdAt))
      def getUpdatedAt(self):
          print("Updated at:   "+str(self.updatedAt))
      def getCountable(self):
          print("Countable:   "+str(self.countable))
      def getActive(self):
          print("Active:   "+str(self.active))
      def getPosition(self):
          print("Position:   "+str(self.position))
      def getId(self):
          print("ID:   "+str(self.id))

      def display(self):
          self.getRawTitle()
          self.getRestriction()
          self.getDescription()
          self.getTitle()
          self.getUrl()
          self.getHighlights()
          self.getCreatedAt()
          self.getUpdatedAt()
          self.getCountable()
          self.getActive()
          self.getPosition()
          self.getId() 


       
