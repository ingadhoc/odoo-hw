from mock import patch
import serial

from openerp.tests.common import TransactionCase
from openerp.addons.hw_scale_latorre.controllers.main import ScaleLatorre


class TestScaleDriver(TransactionCase):

    @patch.object(serial.Serial, 'read', autospec=True)
    def test_something(self, mock_read):
        mock_read.return_value = '1234'

        scale_driver = ScaleLatorre()
        weight = scale_driver.get_weight()

        self.assertEquals('1234', weight)
