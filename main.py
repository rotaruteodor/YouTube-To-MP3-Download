from pytube import YouTube, Playlist
from pytube.exceptions import VideoUnavailable
import os
import datetime


def downloadYoutubePlaylistAsMP3Files(playlist_link, download_destination="."):
    playlist = Playlist(playlist_link)
    for video_link in playlist.video_urls:
        downloadYoutubeVideoAsMP3(video_link, download_destination)

    print("\n\n")
    for i in range(5):
        print("✔✔✔✔✔✔✔✔ DONE ✔✔✔✔✔✔✔✔")


def downloadYoutubeVideoAsMP3(video_link, download_destination="."):
    try:
        yt = YouTube(video_link)
    except VideoUnavailable:
        print("❌ SKIPPED BECAUSE VIDEO IS NOT AVAILABLE")
    else:
        if (yt.title == "Video Not Available"):
            print("❌ SKIPPED BECAUSE VIDEO IS NOT AVAILABLE")
        else:
            video = yt.streams.filter(only_audio=True).first()
            try:
                video_as_mp4_file = video.download(output_path=download_destination)
            except:
                print("❌ ERROR! ⚪ " + yt.title + " ⚪")
            else:
                filename, extension = os.path.splitext(video_as_mp4_file)
                video_as_mp3_file = filename + '.mp3'
                os.rename(video_as_mp4_file, video_as_mp3_file)
                print("✔ SUCCESS! ⚪ " + yt.title + " ⚪")


# video_link = ""
# downloadYoutubeVideoAsMP3(video_link)

playlist_link = ""
download_destination = "D:\Music"
downloadYoutubePlaylistAsMP3Files(playlist_link, os.path.join(download_destination,
                                                              datetime.datetime.now().strftime('%d-%m-%Y %H.%M')))
