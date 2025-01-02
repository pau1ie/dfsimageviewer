class Model:
    def __init__( self ):
        '''
        Initializes the two members the class holds:
        the file name and its contents.
        '''
        self.fileName = None

    def clearDiscImage(self):
        self.fileContent = ""
        self.discTitle = ""
        self.discWrites=0
        self.discSize=0
        self.bootOption=0
        self.ifileName = []
        self.idir = []
        self.iloadAddress = []
        self.iexecAddress = []
        self.ilength = []
        self.istartSector = []
        self.ilocked = []
		
    def isValid( self, fileName ):
        '''
        returns True if the file exists and can be
        opened.  Returns False otherwise.
        '''
        try: 
            file = open( fileName, 'r' )
            file.close()
            return True
        except:
            return False

    def setFileName( self, fileName ):
        '''
        sets the member fileName to the value of the argument
        if the file exists.  Otherwise resets both the filename
        and file contents members.
        '''
        if self.isValid( fileName ):
            print(fileName)
            self.fileName = fileName
            self.clearDiscImage()
            self.openFile()
        else:
            self.fileContents = ""
            self.fileName = ""

    def openFile( self ):
        self.fileContents = open( self.fileName, 'rb' ).read()
        print("Type:"+str(type(self.fileContents)))
        self.discTitle=(self.fileContents[0:8]+self.fileContents[0x100:0x103]).decode("utf-8").rstrip('\x00')
        self.discWrites=int(self.fileContents[0x104])
        self.discSectors=int(self.fileContents[0x107])+int((self.fileContents[0x106]&0x03)<<8)
        self.bootOption=int(self.fileContents[0x106]>>4)
        self.readCatalogue()
        print(self.bootOption)
		
    def readSevenBit(self,start,length):
        st=""
        for i in range(start,start+length):
            st+=chr(self.fileContents[i]&0x7f)
        return st.rstrip('\x00')
		
    def readCatalogue(self):
        nameoffset=8
        detailoffset=0x108
        for i in range(31):
            print(i)
            self.ifileName.append(self.readSevenBit(i*8+nameoffset,7))
            self.idir.append(self.readSevenBit(i*8+nameoffset+7,1))
            self.iloadAddress.append(int(self.fileContents[i*8+detailoffset]) \
			              + 0x100*int(self.fileContents[i*8+detailoffset+1]) \
				          + 0x10000*int((self.fileContents[i*8+detailoffset+6]&0x0c)>>2))
            self.iexecAddress.append(int(self.fileContents[i*8+detailoffset+2]) \
			              + 0x100*int(self.fileContents[i*8+detailoffset+3]) \
                          + 0x10000*int((self.fileContents[i*8+detailoffset+6]&0xc0)>>6))
            self.ilength.append(int(self.fileContents[i*8+detailoffset+4]) \
			         + 0x100*int(self.fileContents[i*8+detailoffset+5]) \
                     + 0x1000*int((self.fileContents[i*8+detailoffset+6]&0x30)>>4))
            self.istartSector.append(int(self.fileContents[i*8+detailoffset+7]) \
                         + 0x100*int(self.fileContents[i*8+detailoffset+6]&0x03))
            self.ilocked.append(self.fileContents[i*8+nameoffset+7]&0x80>>7)
        print (*self.ifileName)
        print (*self.idir)
        print (*self.iloadAddress)
        print (*self.ilength)
        print (*self.istartSector)
        print (*self.iexecAddress)

    def getFileName( self ):
        '''
        Returns the name of the file name member.
        '''
        return self.fileName
	
    def getBootOption( self ):
        return self.bootOption
	
    def getWrites( self ):
        return self.discWrites

    def getTitle( self ):
        return self.discTitle
	
    def getSize(self):
        return self.discSectors*256/1024

    def getFileContents( self ):
        '''
        Returns the contents of the file if it exists, otherwise
        returns an empty string.
        '''
        return self.fileContents

    def getFileEntry(self,catentry):
        '''
        Returns the contents of a file at the cataloge entry 
        '''
        return self.fileContents[ \
                 self.istartSector[catentry]*256: \
                 self.istartSector[catentry]*256  \
                 + self.ilength[catentry]]
