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
❯ mkvirtualenv --python=`which python3.10` analytics
created virtual environment CPython3.10.15.final.0-64 in 306ms
  creator CPython3macOsBrew(dest=/Users/einarnn/.virtualenvs/analytic, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/einarnn/Library/Application Support/virtualenv)
    added seed packages: pip==24.2, setuptools==70.2.0, wheel==0.44.0
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
virtualenvwrapper.user_scripts creating /Users/einarnn/.virtualenvs/analytic/bin/predeactivate
virtualenvwrapper.user_scripts creating /Users/einarnn/.virtualenvs/analytic/bin/postdeactivate
virtualenvwrapper.user_scripts creating /Users/einarnn/.virtualenvs/analytic/bin/preactivate
virtualenvwrapper.user_scripts creating /Users/einarnn/.virtualenvs/analytic/bin/postactivate
virtualenvwrapper.user_scripts creating /Users/einarnn/.virtualenvs/analytic/bin/get_env_details
❯ pip install -r requirements.txt
Collecting influxdb (from -r requirements.txt (line 1))
  ...
  ...elided...
  ...
Installing collected packages: [...elided...]
Successfully installed [...elided...]
❯ 
```

Then you can start the Jupyter Notebook server:

```
❯ jupyter-notebook
[I 2024-11-13 11:40:16.306 ServerApp] jupyter_lsp | extension was successfully linked.
[I 2024-11-13 11:40:16.309 ServerApp] jupyter_server_terminals | extension was successfully linked.
[I 2024-11-13 11:40:16.311 ServerApp] jupyterlab | extension was successfully linked.
[I 2024-11-13 11:40:16.313 ServerApp] notebook | extension was successfully linked.
[I 2024-11-13 11:40:16.573 ServerApp] notebook_shim | extension was successfully linked.
[I 2024-11-13 11:40:16.603 ServerApp] notebook_shim | extension was successfully loaded.
[I 2024-11-13 11:40:16.605 ServerApp] jupyter_lsp | extension was successfully loaded.
[I 2024-11-13 11:40:16.606 ServerApp] jupyter_server_terminals | extension was successfully loaded.
[I 2024-11-13 11:40:16.609 LabApp] JupyterLab extension loaded from /Users/einarnn/.virtualenvs/analytics/lib/python3.10/site-packages/jupyterlab
[I 2024-11-13 11:40:16.610 LabApp] JupyterLab application directory is /Users/einarnn/.virtualenvs/analytics/share/jupyter/lab
[I 2024-11-13 11:40:16.610 LabApp] Extension Manager is 'pypi'.
[I 2024-11-13 11:40:16.620 ServerApp] jupyterlab | extension was successfully loaded.
[I 2024-11-13 11:40:16.622 ServerApp] notebook | extension was successfully loaded.
[I 2024-11-13 11:40:16.623 ServerApp] Serving notebooks from local directory: /opt/git-repos/analytics
[I 2024-11-13 11:40:16.623 ServerApp] Jupyter Server 2.14.2 is running at:
[I 2024-11-13 11:40:16.623 ServerApp] http://localhost:8888/tree?token=3d57e4ab1fe9dac3328aabfa3d439787a01392e66cc87fc4
[I 2024-11-13 11:40:16.623 ServerApp]     http://127.0.0.1:8888/tree?token=3d57e4ab1fe9dac3328aabfa3d439787a01392e66cc87fc4
[I 2024-11-13 11:40:16.623 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
```
