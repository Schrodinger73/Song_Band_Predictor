import os
import shutil
import subprocess
from pytube import Playlist, YouTube


def remove_items(test_list, item):
    res = [i for i in test_list if i != item]
    return str(res)

def run(pl):
    # insert the downloads destination (optional)
    # e.g. C:\Users\Username\Folder
    filepath = "filename"
    # get linked list of links in the playlist
    links = pl.video_urls

    # download each item in the list
    for l in links:
        os.system("cls")

        # converts the link to a YouTube object
        yt = YouTube(l)

        # takes first stream; since ffmpeg will convert to mp3 anyway
        # changes: added filter with file extension of mp4
        music = yt.streams.filter(file_extension="mp4").first()

        # gets the filename of the first video stream
        default_filename = music.default_filename
        print(default_filename)
        print("Downloading " + default_filename + "...")

        # downloads first video stream and rename the first video stream
        try:
            music.download()
            special = [" ", "(", ")", "'", "/", ",", "+"]
            default_filename_remove_spaces = default_filename.replace(" ", "")
            for x in special:
                default_filename_remove_spaces = default_filename_remove_spaces.replace(x, "")
 #       if default_filename_remove_spaces.__contains__("("):
 #           default_filename_remove_spaces = default_filename_remove_spaces[:default_filename_remove_spaces.index("(")] + default_filename_remove_spaces[default_filename_remove_spaces.index(")") + 1:]
        except:
            pass

        try:
            # if its already renamed then pass
            os.rename(default_filename, default_filename_remove_spaces)
        except:
            pass

        # replaces mp4 with mp3 for ffmeg output
        try:
            new_filename = default_filename.replace("mp4", "wav")
            new_filename_remove_spaces = new_filename.replace(" ", "")
            for x in special:
                new_filename_remove_spaces = new_filename_remove_spaces.replace(x, "")
 #       if new_filename_remove_spaces.__contains__("("):
 #           new_filename_remove_spaces = new_filename_remove_spaces[:new_filename_remove_spaces.index("(")] + new_filename_remove_spaces[new_filename_remove_spaces.index(")") + 1:]
            print(default_filename_remove_spaces)
            print(new_filename_remove_spaces)
            print("Converting to wav....")
        except:
            pass

        # converts mp4 video to mp3 audio and moving the audio to folder input
        # NOTE: MUST HAVE "ffmpeg.exe" DOWNLOADED AND PLACED INSIDE THE DIRECTORY
        try:
            subprocess.call(f"ffmpeg -i {default_filename_remove_spaces} {new_filename_remove_spaces}", shell=True)
        except:
            pass
        # if exception then create download folder if not exists and store the downloaded audios
        try:
            # if filepath is empty then create download if not exists and store the downloaded audios
            if filepath == "":
                shutil.move(new_filename_remove_spaces,
                            os.path.join(os.path.abspath("./Downloads"), new_filename_remove_spaces))
            else:
                shutil.move(new_filename_remove_spaces,
                            os.path.join(os.path.abspath(filepath), new_filename_remove_spaces))

        except:
            try:
                if os.path.exists("./Downloads"):
                    shutil.move(new_filename_remove_spaces,
                        os.path.join(os.path.abspath("./Downloads"), new_filename_remove_spaces))
                else:
                    os.makedirs("./Downloads")
                    shutil.move(new_filename_remove_spaces,
                            os.path.join(os.path.abspath("./Downloads"), new_filename_remove_spaces))
            except:
                pass
        try:
            os.remove(default_filename_remove_spaces)
        except:
            pass

        # Old Code
        """
        subprocess.run(['ffmpeg', '-i', 
            os.path.join(filepath, default_filename),
            os.path.join(filepath, new_filename)
        ])
        """

    print("Download finished.")


if __name__ == "__main__":
#    url = input("Please enter the url of the playlist you wish to download: ")
# Linda
 #   pl = Playlist("https://www.youtube.com/playlist?list=PLO8bKIwG5EA2lKlsCn2aoKyQSMOF9rm7e")
# Beatles
    pl = Playlist("playlist link")
    run(pl)
