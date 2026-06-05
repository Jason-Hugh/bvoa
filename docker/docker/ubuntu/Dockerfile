FROM ubuntu:latest
ARG USER
ARG GROUP
ARG PASSWD
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC
ENV PATH="$PATH:/sbin:/usr/sbin:usr/local/sbin"

RUN userdel -rf ubuntu
RUN groupadd --gid 1000 ${GROUP}
RUN useradd --home-dir /home/${USER} --create-home --shell /bin/bash --uid 1000 --gid 1000 --password "${PASSWD}" ${USER}

RUN apt-get update
RUN apt-get -y install sudo
# RUN adduser ${USER} sudo
# RUN echo "${USER} ALL=(ALL:ALL) NOPASSWD: ALL" | sudo tee "/etc/sudoers.d/dont-prompt-$USER-for-sudo-password"

COPY dotfiles/* /home/${USER}/
RUN chown -R ${USER}:${GROUP} /home/${USER}

COPY install.sh /opt/install.sh
RUN /bin/bash -c /opt/install.sh
COPY install-as-user.sh /opt/install-as-user.sh
RUN sudo -u ${USER} /bin/bash -c /opt/install-as-user.sh

USER ${USER}

WORKDIR /home/${USER}
