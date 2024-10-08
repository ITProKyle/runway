.. _k8s-configuration:

#############
Configuration
#############

Configuration options and parameters for :ref:`index:Kubernetes` :term:`Modules <module>`.



*******
Options
*******

.. data:: kubectl_version
  :type: str | None
  :value: None
  :noindex:

  Specify a version of Kubectl for Runway and download and use.
  See :ref:`Version Management <k8s-version>` for more details.

  .. rubric:: Example
  .. code-block:: yaml

    options:
      kubectl_version: 1.14.5

.. data:: overlay_path
  :type: str | None
  :value: None
  :noindex:

  Specify the directory containing the kustomize overlay to use.

  .. rubric:: Example
  .. code-block:: yaml

    options:
      overlay_path: overlays/${env DEPLOY_ENVIRONMENT}-blue

  .. versionadded:: 1.12.0


**********
Parameters
**********

:ref:`index:Kubernetes` does not support the use of :attr:`deployment.parameters`/:attr:`module.parameters` at this time.
