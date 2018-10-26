FROM python:alpine3.7

# RUN apk add --update --no-cache \
#         #make \
#     && pip install \
#         sphinx \
#         sphinxjp.themes.gopher \
#         sphinx-autobuild

RUN  apk add --update --no-cache \
         make \
      && pip install \
         sphinx \
         sphinxjp.themes.gopher \
         sphinx-autobuild

RUN mkdir /work
COPY quickstart.py /work
COPY entrypoint.sh /work
RUN chmod 0755 /work/entrypoint.sh
ENTRYPOINT ["sh", "/work/entrypoint.sh"]

RUN mkdir /documents
WORKDIR /documents
VOLUME /documents

#CMD ["make", "html"]
