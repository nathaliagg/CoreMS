FROM corilo/corems:base-mono-pythonnet AS base
WORKDIR /home/CoreMS

COPY corems/ /home/CoreMS/corems
COPY doc/notebooks/*.ipynb README.md disclaimer.txt requirements.txt SettingsCoreMS.json setup.py /home/CoreMS/
COPY doc/examples /home/CoreMS/
COPY ESI_NEG_SRFA.d/ /home/CoreMS/ESI_NEG_SRFA.d/

#RUN apt update && apt install -y --no-install-recommends  build-essential

FROM base AS build  
COPY --from=base /home/CoreMS /home/CoreMS
WORKDIR /home/CoreMS

RUN python3 setup.py install
RUN python3 -m pip install jupyter
CMD jupyter notebook --ip 0.0.0.0 --no-browser --allow-root

