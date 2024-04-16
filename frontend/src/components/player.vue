<template>
    <!-- <h1>player</h1> -->
    <!--
    <div class="player">
        <audio controls autoplay>
            <source src = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3">
        </audio>

        <div class="song_info">
            <h3>artist</h3>
        </div>
        
      </div>
    -->
</template>

<script>
export default {
  name: 'player',
  props: {
    song: Object
  }
}
</script>

<style scoped>
.player {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: #efebeb;
  color: white;
  padding: 20px;
  box-sizing: border-box;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.player .song_info,
.player .audio_player .player,
.player .add_to_playlist {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}
.player h2 {
  margin: 0;
}
.player audio {
    width: 100%;
}
.player .add_to_playlist a {
  padding: 8px 16px;
  background-color: #4CAF50;
  color: white;
  border: none;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 5px;
}
.player .add_to_playlist a:hover {
  background-color: #45a049;
}

/* # give padding from top so that it will not overlap the contents at bottom */
.player .audio_player {
  z-index: -1;
}
/* its not working */

</style>
