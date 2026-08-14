# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

# Intentionally exports nothing. Importing any submodule runs this file first,
# so re-exporting the managers here would pull `lr_scheduler` and `optimizer`
# into every importer of `checkpointer.utils` and close a cycle:
# optimizer -> checkpointer.utils -> dcp -> lr_scheduler -> optimizer.
# Import from the submodule that owns the name.
