# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
FactorizationMachineBinaryClassifier
"""

__all__ = ["FactorizationMachineBinaryClassifier"]


from sklearn.base import ClassifierMixin

from ..base_predictor import BasePredictor
from ..internal.core.decomposition.factorizationmachinebinaryclassifier \
    import FactorizationMachineBinaryClassifier as core
from ..internal.utils.utils import trace


class FactorizationMachineBinaryClassifier(
        core, BasePredictor, ClassifierMixin):
    """

    Train a field-aware factorization machine for binary classification.

    .. remarks::
        Field Aware Factorization Machines use, in addition to the input
        variables, factorized
        parameters to model the interaction between pairs of variables. The
        algorithm is
        particularly useful for high dimensional datasets which can be very
        sparse (e.g.
        click-prediction for advertising systems). An advantage of FFM over
        SVMs is that the
        training data does not need to be stored in memory, and the
        coefficients can be optimized
        directly.



        **Reference**

            `Field Aware Factorization Machines
            <https://www.csie.ntu.edu.tw/~r01922136/slides/ffm.pdf>`_,
            `Field-aware Factorization Machines for CTR Prediction
            <https://www.csie.ntu.edu.tw/~cjlin/papers/ffm.pdf>`_,
            `Adaptive Subgradient Methods for Online Learning and Stochastic
            Optimization
            <http://jmlr.org/papers/volume12/duchi11a/duchi11a.pdf>`_


    :param feature: see `Columns </nimbusml/concepts/columns>`_.

    :param label: see `Columns </nimbusml/concepts/columns>`_.

    :param weight: see `Columns </nimbusml/concepts/columns>`_.

    :param learning_rate: Determines the size of the step taken in the
        direction of the gradient in each step of the learning process.  This
        determines how fast or slow the learner converges on the optimal
        solution. If the step size is too big, you might overshoot the optimal
        solution.  If the step size is too small, training takes longer to
        converge to the best solution.

    :param number_of_iterations: Number of training iterations.

    :param latent_dimension: Latent space dimension.

    :param lambda_linear: Regularization coefficient of linear weights.

    :param lambda_latent: Regularization coefficient of latent weights.

    :param normalize: Whether to normalize the input vectors so that the
        concatenation of all fields' feature vectors is unit-length.

    :param caching: Whether trainer should cache input training data.

    :param extra_feature_columns: Extra columns to use for feature vectors. The
        i-th specified string denotes the column containing features form the
        (i+1)-th field. Note that the first field is specified by "feat"
        instead of "exfeat".

    :param shuffle: Whether to shuffle for each training iteration.

    :param verbose: Report traning progress or not.

    :param radius: Radius of initial latent factors.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:func:`LogisticRegressionClassifier
        <nimbusml.linear_model.LogisticRegressionClassifier>`,
        :py:func:`AveragedPerceptronBinaryClassifier
        <nimbusml.linear_model.AveragedPerceptronBinaryClassifier>`,
        :py:func:`GamBinaryClassifier <nimbusml.ensemble.GamBinaryClassifier>`,
        :py:func:`SgdBinaryClassifier
        <nimbusml.linear_model.SgdBinaryClassifier>`

    .. index:: models, stochastic, online, gradient, descent

    Example:
      .. literalinclude:: /../nimbusml/examples/FactorizationMachineBinaryClassifier.py
             :language: python
    """

    @trace
    def __init__(
            self,
            learning_rate=0.1,
            number_of_iterations=5,
            latent_dimension=20,
            lambda_linear=0.0001,
            lambda_latent=0.0001,
            normalize=True,
            caching='Auto',
            extra_feature_columns=None,
            shuffle=True,
            verbose=True,
            radius=0.5,
            feature=None,
            label=None,
            weight=None,
            **params):

        if 'feature_column_name' in params:
            raise NameError(
                "'feature_column_name' must be renamed to 'feature'")
        if feature:
            params['feature_column_name'] = feature
        if 'label_column_name' in params:
            raise NameError(
                "'label_column_name' must be renamed to 'label'")
        if label:
            params['label_column_name'] = label
        if 'example_weight_column_name' in params:
            raise NameError(
                "'example_weight_column_name' must be renamed to 'weight'")
        if weight:
            params['example_weight_column_name'] = weight
        BasePredictor.__init__(self, type='classifier', **params)
        core.__init__(
            self,
            learning_rate=learning_rate,
            number_of_iterations=number_of_iterations,
            latent_dimension=latent_dimension,
            lambda_linear=lambda_linear,
            lambda_latent=lambda_latent,
            normalize=normalize,
            caching=caching,
            extra_feature_columns=extra_feature_columns,
            shuffle=shuffle,
            verbose=verbose,
            radius=radius,
            **params)
        self.feature = feature
        self.label = label
        self.weight = weight

    @trace
    def predict_proba(self, X, **params):
        '''
        Returns probabilities
        '''
        return self._predict_proba(X, **params)

    @trace
    def decision_function(self, X, **params):
        '''
        Returns score values
        '''
        return self._decision_function(X, **params)

    def get_params(self, deep=False):
        """
        Get the parameters for this operator.
        """
        return core.get_params(self)
