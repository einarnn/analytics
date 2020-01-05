# initial analytics prototyping

## introduction

Several Jupyter notebooks that try out some analytics approaches for time series predictions:

- [arima.ipynb](arima.ipynb) - Experimentation with ARIMA
- [arima-lr-comparison.ipynb](arima-lr-comparison.ipynb) - Comparing ARIMA directly with single coefficient linear regression
- [tf-time-series.ipynb](tf-time-series.ipynb) - Time series predictions using TensorFlow RNNs

Then you can select one of the notebooks from the browser window that pops up. Of course, you can also run the notebook server on a remote server.

These notebooks are "scratchpads" used for some initial experimentation:

- [airline.ipynb](airline.ipynb)
- [linear-regression-play.ipynb](linear-regression-play.ipynb)

## setup and running jupyter-notebook

To start playing with examples, first create a Python virtualenv (example uses `virtualenvwrapper`):

```
$ mkvirtualenv analytics
Using base prefix '/usr/local/Cellar/python/3.7.5/Frameworks/Python.framework/Versions/3.7'
New python executable in /Users/einarnn/.virtualenvs/analytics/bin/python3.7
Also creating executable in /Users/einarnn/.virtualenvs/analytics/bin/python
Installing setuptools, pip, wheel...
done.
virtualenvwrapper.user_scripts creating /Users/einarnn/.virtualenvs/analytics/bin/predeactivate
virtualenvwrapper.user_scripts creating /Users/einarnn/.virtualenvs/analytics/bin/postdeactivate
virtualenvwrapper.user_scripts creating /Users/einarnn/.virtualenvs/analytics/bin/preactivate
virtualenvwrapper.user_scripts creating /Users/einarnn/.virtualenvs/analytics/bin/postactivate
virtualenvwrapper.user_scripts creating /Users/einarnn/.virtualenvs/analytics/bin/get_env_details
(analytics) $ pip install -r requirements.txt
Collecting influxdb==5.2.3
  ...
  ...elided...
  ...
Installing collected packages: [...elided...]
Successfully installed [...elided...]
(analytics) $
```

Then you can start the Jupyter Notebook server:

```
(analytics) $ jupyter-notebook
[I 11:55:32.412 NotebookApp] Serving notebooks from local directory: /opt/git-repos/AI3106/analytics
[I 11:55:32.412 NotebookApp] The Jupyter Notebook is running at:
[I 11:55:32.412 NotebookApp] http://localhost:8888/
[I 11:55:32.412 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[W 11:55:34.171 NotebookApp] Clearing invalid/expired login cookie username-localhost-8888
[W 11:55:34.172 NotebookApp] Clearing invalid/expired login cookie username-localhost-8888
[I 11:55:34.173 NotebookApp] 302 GET /tree (::1) 4.01ms
```
