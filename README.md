#System Admin CMD

# How to use youtube-dl
# https://www.youtube.com/watch?v=-AlsjIbu7Sc&ab_channel=ConstructionCoach
youtube-dl <youtube url>
# Download the url video and audio and join them
# similarly download the playlist
youtube-dl -F url # get all the formats of youtube video
youtube-dl -f 136 url

youtube-dl -x url #download entire video & audio then delete video
youtube-dl -f bestaudio url
