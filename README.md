# Tugas Day 4

# Run it directly from cloned git
<img width="464" alt="image" src="https://res.cloudinary.com/dvcrbperu/image/upload/v1714571597/Screenshot_2024-05-01_at_9.50.38_PM_scnuy1.png">

## Step 1: Clone git project
To pull using Github CLI
```bash
gh repo clone haetsugaya/onxpnet-tugas-day-4
```

## Step 2: Clone git project
Move to cloned dir and run it
```bash
cd /onxpnet-tugas-day-4
python -u main.py
```


# Using Docker 
<img width="464" alt="image" src="https://res.cloudinary.com/dvcrbperu/image/upload/v1714572097/Screenshot_2024-05-01_at_10.01.17_PM_cmmmva.png">

## Step 1: Pull the Docker Image
To pull the image from GHCR.io, use the docker pull command followed by the image name and tag.
```bash
docker pull ghcr.io/haetsugaya/kelas-onxp-python-group5-task4:latest
```

## Step 2: Run the Docker Image
After pulling the image, you can run it using the docker run command.

```bash
docker run -it ghcr.io/haetsugaya/kelas-onxp-python-group5-task4:latest
```

### Re-run the Docker Container after exit
To run the app again after exiting, use this command below:
```bash
docker start [CONTAINER ID or NAME] --attach
```
Change [CONTAINER ID or NAME] into the based on the container that created after 'docker run -it'

