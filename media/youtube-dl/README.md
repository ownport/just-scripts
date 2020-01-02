# youtube-dl wrapper

## How to use

### Video

Download single video
```sh
my-youtube-dl video <url to video>
```

To Download multiple videos from url file, the file with the name `url` must be present in current directory and contains the list of urls to videos
```sh
my-youtube-dl video
```

To avoid re-downloading the video, the file .archive is created and contains the list of downloaded videos

### Audio

Download single audio
```sh
my-youtube-dl audio <url to audio>
```

To download multiple audios from url file, the file with the name `url` must be present in current directory and contains the list of urls to audios
```sh
my-youtube-dl audio
```

To avoid re-downloading the audio, the file .archive is created and contains the list of downloaded audios



