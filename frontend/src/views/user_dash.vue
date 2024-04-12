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
              <button @click="editSong(song.id)">Edit</button>
              <button @click="deleteSong(song.id)">Delete</button>
            </div>
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
      uploadedSongs: [],
      showUploadedSongs: false
    };
  },
  created() {
    this.fetchUploadedSongs();
  },
  mounted() {    
    this.username = localStorage.getItem('email') || '';
  },
  methods: {
    toggleUploadedSongs(){
      if (this.uploadedSongs.length) {
        this.showUploadedSongs = !this.showUploadedSongs;
      }
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
    editSong(songId) {
      // Implement your edit logic here, e.g., navigate to edit page
      // out api endpoint is 
      console.log('Edit song:', songId);
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
}

  }
};
</script>

<style scoped>
/* Add your component styles here */
.user-info {
  margin-bottom: 20px;
}
.actions {
  display: flex;
  justify-content: space-between;
}
.uploaded-songs {
  margin-top: 20px;
  cursor: pointer;
}
.uploaded-songs h2 {
  text-decoration: underline;
}
.song-details {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
}
</style>
