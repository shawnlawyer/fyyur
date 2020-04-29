FROM fedora:28
WORKDIR /var/www/html
EXPOSE 80

RUN dnf -y update && dnf clean all

RUN dnf install -y \
    nginx \
    screen \
    unzip \
    wget \
    nodejs \
    && dnf clean all \
    && npm update -g \
    && npm install -g n \
    && npm cache clean -f \
    && n stable

COPY . /var/www/html
COPY ./docker/nginx.conf /etc/nginx/

RUN pip3 install -r requirements.txt
RUN ln -sf /dev/stdout /var/www/html/access.log && ln -sf /dev/stderr /var/www/html/error.log
RUN echo "screen -r" > /root/.bash_history

ENTRYPOINT ["/var/www/html/start.sh"]

