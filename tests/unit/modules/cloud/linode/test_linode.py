from __future__ import (absolute_import, division, print_function)

import pytest

from ansible_collections.ansible.misc.plugins.modules import linode
from ansible_collections.ansible.misc.tests.unit.modules.utils import set_module_args

if not linode.HAS_LINODE:
    pytestmark = pytest.mark.skip('test_linode.py requires the `linode-python` module')


def test_name_is_a_required_parameter(api_key, auth):
    with pytest.raises(SystemExit):
        set_module_args({})
        linode.main()
