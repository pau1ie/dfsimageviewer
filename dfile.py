from PyQt5 import QtCore
from displayfile import Ui_fileDialog
from PyQt5.QtWidgets import QDialog

class fileContents(QDialog, Ui_fileDialog):
    def __init__(self):
        self.fileContents=""
        super().__init__()
        self.setupUI(self)

    def setupUI(self,dialogue):
        super().setupUi(dialogue)

    def refreshAll(self, fileContents):
        self.fileContents = fileContents
        self.hexDump.setText(self.xDump())
        self.basicText.setText(self.basDump())
        self.plainText.setText(self.texDump())

    @QtCore.pyqtSlot()
    def prev(self):
        pass

    @QtCore.pyqtSlot()
    def next(self):
        pass

    def xDump(self):
        output=""
        col2=""
        stride=16

        for i in range(len(self.fileContents)):

            if ( i%stride == 0 ):
                output += "  "+col2+"\r{0:08x} ".format(i)
                col2=""

            output+="{0:02X}".format(self.fileContents[i])
            if ( 31 < self.fileContents[i] < 127 ):
                col2+=chr(self.fileContents[i])
            else:
                col2+='.'
        return output

    def basDump(self):
        d = ""
        line = 0
        llen = 0
        raw = 0
        decode = ""
        output = ""
        lend = 0
        lno =0
        n1=0
        n2=0
        n3=0
        low=0
        high=0
        i=0
        tokens = { 128: 'AND', 129: 'DIV', 130: 'EOR', 131: 'MOD', 132: 'OR',
             133: 'ERROR', 134: 'LINE', 135: 'OFF', 136: 'STEP', 137: 'SPC',
             138: 'TAB(', 139: 'ELSE', 140: 'THEN', 142: 'OPENIN', 143: 'PTR',
             144: 'PAGE', 145: 'TIME', 146: 'LOMEM', 147: 'HIMEM', 148: 'ABS',
             149: 'ACS', 150: 'ADVAL', 151: 'ASC', 152: 'ASN', 153: 'ATN',
             154: 'BGET', 155: 'COS', 156: 'COUNT', 157: 'DEG', 158: 'ERL',
             159: 'ERR', 160: 'EVAL', 161: 'EXP', 162: 'EXT', 163: 'FALSE',
             164: 'FN', 165: 'GET', 166: 'INKEY', 167: 'INSTR(', 168: 'INT',
             169: 'LEN', 170: 'LN', 171: 'LOG', 172: 'NOT', 173: 'OPENUP',
             174: 'OPENOUT', 175: 'PI', 176: 'POINT(', 177: 'POS', 178: 'RAD',
             179: 'RND', 180: 'SGN', 181: 'SIN', 182: 'SQR', 183: 'TAN',
             184: 'TO', 185: 'TRUE', 186: 'USR', 187: 'VAL', 188: 'VPOS',
             189: 'CHR$', 190: 'GET$', 191: 'INKEY$', 192: 'LEFT$(', 193: 'MID$(',
             194: 'RIGHT$(', 195: 'STR$', 196: 'STRING$(', 197: 'EOF', 198: 'AUTO',
             199: 'DELETE', 200: 'LOAD', 201: 'LIST', 202: 'NEW', 203: 'OLD',
             204: 'RENUMBER', 205: 'SAVE', 207: 'PTR', 208: 'PAGE', 209: 'TIME',
             210: 'LOMEM', 211: 'HIMEM', 212: 'SOUND', 213: 'BPUT', 214: 'CALL',
             215: 'CHAIN', 216: 'CLEAR', 217: 'CLOSE', 218: 'CLG', 219: 'CLS',
             220: 'DATA', 221: 'DEF', 222: 'DIM', 223: 'DRAW', 224: 'END',
             225: 'ENDPROC', 226: 'ENVELOPE', 227: 'FOR', 228: 'GOSUB', 229: 'GOTO',
             230: 'GCOL', 231: 'IF', 232: 'INPUT', 233: 'LET', 234: 'LOCAL',
             235: 'MODE', 236: 'MOVE', 237: 'NEXT', 238: 'ON', 239: 'VDU',
             240: 'PLOT', 241: 'PRINT', 242: 'PROC', 243: 'READ', 244: 'REM',
             245: 'REPEAT', 246: 'REPORT', 247: 'RESTORE', 248: 'RETURN',
             249: 'RUN', 250: 'STOP', 251: 'COLOUR', 252: 'TRACE', 253: 'UNTIL',
             254: 'WIDTH', 255: 'OSCLI' }

        while i < len(self.fileContents):
            if self.fileContents[i] != 13:
                output+="\nBad Program (Expected ^M at start of line)."
                ret=False
                break
            i+=1

            # Line number high
            if self.fileContents[i] == 255 :
                break

            if len(self.fileContents) < i+2 :
                output += "\nBad Program (Line finishes before metadata)."
                ret=False
                break

            line=self.fileContents[i]*256
            i+=1

            # Line number low
            line = line+self.fileContents[i]
            i+=1

            # Line length
            llen = self.fileContents[i]-4
            if llen < 0 :
                output += "\nBad Program (Line length too short)"
                ret = False

            raw=0
            decode=""
            lend=i+llen
            if lend > len(self.fileContents):
                output += "\nBad Program (Line truncated)"
                ret = False

            # Read rest of line
            while i < lend :
                i+=1
                if raw==1:
                    d=chr(self.fileContents[i])
                else:
                    if self.fileContents[i] == 0x8D :
                        # Line token
                        i+=1
                        n1 = self.fileContents[i]
                        i+=1
                        n2 = self.fileContents[i]
                        i+=1
                        n3 = self.fileContents[i]
                        # This comes from page 41 of "The BASIC ROM User Guide"
                        n1=(n1*4)&255
                        low=(n1 & 192 ) ^ n2
                        n1=(n1*4)&255
                        high=n1^n3
                        lno=high*256+low
                        d=lno
                    else:
                        if self.fileContents[i] in tokens :
                            d='<span style=\" color: #0000ff;\">'+tokens[self.fileContents[i]]+'</span>'
                        else:
                            d=str(chr(self.fileContents[i]))
                if chr(self.fileContents[i]) == '"' :
                    raw=1-raw
                    if raw == 1 :
                        decode += '<span style=\" color: #ff0000;\">' + str(d)
                    else:
                        decode += str(d) + '</span>'
                elif chr(self.fileContents[i]) == '<':
                    decode += '&lt;'
                else:
                    decode += str(d)
            output += "{0:6d}{1:s}\n".format(line,decode)
            i+=1
        return '<pre>'+output+'</pre>'

    def texDump(self):
        output = ""
        i=0
        while i < len(self.fileContents):
            if 31 < self.fileContents[i] < 127 :
                output+=chr(self.fileContents[i])
            else:
                output+='['+format(self.fileContents[i],'02x')+']'
                if (self.fileContents[i] == 10 or self.fileContents[i]==13):
                    output += '<br />'
            i+=1
        return '<pre>'+output+'</pre>'
