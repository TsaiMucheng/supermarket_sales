Create environment named flask_sales
```bash
conda create -n flask_sales python=3.10.10 \
	numpy=1.23.5 flask=2.2.2 plotly=5.9.0 \
	seaborn=0.12.2 scikit-learn=1.2.2 scipy=1.10.1
```

Build image called marketsales
```bash
docker build -t marketsales:0.0.0 \
	--build-arg APP_PATH=/home/flask_sales/ \
	--build-arg CONDA_ENV=flask_sales . --no-cache
```

Run container in Window/Linux
```bash
docker run -ti -p 8083:8080 -v %cd%:/home/flask_sales/ --name marketsales_container marketsales:0.0.0 bash
```
```bash
docker run -ti -p 8083:8080 -v $(pwd):/home/flask_sales/ --name marketsales_container marketsales:0.0.0 bash
```

Run flask api in container
```bash
conda activate flask_sales && flask run --host 0.0.0.0 --port 5000
```
 - View 127.0.0.1:5000