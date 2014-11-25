from mock import patch, Mock
from openerp.tests.common import TransactionCase

from openerp.addons.hw_scale_latorre.controllers.main import ScaleLatorre


class TestScaleDriver(TransactionCase):

    @patch('serial.Serial', new_callable=Mock(
        return_value=Mock(
            read=Mock(return_value='1234')
        )
    )
    )
    def test_something(self, serial_mock):
        serial_mock.return_value = Mock(
            return_value=Mock(
                read=Mock(return_value='1234')
            )
        )
        scale_driver = ScaleLatorre()
        weight = scale_driver.get_weight()
        self.assertEquals('1234', weight)
