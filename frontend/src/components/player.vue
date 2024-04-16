<template>
    
    <!---------------------- player------------- -->
    <div class="player">
        <div class="song_info">
            <h3>playing khamoshiya by arjit...</h3>
        </div>

        <audio controls>
            <source src = "../static/songs/arijit_aaaaaaaaaaaaaabb_5735.mp3">
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
..player {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: fixed;
  bottom: 0;
  width: 100%;
  background-color: #f4f4f4; /* Optional: Add background color */
  padding: 10px 0; /* Optional: Add padding */
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