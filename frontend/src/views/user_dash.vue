<template>
  <div>
    <h1>User Dashboard</h1>
    <div class="user-info">
      <p>Welcome, {{ username }}</p>
      <!-- Other user information display -->
    </div>
    <div class="actions">
      <router-link to="/upload_song">Upload Song</router-link>
      <!-- Other actions or links for the user -->
    </div>
    <div class="uploaded-songs">
      <h2 @click.prevent="toggleUploadedSongs">Your Uploaded Songs</h2>
      <ul v-if="showUploadedSongs">
        <li v-for="song in uploadedSongs" :key="song.id">
          <div class="song-details">
            <h3>{{ song.title }}</h3>
            <p><strong>Artist:</strong> {{ song.artist }}</p>
            <p><strong>Genre:</strong> {{ song.genre }}</p>
            <p><strong>Lyrics:</strong> {{ song.lyrics }}</p>
            <!-- Display other song details as needed -->
            <div>
              <button @click="deleteSong(song.id)">Delete</button>
            </div>
          </div>
        </li>
      </ul>
    </div>
    
    <!-- Create Playlist Form -->
    <div class="playlist-form" @click="togglePlaylistForm">
      <h2>Create Playlist</h2>
      <form v-if="showPlaylistForm" @submit.prevent="createPlaylist">
        <div class="form-group">
          <label for="playlistName">Playlist Name:</label>
          <input type="text" id="playlistName" v-model="playlistName" @click.stop required>
        </div>
        <button type="submit" @click="createPlaylist">Create Playlist</button>
      </form>
    </div>

    <!-- Create Album Form -->
    <div class="album-form" @click="toggleAlbumForm">
      <h2>Create Album</h2>
      <form v-if="showAlbumForm" @submit.prevent="createAlbum">
        <div class="form-group">
          <label for="albumName">Album Name:</label>
          <input type="text" id="albumName" v-model="albumName" @click.stop required>
          </div>
          <div class="form-group">
            <label for="releaseYear">Release Year:</label>
            <input type="number" id="releaseYear" v-model="releaseYear" @click.stop required>
        </div>
        <button type="submit" @click="createAlbum">Create Album</button>
      </form>
    </div>

    <!-- Your Albums -->
    <div class="your-albums">
      <h2 @click.prevent="toggleYourAlbums">Your Albums</h2>
      <ul v-if="showYourAlbums">
        <li v-for="album in yourAlbums" :key="album.id">
          <div class="album-details">
            <h3>{{ album.title }}</h3>
            <p><strong>Release Year:</strong> {{ album.release_year }}</p>
            <!-- Display other album details as needed -->
          </div>
        </li>
      </ul>
    </div>


    <!-- Your Playlists -->
    <div class="your-playlists">
      <h2 @click.prevent="toggleYourPlaylists">Your Playlists</h2>
      <ul v-if="showYourPlaylists">
        <li v-for="playlist in yourPlaylists" :key="playlist.id">
          <div class="playlist-details">
            <h3>{{ playlist.title }}</h3>
            <!-- Display other playlist details as needed -->
          </div>
        </li>
      </ul>
    </div>

  </div>
</template>

<script>
import axios from 'axios'; 
export default {
  data() {
    return {
      username: '',
      user_id : '',
      uploadedSongs: [],
      yourAlbums: [],
      yourPlaylists: [],
      showUploadedSongs: false,
      showPlaylistForm: false,
      showAlbumForm: false,
      showYourAlbums: false,
      showYourPlaylists: false,
      playlistName: '',
      albumName: '',
      releaseYear: '',
    };
  },
  created() {
    this.fetchUploadedSongs();
    this.fetchYourAlbums();
    this.fetchYourPlaylists();
  },
  mounted() {    
    this.username = localStorage.getItem('email') || '';
    this.user_id = localStorage.getItem('id') || '';
  },
  methods: {
    toggleUploadedSongs(){
      if (this.uploadedSongs.length) {
        this.showUploadedSongs = !this.showUploadedSongs;
      }
    },
    toggleYourAlbums(){
      if (this.yourAlbums.length) {
        this.showYourAlbums = !this.showYourAlbums;
      }
    },
    toggleYourPlaylists(){
      if (this.yourPlaylists.length) {
        this.showYourPlaylists = !this.showYourPlaylists;
      }
    },
    togglePlaylistForm(){
      this.showPlaylistForm = !this.showPlaylistForm;
      // Hide album form when playlist form is toggled
      this.showAlbumForm = false;
    },
    toggleAlbumForm(){
      this.showAlbumForm = !this.showAlbumForm;
      // Hide playlist form when album form is toggled
      this.showPlaylistForm = false;
    },

    async fetchUploadedSongs() {
      try {
        const response = await axios.get('http://localhost:5000/users/users/songs', {
          headers: { Authorization: localStorage.getItem('token') }, 
        });
        this.uploadedSongs = response.data;
        console.log('Uploaded songs:', this.uploadedSongs);
      } catch (error) {
        console.error('Error fetching uploaded songs:', error);
      }
    },

    async fetchYourAlbums() {
      try {
        const response = await axios.get('http://localhost:5000/users/users/albums', {
          headers: { Authorization: localStorage.getItem('token') },
        })
        this.yourAlbums = response.data;
        console.log('Your albums:', this.yourAlbums);
      } catch (error) {
        console.error('Error fetching your albums:', error);
      }
    },

    async fetchYourPlaylists() {
      try {
        const response = await axios.get('http://localhost:5000/users/users/playlists', {
          headers: { Authorization: localStorage.getItem('token') },
        })
        this.yourPlaylists = response.data;
        console.log('Your playlists:', this.yourPlaylists);
      } catch (error) {
        console.error('Error fetching your playlists:', error);
      }
    },

    deleteSong(songId) {
      axios.delete(`http://localhost:5000/songs/delete_song/${songId}`, {
        headers: { Authorization: localStorage.getItem('token') }, 
      })
      .then(response => {
        // If the deletion was successful, remove the song from the uploadedSongs array
        this.uploadedSongs = this.uploadedSongs.filter(song => song.id !== songId);
        console.log('Song deleted successfully.');
      })
      .catch(error => {
        console.error('Error deleting song:', error);
      });
    },

    async createPlaylist() {
      try {
        const response = await axios.post(`http://localhost:5000/playlists/playlists/${this.user_id}`, {
          title: this.playlistName,
          id: this.user_id 
        }, {
          headers: { Authorization: localStorage.getItem('token') }, 
        });
        console.log('Playlist created successfully:', response.data);
        this.playlistName = '';
        this.showPlaylistForm = false;

        this.fetchYourPlaylists();
      } catch (error) {
        console.error('Error creating playlist:', error);
      }
    },

    async createAlbum() {
      try {
        const response = await axios.post(`http://localhost:5000/albums/albums/${this.user_id}`, {
          title: this.albumName,
          release_year: this.releaseYear
        }, {
          headers: { Authorization: localStorage.getItem('token') }, 
        });
        console.log('Album created successfully:', response.data);
        this.albumName = '';
        this.showAlbumForm = false;

        this.fetchYourAlbums();
      } catch (error) {
        console.error('Error creating album:', error);
      }
    },

  }
};
</script>

<style scoped>

</style>


