==============================================
Prometheus GitHub vulnerability alert exporter
==============================================

This package exports the `Security Vulnerability Alerts`_ from GitHub for all repositories of an organization as `Prometheus`_ metrics.

.. _`Security Vulnerability Alerts`: https://help.github.com/en/categories/managing-security-vulnerabilities
.. _`Prometheus`: https://prometheus.io


Usage
=====

Configure API token
-------------------

You'll need to provide an access token with scope ``repo`` to access the GitHub API.
See the `GitHub documentation`_ for details.

.. _`GitHub documentation`: https://developer.github.com/v4/guides/forming-calls/#authenticating-with-graphql


Start HTTP service
------------------

Start the HTTP server like this::

    $ GITHUB_AUTHTOKEN=MYTOKEN GITHUB_OWNER=MyGitHubOrgOrUser github_vulnerability_exporter --host=127.0.0.1 --port=9597

Pass ``--ttl=SECONDS`` to cache GitHub API results for the given time or -1 to disable (default is 600).
Prometheus considers metrics stale after 300s, so that's the highest scrape_interval one should use.
However it's usually unnecessary to hit the API that often, since the vulnerability alert information does not change that rapidly.

Pass ``--forked`` if you want to include forked repositories (not sure if they actually receive vulnerability alerts, though).


Configure Prometheus
--------------------

::

    scrape_configs:
      - job_name: 'vulnerabilities'
        scrape_interval: 300s
        static_configs:
          - targets: ['localhost:9597']

We export one metric, a gauge called ``github_vulnerability_alerts``,
with labels ``{repository="MyGitHubOrgOrUser/my-repository-name, status="active|dismissed"}``.

Additionally, a ``ghvuln_scrape_duration_seconds`` gauge is exported.
