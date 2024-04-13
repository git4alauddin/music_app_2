<template>
    <div>
        {{ $route.params.title }}
    </div>

    <!-- songs in the playlist -->
    <div>
    <h2>{{ $route.params.title }}</h2>
    <!-- Display songs of the playlist -->
    <div>
      <h3>Playlist Songs</h3>
      <ul>
        <li v-for="song in playlistSongs" :key="song.id">
          <div class="song-details">
            <h3>{{ song.title }}</h3>
            <p><strong>Artist:</strong> {{ song.artist }}</p>
            <p><strong>Genre:</strong> {{ song.genre }}</p>
            <p><strong>Lyrics:</strong> {{ song.lyrics }}</p>
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
            <h3>{{ song.title }} </h3>
            <p><strong>Artist:</strong> {{ song.artist }}</p>
            <p><strong>Genre:</strong> {{ song.genre }}</p>
            <p><strong>Lyrics:</strong> {{ song.lyrics }}</p>
            <!-- Display other song details as needed -->
            <div class="rating">
              <input type="radio" v-model="song.rating" value="1"> 1
              <input type="radio" v-model="song.rating" value="2"> 2
              <input type="radio" v-model="song.rating" value="3"> 3
              <input type="radio" v-model="song.rating" value="4"> 4
              <input type="radio" v-model="song.rating" value="5"> 5
            </div>
            <button @click="rateSong(song.id, parseInt(song.rating))">Rate</button>
            <button @click="addToPlaylist(song.id)">Add to Playlist</button>
            <button @click="deleteSong(song.id)">Delete</button>
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
      this.fetchPlaylistSongs();
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
        })
        this.suggestedSongs = response.data;
        console.log('Songs:', this.suggestedSongs);
      } catch (error) {
        console.error('Error fetching songs:', error);
      }
    },

    async addToPlaylist(songId) {
      try {
        const response = await axios.post(`http://localhost:5000/playlists/playlists/${this.$route.params.id}/songs/${songId}`, {}, {
          headers: { Authorization: localStorage.getItem('token') }, 
        })
        console.log('Song added to playlist:', response.data);

        window.location.reload();
      } catch (error) {
        console.error('Error adding song to playlist:', error);
      }
    },

    async fetchPlaylistSongs() {
      try {
        const response = await axios.get(`http://localhost:5000/playlists/playlists/${this.$route.params.id}/songs`, {
          headers: { Authorization: localStorage.getItem('token') }, 
        })
        this.playlistSongs = response.data;
        console.log('Playlist songs:', this.playlistSongs);
      } catch (error) {
        console.error('Error fetching playlist songs:', error);
      }
    },
  }     
}
</script>

<style scoped>
</style>