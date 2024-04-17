<template>
  <div>
    <h2>{{ $route.params.title }}</h2>

    <!-- Playlist Songs -->
    <div>
      <h3>Playlist Songs</h3>
      <ul class="playlist">
        <li v-for="song in playlistSongs" :key="song.id">
          <div class="song-details">
            <h3>{{ song.title }} [{{ song.genre }}]</h3>
            <button @click="removeFromPlaylist(song.id)">Delete</button>
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
              <button @click="addToPlaylist(song.id)">Add to Playlist</button>
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
      playlistSongs: [],
    };
  },
  created() {
    this.fetchPlaylistSongs();
    this.fetchSuggestedSongs();
  },
  methods: {
    async fetchSuggestedSongs() {
      try {
        const response = await axios.get('http://localhost:5000/songs/songs', {
          headers: { Authorization: 'Bearer ' + localStorage.getItem('token') },
        })
        this.suggestedSongs = response.data;
      } catch (error) {
        console.error('Error fetching songs:', error);
      }
    },
    async addToPlaylist(songId) {
      try {
        const response = await axios.post(`http://localhost:5000/playlists/playlists/${this.$route.params.id}/songs/${songId}`, {}, {
          headers: { Authorization: 'Bearer ' + localStorage.getItem('token') },
        })
        console.log('Song added to playlist:', response.data);
        this.fetchPlaylistSongs();
      } catch (error) {
        console.error('Error adding song to playlist:', error);
      }
    },
    async fetchPlaylistSongs() {
      try {
        const response = await axios.get(`http://localhost:5000/playlists/playlists/${this.$route.params.id}/songs`, {
          headers: { Authorization: 'Bearer ' + localStorage.getItem('token') },
        })
        this.playlistSongs = response.data;
      } catch (error) {
        console.error('Error fetching playlist songs:', error);
      }
    },
    async removeFromPlaylist(songId) {
      try {
        const response = await axios.delete(`http://localhost:5000/playlists/playlists/${this.$route.params.id}/songs/${songId}`, {
          headers: { Authorization: 'Bearer ' + localStorage.getItem('token') },
        })
        console.log('Song removed from playlist:', response.data);
        this.fetchPlaylistSongs();
      } catch (error) {
        console.error('Error removing song from playlist:', error);
      }
    },
  }
}
</script>

<style scoped>
.playlist {
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
.playlist button:hover {
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
.playlist button {
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

