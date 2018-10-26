==============================
docker-sphinx-gopher-theme
==============================


Sphinxでスライド作る用のコンテナで、テーマは `sphinxjp.themes.gopher <https://github.com/tell-k/sphinxjp.themes.gopher>`_ を使用

使い方
==============================

build

.. code-block:: sh

   $ docker build -t mursts/docker-sphinx-gopher-theme .

sphinx-quickstart

.. code-block:: sh

   $ docker run -it --rm -v /path/to/dir:/documets mursts/docker-sphinx-gopher-theme sphinx-quickstart

build

.. code-block:: sh

   $ docker run -it --rm -v /path/to/dir:/documets -p 8000:8000 mursts/docker-sphinx-gopher-theme make html

   or

   $ docker run -it --rm -v /path/to/dir:/documets -p 8000:8000 mursts/docker-sphinx-gopher-theme make livehtml


