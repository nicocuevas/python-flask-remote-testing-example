FROM node:10.15.1-alpine
RUN deluser --remove-home node

RUN apk --no-cache add --virtual  \
  .gyp g++ gcc libgcc libstdc++ linux-headers make python && \
  apk add git && \
  npm install --quiet node-gyp -g

ENV JAVA_HOME=/usr/lib/jvm/default-jvm

RUN apk add --no-cache openjdk8 && \
    ln -sf "${JAVA_HOME}/bin/"* "/usr/bin/"


ENV ANDROID_HOME /opt/android-sdk-linux
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-tools

RUN apk update && apk add --no-cache bash unzip libstdc++

RUN mkdir ~/.android
RUN touch ~/.android/repositories.cfg

RUN mkdir -p /opt/android-sdk-linux && cd /opt \
    && wget -q https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip -O android-sdk-tools.zip \
    && unzip -q android-sdk-tools.zip -d ${ANDROID_HOME} \
    && rm -f android-sdk-tools.zip \
    && echo y | sdkmanager "build-tools;28.0.3" "platform-tools" "platforms;android-26" "platforms;android-23"


RUN npm config set user 0
RUN npm config set unsafe-perm true
RUN npm install --quiet appium appium-uiautomator2-driver -g

