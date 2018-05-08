# import the Qt components we'll use    
from PyQt5.QtCore import (
    Qt
    )
    
from PyQt5.QtWidgets import (
    QItemDelegate
    )
           
class FloatDelegate(QItemDelegate):
    
    def __init__(self, decimals, parent=None):
        QItemDelegate.__init__(self, parent=parent)
        self.nDecimals = decimals

    def paint(self, painter, option, index):
        value = index.model().data(index, Qt.EditRole)
        try:
            number = float(value)        
            painter.drawText(option.rect, Qt.AlignCenter, "{:.{}f}".format(number, self.nDecimals))
        except :
            QItemDelegate.paint(self, painter, option, index)            
