# Docker - Cat Gif of the Day

Docker image just to play around.

Runs a Flask app that displays a cute cat gif provided by Giphy, on top of Alpine listening in port 5000.


## Usage
    docker run -p 8888:5000 --name cat-gif goncalommarques/cat-gif-of-the-day
## View

Going to http://localhost:8888 you should see something similar to:

![Cat of the day](sample.png)

## References

This has been an adapted version of the Docker sample from [Docker Labs](https://github.com/docker/labs/blob/master/beginner/chapters/webapps.md#231-create-a-python-flask-app-that-displays-random-cat-pix). 
Changes include:
- Use Alpine 3.12.1
- Update to Python 3.x
- Update to Flask 1.1.2
- Clean up index.html a bit
- Change gif from BuzFeed (no longer available) to selected funny cat Giphys
