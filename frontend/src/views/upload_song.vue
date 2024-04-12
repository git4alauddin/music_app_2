<template>
  <router-view></router-view>

  <div id="m">
    <div class="container">
      <div class="jumbotron text-center">
        <h1>Upload Song</h1>
        <h5>Enter song details</h5>
        <form @submit.prevent="uploadSong1" novalidate>
          <div class="form-group">
            <label for="title">Title:</label>
            <input type="text" class="form-control" id="title" v-model="song.title" required>
          </div>

          <div class="form-group">
            <label for="artist">Artist:</label>
            <input type="text" class="form-control" id="artist" v-model="song.artist" required>
          </div>

          <div class="form-group">
            <label for="genre">Genre:</label>
            <input type="text" class="form-control" id="genre" v-model="song.genre" required>
          </div>

          <div class="form-group">
            <label for="lyrics">Lyrics:</label>
            <textarea class="form-control" id="lyrics" v-model="song.lyrics" required></textarea>
          </div>
          <button type="submit" class="btn btn-primary">Upload</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue';
// import useFormValidation from '../modules/useFormValidation';
// import useSubmitButtonState from '../modules/useSubmitButtonState';
// import customfetch from '../modules/customfetch';
import router from '../router/index';
import axios from 'axios';

const song = reactive({
  title: '',
  artist: '',
  genre: '',
  lyrics: ''
})

function uploadSong() {
  console.log(localStorage.getItem('token'))
  customfetch('http://127.0.0.1:5000/songs/upload_song', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'Authorization': localStorage.getItem('token')        
      },
      body: JSON.stringify({title: song.title, artist: song.artist, genre: song.genre, lyrics: song.lyrics})
  })
  .then((response) => {
      if (response.ok) {
          console.log('Song uploaded successfully')
          alert('Song uploaded successfully')
          router.push({name: 'user_dash'})
      } else {
          throw new Error('Failed to upload song')
      }
  })
  .catch((error) => {
      console.error('Error uploading song:', error)
      alert(error.message || 'An error occurred while uploading the song')
  })
};

function  uploadSong1() {
            axios
                .post
                (`http://localhost:5000/songs/upload_song`, 
                  {
                    title: song.title, artist: song.artist, genre: song.genre, lyrics: song.lyrics
                  }, 
                  {
                    headers: {Authorization: localStorage.getItem('token')},
                  }
                )
                .then(response => {
                  console.log('Song uploaded successfully')
                  // Clear the form fields after successful show creation
                  song.title = '';
                  song.artist = '';
                  song.genre = '';
                  song.lyrics = '';
                  alert('Song uploaded successfully')
                  router.push({name: 'user_dash'})
                })
                .catch(error => {
                    this.message = 'An error occurred while creating the show';
                });
        };

</script>

<style>
.jumbotron {
  font-family: cursive;
}
.container {
  display: flex;
  justify-content: center;
  padding-top: 100px;
}

#m {
  background-image: url('@/assets/BGimg3.jpg');
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: 100% 100%;
}
</style>
