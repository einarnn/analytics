# initial analytics prototyping

Several Jupyter notebooks that try out some analytics approaches for time series predictions:

- ARIMA
- Simple Linear Regressiuon
- TensorFlow RNN

To start playing with examples, first create a Python virtualenv (I use `virtualenvwrapper`):

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
Installing collected packages: six, python-dateutil, certifi, chardet, urllib3, idna, requests,
pytz, influxdb, pyzmq, ipython-genutils, decorator, traitlets, jupyter-core, tornado, jupyter-client,
appnope, backcall, wcwidth, prompt-toolkit, parso, jedi, ptyprocess, pexpect, pickleshare, pygments,
ipython, ipykernel, qtconsole, jupyter-console, Send2Trash, attrs, pyrsistent, more-itertools, zipp,
importlib-metadata, jsonschema, nbformat, terminado, prometheus-client, MarkupSafe, jinja2,
entrypoints, defusedxml, pandocfilters, testpath, webencodings, bleach, mistune, nbconvert,
notebook, widgetsnbextension, ipywidgets, jupyter, pyparsing, cycler, kiwisolver, numpy, matplotlib,
pandas, joblib, scipy, scikit-learn, sklearn, opt-einsum, absl-py, astor, tensorflow-estimator,
termcolor, protobuf, gast, google-pasta, keras-preprocessing, grpcio, h5py, keras-applications,
cachetools, pyasn1, pyasn1-modules, rsa, google-auth, werkzeug, markdown, oauthlib,
requests-oauthlib, google-auth-oauthlib, tensorboard, wrapt, tensorflow, tqdm
Successfully installed MarkupSafe-1.1.1 Send2Trash-1.5.0 absl-py-0.9.0 appnope-0.1.0 astor-0.8.1 
attrs-19.3.0 backcall-0.1.0 bleach-3.1.0 cachetools-4.0.0 certifi-2019.11.28 chardet-3.0.4 
cycler-0.10.0 decorator-4.4.1 defusedxml-0.6.0 entrypoints-0.3 gast-0.2.2 google-auth-1.10.0 
google-auth-oauthlib-0.4.1 google-pasta-0.1.8 grpcio-1.26.0 h5py-2.10.0 idna-2.8 
importlib-metadata-1.3.0 influxdb-5.2.3 ipykernel-5.1.3 ipython-7.11.1 ipython-genutils-0.2.0 
ipywidgets-7.5.1 jedi-0.15.2 jinja2-2.10.3 joblib-0.14.1 jsonschema-3.2.0 jupyter-1.0.0 
jupyter-client-5.3.4 jupyter-console-6.0.0 jupyter-core-4.6.1 keras-applications-1.0.8 
keras-preprocessing-1.1.0 kiwisolver-1.1.0 markdown-3.1.1 matplotlib-3.1.1 mistune-0.8.4
more-itertools-8.0.2 nbconvert-5.6.1 nbformat-4.4.0 notebook-6.0.2 numpy-1.17.4 oauthlib-3.1.0 
opt-einsum-3.1.0 pandas-0.25.3 pandocfilters-1.4.2 parso-0.5.2 pexpect-4.7.0 pickleshare-0.7.5 
prometheus-client-0.7.1 prompt-toolkit-2.0.10 protobuf-3.11.2 ptyprocess-0.6.0 pyasn1-0.4.8 
pyasn1-modules-0.2.7 pygments-2.5.2 pyparsing-2.4.6 pyrsistent-0.15.6 python-dateutil-2.8.1 
pytz-2019.3 pyzmq-18.1.1 qtconsole-4.6.0 requests-2.22.0 requests-oauthlib-1.3.0 rsa-4.0 
scikit-learn-0.22.1 scipy-1.4.1 six-1.13.0 sklearn-0.0 tensorboard-2.0.2 tensorflow-2.0.0 
tensorflow-estimator-2.0.1 termcolor-1.1.0 terminado-0.8.3 testpath-0.4.4 tornado-6.0.3 
tqdm-4.41.1 traitlets-4.3.3 urllib3-1.25.7 wcwidth-0.1.8 webencodings-0.5.1 werkzeug-0.16.0 
widgetsnbextension-3.5.1 wrapt-1.11.2 zipp-0.6.0
```

Then you can start the Jupyter Notebook:

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

Then you can select one of the notebooks from the browser window that pops up. Of course, you can also run the notebook server on a remote server.
