<template>
  
    <!-- Songs in the album -->
    <div>
      <h2>{{ $route.params.title }}</h2>
      <!-- Display songs of the album -->
      <div>
        <h3>Album Songs</h3>
        <ul>
          <li v-for="song in albumSongs" :key="song.id">
            <div class="song-details">
              <h3>{{ song.title }} [{{ song.genre }}]</h3>
              <button @click="removeFromAlbum(song.id)">Delete</button>
            </div>
          </li>
        </ul>
        <hr>
      </div>
    </div>
  
    <!-- Suggested Songs -->
    <div class="suggested-songs">
      <h2>Suggested Songs</h2>
      <ul>
        <li v-for="song in suggestedSongs" :key="song.id">
          <div class="song-details">
            <h3>{{ song.title }} [{{ song.average_rating }}] </h3>
            <p><strong>Artist:</strong> {{ song.artist }}</p>
            <p><strong>Genre:</strong> {{ song.genre }}</p>
            <p><strong>Lyrics:</strong> {{ song.lyrics }}</p>
            <div class="rating">
              <input type="radio" v-model="song.rating" value="1"> 1
              <input type="radio" v-model="song.rating" value="2"> 2
              <input type="radio" v-model="song.rating" value="3"> 3
              <input type="radio" v-model="song.rating" value="4"> 4
              <input type="radio" v-model="song.rating" value="5"> 5
            </div>
            <button @click="rateSong(song.id, parseInt(song.rating))">Rate</button>
            <button @click="addToAlbum(song.id)">Add to Album</button>
          </div>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        suggestedSongs: [],
      };
    },
    
    created() {
      this.fetchAlbumSongs();
      this.fetchSuggestedSongs();
    },
  
    mounted() {
      this.user_id = localStorage.getItem('id');
      this.role = localStorage.getItem('role');
    },
  
    methods: {
      async fetchSuggestedSongs() {
        try {
          const response = await axios.get('http://localhost:5000/songs/songs', {
            headers: { Authorization: localStorage.getItem('token') }, 
          });
          this.suggestedSongs = response.data;
          console.log('Songs:', this.suggestedSongs);
        } catch (error) {
          console.error('Error fetching songs:', error);
        }
      },
  
      async addToAlbum(songId) {
        try {
          const response = await axios.post(`http://localhost:5000/albums/albums/${this.$route.params.id}/songs/${songId}`, {}, {
            headers: { Authorization: localStorage.getItem('token') }, 
          });
          console.log('Song added to album:', response.data);
          window.location.reload();
        } catch (error) {
          console.error('Error adding song to album:', error);
        }
      },
  
      async fetchAlbumSongs() {
        try {
          const response = await axios.get(`http://localhost:5000/albums/albums/${this.$route.params.id}/songs`, {
            headers: { Authorization: localStorage.getItem('token') }, 
          });
          this.albumSongs = response.data;
          console.log('Album songs:', this.albumSongs);
        } catch (error) {
          console.error('Error fetching album songs:', error);
        }
      },
  
      async removeFromAlbum(songId) {
        try {
          const response = await axios.delete(`http://localhost:5000/albums/albums/${this.$route.params.id}/songs/${songId}`, {
            headers: { Authorization: localStorage.getItem('token') }, 
          });
          console.log('Song removed from album:', response.data);
          window.location.reload();
        } catch (error) {
          console.error('Error removing song from album:', error);
        } 
      },
    }     
  };
  </script>
  
  <style scoped>
  </style>
  