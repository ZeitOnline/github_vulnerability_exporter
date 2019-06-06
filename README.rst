==============================================
Prometheus GitHub vulnerability alert exporter
==============================================

This package exports the `Security Vulnerability Alerts`_ collected by GitHub as `Prometheus`_ metrics.

.. _`Security Vulnerability Alerts`: https://help.github.com/en/categories/managing-security-vulnerabilities
.. _`Prometheus`: https://prometheus.io


Usage
=====

Configure API token
-------------------

You'll need to provide an access token to access the GitHub API.
See the `GitHub documentation` for details.

.. `GitHub documentation`: https://developer.github.com/v4/guides/forming-calls/#authenticating-with-graphql


Start HTTP service
------------------

Start the HTTP server like this::

    $ uptimerobot_exporter --port=9597 --organization=MyGitHubOrg --authtoken=ACCESSTOKEN


Configure Prometheus
--------------------

::

    scrape_configs:
      - job_name: 'vulnerabilities'
        scrape_interval: 600s
        static_configs:
          - targets: ['localhost:9597']

We export one metric, a gauge called ``github_vulnerability_alerts``,
with a label ``{repository="MyGitHubOrg/my-repository-name}``.

Additionally, a ``ghvuln_scrape_duration_seconds`` gauge is exported.
