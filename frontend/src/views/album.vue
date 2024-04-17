<template>
  <div>
    <h2>{{ $route.params.title }}</h2>

    <!-- album Songs -->
    <div>
      <h3>Album Songs</h3>
      <ul class="album">
        <li v-for="song in albumSongs" :key="song.id">
          <div class="song-details">
            <h3>{{ song.title }} [{{ song.genre }}]</h3>
            <button @click="removeFromAlbum(song.id)">Delete</button>
          </div>
        </li>
      </ul>
      <hr>
    </div>

    <!-- Suggested Songs -->
    <div class="suggested-songs">
      <h2>Suggested Songs</h2>
      <table class="song-table">
        <thead>
          <tr>
            <th>Title</th>
            <th>Artist</th>
            <th>Genre</th>
            <th>Rating</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="song in suggestedSongs" :key="song.id">
            <td>{{ song.title }}</td>
            <td>{{ song.artist }}</td>
            <td>{{ song.genre }}</td>
            <td>[{{ song.average_rating }}]</td>
            <td>
              <button @click="addToAlbum(song.id)">Add to Album</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        suggestedSongs: [],
        albumSongs: [],
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
            headers: { Authorization: 'Bearer ' + localStorage.getItem('token') }, 
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
            headers: { Authorization: 'Bearer ' + localStorage.getItem('token') }, 
          });
          console.log('Song added to album:', response.data);
          this.fetchAlbumSongs();
        } catch (error) {
          console.error('Error adding song to album:', error);
        }
      },
  
      async fetchAlbumSongs() {
        try {
          const response = await axios.get(`http://localhost:5000/albums/albums/${this.$route.params.id}/songs`, {
            headers: { Authorization: 'Bearer ' + localStorage.getItem('token') }, 
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
            headers: { Authorization: 'Bearer ' + localStorage.getItem('token') }, 
          });
          console.log('Song removed from album:', response.data);
          this.fetchAlbumSongs();
        } catch (error) {
          console.error('Error removing song from album:', error);
        } 
      },
    }     
  };
  </script>
  
<style scoped>

.album {
  list-style-type: none;
  padding: 0;
}

.song-details {
  margin-bottom: 10px;
}

.rating {
  margin-top: 5px;
}

.song-table {
  width: 100%;
  border-collapse: collapse;
}

.song-table th,
.song-table td {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

.song-table th {
  background-color: #f2f2f2;
}

/* Hover effect for playlist delete button */
.album button:hover {
  background-color: #ff4d4d;
  color: white;
}

/* Styling for add to playlist button */
.suggested-songs button {
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  transition-duration: 0.4s;
  cursor: pointer;
}

.suggested-songs button:hover {
  background-color: #45a049;
}

/* Style for rating input */
.rating input[type="radio"] {
  display: none;
}

.rating input[type="radio"] + label {
  font-size: 20px;
  color: #bbb;
  cursor: pointer;
  transition: color 0.25s ease-in-out;
}

.rating input[type="radio"]:checked + label {
  color: #ffcc00;
}

/* Additional styling for table rows */
.song-table tbody tr:hover {
  background-color: #f5f5f5;
}

/* Styling for playlist song delete button */
.album button {
  background-color: #f44336; /* Red */
  border: none;
  color: white;
  padding: 8px 16px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  transition-duration: 0.4s;
  cursor: pointer;
}

/* Hover effect for table rows */
.song-table tbody tr:hover {
  background-color: #f2f2f2;
}

</style>
