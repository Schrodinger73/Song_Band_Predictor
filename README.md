# Song_Band_Predictor

Credit to https://github.com/modkhi/yt-playlist/tree/master?tab=readme-ov-file for the code to convert YouTube Playlist to wav files.

Due to size problems, I could not upload the songs on GitHub, but I took the songs from the catalogues of - The Beatles, ABBA, Queen, Nirvana, Led Zeppelin, Beach Boys, Bob Dylan, Elvis Presley, Pink Floyd.

The model I created trained on those songs, which I converted to a numpy array using Librosa. The model worked with a 70% accuracy on the validation set(test set). The main goal of the model is to try it on songs which are not by these bands, so I tried songs by Lana Del Rey, Olivia Rodrigo, Linda Ronstadt, Arctic Monkeys, Dua Lipa, and so on...

The output was given by the Softmax function, which gives the output in terms of probabilities, which I used to convert to percentages, for each band. I used 2 songs of the initially mentioned bands, for trial of the model. All the  model needs to work is the link of the wav file, and voila!
