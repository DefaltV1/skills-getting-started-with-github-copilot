from copy import deepcopy

import pytest

from src import app as app_module


@pytest.fixture(autouse=True)
def isolate_activities():
    snapshot = deepcopy(app_module.activities)

    yield

    app_module.activities.clear()
    app_module.activities.update(snapshot)
