# This file is part of Shoop Wintergear Demo.
#
# Copyright (c) 2012-2015, Shoop Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.

from shoop.themes.classic_gray.views import product_price  # noqa
from .basket import basket_partial  # noqa

__all__ = ["basket_partial", "product_price"]
