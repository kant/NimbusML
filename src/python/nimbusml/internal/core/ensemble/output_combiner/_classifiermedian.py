# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
ClassifierMedian
"""

__all__ = ["ClassifierMedian"]


from ....utils.entrypoints import Component
from ....utils.utils import trace, try_set


class ClassifierMedian(Component):
    """
    **Description**
        Computes the median of the outputs of the trained models

    :param normalize: Whether to normalize the output of base models before
        combining them.

    :param params: Additional arguments sent to compute engine.

    """

    @trace
    def __init__(
            self,
            normalize=True,
            **params):

        self.normalize = normalize
        self.kind = 'EnsembleMulticlassOutputCombiner'
        self.name = 'MultiMedian'
        self.settings = {}

        if normalize is not None:
            self.settings['Normalize'] = try_set(
                obj=normalize, none_acceptable=True, is_of_type=bool)

        super(
            ClassifierMedian,
            self).__init__(
            name=self.name,
            settings=self.settings,
            kind=self.kind)