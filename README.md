# LM Connection Speed

Python script that displays Down/Upload-Speed using speedtest-cli on your LaMetric Time.

#####Instructions:

You need to create an indicatior app for your LaMetric time [in the developer area](https://developer.lametric.com). It needs to be a private push app with two text frames. After publishing it, copy the access token and the local push url. Install the app on your device using the LaMetric smartphone app.

Insert access token and local push url into the connection_speed.py (look for `"ENDPOINT_URL"` and `"YOUR ACCESS TOKEN"`).

After that make the file executable (`chmod +x connection_speed.py`) and you shoukd be able to start it with
```
./connection_speed.py
```
you can also use
```
python3 connection_speed.py
```

#####Remarks
- The script takes a few seconds to finish
- The results may vary a lot (e.g. sometimes it showed only 5 Mbit/s for downloads, although I know it was 90 Mbit/s at this point) - so don't take those values too serious 
- This script should run with Python 2 and 3 but I only use Python 3, so I won't guarantee anything

#####Dependencies:
You need the following Python packages:

- requests
- json
- speedtest-cli
