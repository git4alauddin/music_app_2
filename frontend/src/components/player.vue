<template>
    
    <!---------------------- player------------- -->
    <div class="player">
        <div class="song_info">
            <h3>playing khamoshiya by arjit...</h3>
        </div>

        <audio controls>
            <!-- <source src = "music_app_2\backend\static\songs\arijit_aaaaaaaaaaaaaabb_5735.mp3"> -->
            <source src = "#">
        </audio>

        
      </div>
      <!---------------------- player------------- -->
</template>

<script>
export default {
    name: 'player',
}
</script>

<style scoped>
.player {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

audio {
    width: 90%;
}

.song_info {
  margin-top: 20px;
  text-align: center;
}

.song_info h3 {
  font-size: 18px;
  color: #333;
}

</style>