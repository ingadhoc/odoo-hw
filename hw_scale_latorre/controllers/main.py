import logging
from threading import Thread

import openerp.addons.hw_proxy.controllers.main as hw_proxy
from openerp import http

_logger = logging.getLogger(__name__)

try:
    import serial
except ImportError:
    _logger.error('Odoo module hw_scale depends on the pyserial python module')
    serial = None


class ScaleLatorre(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.serial = serial.Serial()

    def get_weight(self):
        return self.serial.read()

    def get_weight_info(self):
        return 'ok'


s = ScaleLatorre()


class ScaleDriver(hw_proxy.Proxy):

    @http.route('/hw_proxy/scale_latorre_read/', type='json', auth='none')
    def scale_read(self):
        '''
        This function is accessible if there is only one database installed
        in the instance.

        You can test this with curl:

        curl -H "Content-Type: application/json" -d '{}' http://localhost:8069/hw_proxy/scale_latorre_read
        '''
        return {
            'weight': s.get_weight(),
            'unit': 'kg',
            'info': s.get_weight_info(),
        }
