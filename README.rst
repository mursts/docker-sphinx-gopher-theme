==============================
docker-sphinx-gopher-theme
==============================


Sphinxでスライド作る用のコンテナで、テーマは `sphinxjp.themes.gopher <https://github.com/tell-k/sphinxjp.themes.gopher>`_ を使用

使い方
==============================

create docker image

.. code-block:: sh

   $ docker build -t mursts/sphinx-gopher-theme .

sphinx-quickstart

.. code-block:: sh

   $ docker run -it --rm -v $PWD:/doc mursts/sphinx-gopher-theme sphinx-quickstart

edit conf.py

.. code-block:: python

   html_theme = "gopher"
   extensions.append('sphinxjp.themes.gopher')
   html_theme_options = {'note_enabled': True}

build

.. code-block:: sh

   $ docker run -it --rm -v $PWD:/doc -p 8000:8000 mursts/sphinx-gopher-theme make html

