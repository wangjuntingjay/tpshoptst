import pytest
from common.getdata import getdata
from page.login import Login


class TestLogin:

    def setup_class(self):
        self.login = Login()
        pass

    def teardown_class(self):
        pass

    @pytest.mark.parametrize('args', getdata("Login.json"))
    def test_001(self, args):
        # print(args)
        self.login.start_test(args["test_id"])
        self.login.login_success(args)
        self.login.end_test(args["test_id"])
