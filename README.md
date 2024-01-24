# ABOUT

This project is a test implementation of extracting unique faces detected on YouTube videos with a given URL. I have not implemented CLI tools or video ID extraction. It is a plain coded URL that you must change or extend functionality to deliver new video URLs or process batch videos.

The core of this project is built on top of the `face_recognition` and `rembg` Python libraries, which are doing pretty much all of the work; I just made a composable reading from a given video file using Python OpenCV.

## Running Locally

This project doesn’t have external service dependencies, and everything is inside an `[experiment.py](http://experiment.py)` file, where it will handle the video download using the `pytube` library and write extracted frames inside the same directory.

```bash
pip install -r requirements.txt

python experiment.py
```

## What’s Next Here?

This project doesn’t have that much in it, because it was very small functionality that I am building for one of my products within `[treescale.com](http://treescale.com)` as a Face detection API Endpoint.