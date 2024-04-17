<template>
  <div class="user-dash">
    <div class="search-bar">
      <input type="text" placeholder="Search..." v-model="searchQuery">
      <button class="search-btn" @click="searchSongs">Search</button>
    </div>

    <div class="user-info">
      <h2><p>Welcome, {{ email }} [{{ role }}]</p></h2>
      <h3 v-if="role === 'user'" @click="registerAsCreator">[Register as creator]</h3>
    </div><hr>

      <!-- creator stats -->
      <div class="creator-stats-container">
  <h2 id="headings">Statistics</h2>
  <div v-if="loading">Loading...</div>
  <div v-else>
    <table class="creator-stats-table">
      <tr>
        <th>Category</th>
        <th>Value</th>
      </tr>
      <tr>
        <td>Total Songs</td>
        <td>{{ creatorStats.total_songs }}</td>
      </tr>
      <tr>
        <td>Total Albums</td>
        <td>{{ creatorStats.total_albums }}</td>
      </tr>
      <tr>
        <td>Total Playlists</td>
        <td>{{ creatorStats.total_playlists }}</td>
      </tr>
      <tr>
        <td>Average Rating</td>
        <td>{{ creatorStats.average_rating }}</td>
      </tr>
    </table>
  </div>
</div><hr>


    <!-- searched songs -->
    <div class="searched-songs">
      <h2 id="headings">Searched Songs</h2>
      <div class="song-container">
        <div v-for="song in searchedSongs" :key="song.id" class="song-details">
          <h3>{{ song.title }} [{{  song.average_rating }}]</h3>
          <p><strong>Artist:</strong> {{ song.artist }}</p>
          <p><strong>Genre:</strong> {{ song.genre }}</p>
          <button @click="toggleLyrics(song)">Lyrics</button>
          <p v-if="song.showLyrics"><strong>Lyrics:</strong> {{ song.lyrics }}</p>
          <div class="rating">
            <input type="radio" v-model="song.rating" value="1"> 1
            <input type="radio" v-model="song.rating" value="2"> 2
            <input type="radio" v-model="song.rating" value="3"> 3
            <input type="radio" v-model="song.rating" value="4"> 4
            <input type="radio" v-model="song.rating" value="5"> 5
          </div>
          <button @click="rateSong(song.id, parseInt(song.rating))">Rate</button>
          <button @click="playSong(song.id)">Play</button>
        </div>
      </div>
    </div><hr>


    <!-- Suggested Songs -->
    <div class="suggested-songs">
      <h2 id="headings">Suggested Songs</h2>
      <div class="song-container">
        <div v-for="song in suggestedSongs" :key="song.id" class="song-details">
          <h3>{{ song.title }} [{{  song.average_rating }}]</h3>
          <p><strong>Artist:</strong> {{ song.artist }}</p>
          <p><strong>Genre:</strong> {{ song.genre }}</p>
          <button @click="toggleLyrics(song)">Lyrics</button>
          <p v-if="song.showLyrics"><strong>Lyrics:</strong> {{ song.lyrics }}</p>
          <div class="rating">
            <input type="radio" v-model="song.rating" value="1"> 1
            <input type="radio" v-model="song.rating" value="2"> 2
            <input type="radio" v-model="song.rating" value="3"> 3
            <input type="radio" v-model="song.rating" value="4"> 4
            <input type="radio" v-model="song.rating" value="5"> 5
          </div>
          <button @click="rateSong(song.id, parseInt(song.rating))">Rate</button>
          <button @click="playSong(song.id)">Play</button>
        </div>
      </div>
    </div><hr>

    <h2 id = head>Create your own playlists and more...</h2>

    <!-- Upload Song Form -->
    <div class="actions">
      <h2 id="headings"><router-link to="/upload_song">Upload Song</router-link></h2>
    </div>

    <!-- Create Playlist Form -->
    <div class="playlist-form" @click="togglePlaylistForm">
      <h2 id="headings">Create Playlist</h2>
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
      <h2 id="headings">Create Album</h2>
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
    </div><br><hr>


    <h2 id = head>Enjoy your own albums and more...</h2>
    <!-- Uploaded Songs Section -->
    <div class="section">
      <h2 id="headings" @click.prevent="toggleUploadedSongs">Your Uploaded Songs</h2>
      <ul class="uploaded-songs-list" v-if="showUploadedSongs">
        <li v-for="song in uploadedSongs" :key="song.id" class="uploaded-song">
          <div class="song-details">
            <h3>{{ song.title }}</h3>
            <p><strong>Artist:</strong> {{ song.artist }}</p>
            <p><strong>Genre:</strong> {{ song.genre }}</p>
            <p><strong>Lyrics:</strong> {{ song.lyrics }}</p>
            <div>
              <button @click="deleteSong(song.id)">Delete</button>
            </div>
          </div>
        </li>
      </ul>
    </div>



    <!-- Your Albums -->
    <div class="section">
  <h2 id="headings" @click.prevent="toggleYourAlbums">Your Albums</h2>
  <table v-if="showYourAlbums" class="data-table">
    <thead>
      <tr>
        <th>Title</th>
        <th>Release Year</th>
        <th>Actions</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="album in yourAlbums" :key="album.id">
        <td @click="navigateToAlbum(album.id, album.title)">{{ album.title }}</td>
        <td>{{ album.releaseYear }}</td>
        <td>
          <button @click="deleteAlbum(album.id)">Delete</button>
          <button @click="toggleAlbumEditForm(album)">Edit</button>
          <form v-if="album.id === editingAlbumId" @submit.prevent="submitAlbumEditForm">
            <input type="text" v-model="editedAlbumTitle" placeholder="Enter new title" required>
            <input type="number" v-model="editedAlbumReleaseYear" placeholder="Enter new release year" required>
            <button type="submit">Save</button>
          </form>
        </td>
      </tr>
    </tbody>
  </table>
</div>

<div class="section">
  <h2 id="headings" @click.prevent="toggleYourPlaylists">Your Playlists</h2>
  <table v-if="showYourPlaylists" class="data-table">
    <thead>
      <tr>
        <th>Title</th>
        <th>Actions</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="playlist in yourPlaylists" :key="playlist.id">
        <td @click="navigateToPlaylist(playlist.id, playlist.title)">{{ playlist.title }}</td>
        <td>
          <button @click="deletePlaylist(playlist.id)">Delete</button>
          <button @click="togglePlaylistEditForm(playlist)">Edit</button>
          <form v-if="playlist.id === editingPlaylistId" @submit.prevent="submitPlaylistEditForm">
            <input type="text" v-model="editedPlaylistTitle" placeholder="Enter new title" required>
            <button type="submit">Save</button>
          </form>
        </td>
      </tr>
    </tbody>
  </table><hr>
</div>

    <!---------------------- player------------- -->
    <div class="player">
        <div class="song_info">
            <h3>playing [song] by [artist]...</h3>
        </div>

        <audio  controls>
          <source :src="songFilePath" type="audio/mpeg">
        </audio>

        
      </div>
      <!---------------------- player------------- -->





  </div>
</template>



<script>

import axios from 'axios'; 
export default {
  data() {
    return {
      username: '',
      user_id : '',
      role: '',
      uploadedSongs: [],
      yourAlbums: [],
      yourPlaylists: [],
      suggestedSongs: [],
      showUploadedSongs: false,
      showPlaylistForm: false,
      showAlbumForm: false,
      showYourAlbums: false,
      showYourPlaylists: false,

      playlistName: '',
      albumName: '',
      releaseYear: '',

      editingPlaylistId: null,
      editedPlaylistTitle: '',

      editingAlbumId: null,
      editedAlbumTitle: '',
      editedAlbumReleaseYear: '',

      showLyrics: false,
      searchedSongs : '',

      creatorStats: '',

      song: '',
      artist: '',
      songFileName:  '',
    };
  },
  created() {
    this.fetchUploadedSongs();
    this.fetchYourAlbums();
    this.fetchYourPlaylists();
    this.fetchSuggestedSongs();
    this.fetchCreatorStats();
  },
  mounted() {    
    this.email = localStorage.getItem('email') || '';
    this.user_id = localStorage.getItem('id') || '';
    this.role = localStorage.getItem('role') || '';

  
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
          headers: { Authorization: 'Bearer ' + localStorage.getItem('token') }, 
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
          headers: { Authorization: 'Bearer ' + localStorage.getItem('token') },
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
          headers: { Authorization: 'Bearer ' +localStorage.getItem('token') },
        })
        this.yourPlaylists = response.data;
        console.log('Your playlists:', this.yourPlaylists);
      } catch (error) {
        console.error('Error fetching your playlists:', error);
      }
    },


    async fetchCreatorStats() {
        try {
          const response = await axios.get('http://localhost:5000/users/users/creator_stats' , {
            headers: { Authorization: 'Bearer ' + localStorage.getItem('token') },
          });

          this.creatorStats = response.data;
        } catch (error) {   
          console.error('Error fetching creator stats:', error);
        }
      },

    deleteSong(songId) {
      axios.delete(`http://localhost:5000/songs/delete_song/${songId}`, {
        headers: { Authorization: 'Bearer ' + localStorage.getItem('token') }, 
      })
      .then(response => {
        // If the deletion was successful, remove the song from the uploadedSongs array
        this.uploadedSongs = this.uploadedSongs.filter(song => song.id !== songId);
        console.log('Song deleted successfully.');

        this.fetchCreatorStats();
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
          headers: { Authorization: 'Bearer ' + localStorage.getItem('token') }, 
        });
        console.log('Playlist created successfully:', response.data);
        this.playlistName = '';
        this.showPlaylistForm = false;

        this.fetchYourPlaylists();
        this.fetchCreatorStats();
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
          headers: { Authorization: 'Bearer '  + localStorage.getItem('token') }, 
        });
        console.log('Album created successfully:', response.data);
        this.albumName = '';
        this.showAlbumForm = false;

        this.fetchYourAlbums();
        this.fetchCreatorStats();
      } catch (error) {
        console.error('Error creating album:', error);
      }
    },

    async deleteAlbum(albumId) {
      axios.delete(`http://localhost:5000/albums/albums/${albumId}`, {
        headers: { Authorization: 'Bearer ' + localStorage.getItem('token') }, 
      })
      .then(response => {
        // If the deletion was successful, remove the album from the yourAlbums array
        this.yourAlbums = this.yourAlbums.filter(album => album.id !== albumId);
        console.log('Album deleted successfully.');

        this.fetchYourAlbums();
        this.fetchCreatorStats();
      })
      .catch(error => {
        console.error('Error deleting album:', error);
      });
    },

    async deletePlaylist(playlistId) {
      axios.delete(`http://localhost:5000/playlists/playlists/${playlistId}`, {
        headers: { Authorization: 'Bearer ' + localStorage.getItem('token') }, 
      })
      .then(response => {
        // If the deletion was successful, remove the playlist from the yourPlaylists array
        this.yourPlaylists = this.yourPlaylists.filter(playlist => playlist.id !== playlistId);
        console.log('Playlist deleted successfully.');
        
        this.fetchYourPlaylists();
        this.fetchCreatorStats();
      })
      .catch(error => {
        console.error('Error deleting playlist:', error);
      });
    },

    // registerAsCreator()  
    async registerAsCreator() {
      try {
        const response = await axios.put(`http://localhost:5000/users/users/${this.user_id}`, {
          id: this.user_id
        }, {
          headers: { Authorization: 'Bearer ' + localStorage.getItem('token') }, 
        });
        console.log('User registered as creator successfully:', response.data);
        
        localStorage.setItem('role', 'creator');
        window.location.reload();

      } catch (error) {
        console.error('Error registering as creator:', error);
      }
    },

    async fetchSuggestedSongs() {
      try {
        const response = await axios.get('http://localhost:5000/songs/songs', {
          headers: { Authorization: 'Bearer ' + localStorage.getItem('token') }, 
        })
        this.suggestedSongs = response.data;
        console.log('Songs:', this.suggestedSongs);
      } catch (error) {
        console.error('Error fetching songs:', error);
      }
    },

    async rateSong(songId, rating) {
      try {
        const response = await axios.post(`http://localhost:5000/songs/rate_song`, {
          rating: rating,
          song_id: songId
        }, {
          headers: { Authorization: 'Bearer ' + localStorage.getItem('token') }, 
        });
        console.log('Song rated successfully:', response.data);

        this.fetchSongs();
        this.searchSongs();
        this.fetchCreatorStats();
      } catch (error) {
        console.error('Error rating song:', error);
      }
    },


  navigateToPlaylist(id, title) {
    this.$router.push({ name: 'playlist', params: { id: id, title: title }});
  },

  navigateToAlbum(id, title) {
    this.$router.push({ name: 'album', params: { id: id, title: title }});
  },

  // ----------------------------playlist------------------------------- //

  togglePlaylistEditForm(playlist) {
  if (playlist && playlist.id) {
    this.editingPlaylistId = playlist.id;
    this.editedPlaylistTitle = playlist.title;
  } else {
    console.error('Invalid playlist:', playlist);
  }
},

  toggleAlbumEditForm(album) {
  if (album && album.id) {
    this.editingAlbumId = album.id;
    this.editedAlbumTitle = album.title;
    this.editedAlbumReleaseYear = album.releaseYear;
  } else {
    console.error('Invalid album:', album);
  } 
  },


  async submitPlaylistEditForm() {
    axios.put(`http://localhost:5000/playlists/playlists/${this.editingPlaylistId}`, {
      id: this.editingPlaylistId,
      title: this.editedPlaylistTitle
    }, {
      headers: { Authorization: localStorage.getItem('token') }, 
    })
    .then(response => {
      console.log('Playlist updated successfully:', response.data);
      this.editingPlaylistId = null;
      this.editedPlaylistTitle = null;
      this.fetchYourPlaylists();
    })
    .catch(error => {
      console.error('Error updating playlist:', error);
    });
  },

  async submitAlbumEditForm() {
    axios.put(`http://localhost:5000/albums/albums/${this.editingAlbumId}`, {
      id: this.editingAlbumId,
      title: this.editedAlbumTitle,
      release_year: this.editedAlbumReleaseYear
    }, {
      headers: { Authorization: localStorage.getItem('token') }, 
    })
    .then(response => {
      console.log('Album updated successfully:', response.data);
      this.editingAlbumId = null;
      this.editedAlbumTitle = null;
      this.editedAlbumReleaseYear = null;
      this.fetchYourAlbums();
    })
    .catch(error => {
      console.error('Error updating album:', error);
    });
  },

  toggleLyrics(song) {
    song.showLyrics = !song.showLyrics;
  },


  async searchSongs() {
    try {
      const response = await axios.get(`http://localhost:5000/songs/songs/search/${this.searchQuery}`, {
        headers: { Authorization: localStorage.getItem('token') }, 
      });
      this.searchedSongs = response.data;
    } catch (error) {
      console.error('Error searching songs:', error);
    }
  },


  // ------------------------------------play song--------------------
  async playSong(songId) {
    try {
      const response = await axios.get(`http://localhost:5000/songs/songs/play_song/${songId}`, {
        headers: { Authorization: 'Bearer ' + localStorage.getItem('token') }, 
      });
      this.songFileName = response.data;
      console.log('song_file:', response.data);
    } catch (error) {
      console.error('Error playing song:', error);
    }
  },

  },
  computed: {
    songFilePath() {
      return `C:/Users/ASUS/Desktop/proj/music_app_2/backend/static/songs/${this.songFileName}`; 
    }
  }
};

</script>

<style scoped>

#head{
  border: solid 2px rgb(223, 242, 102);
  border-radius: 5px;
  text-align: center;
  color:rgb(9, 123, 45);
  background-color: rgb(242, 233, 210);
}

#headings {
  padding: 8px 12px;
  border: none;
  width:48%;
  border-radius: 4px;
  margin-top: 10px;
  margin-bottom: 10px;
  margin-left: 23%;
  cursor: pointer;
  background-color: #555;
  color: white;
  text-align: center;
}

#headings a {
  color: white;
  text-decoration: none;}

#headings:hover {
  background-color: #777;
}

  /* ------------------------------creator stats------------------ */
  .creator-stats-container {
  margin-top: 20px;
}

.creator-stats-container h2 {
  font-size: 24px;
  margin-bottom: 10px;
}

.creator-stats-table {
  width: 100%;
  border-collapse: collapse;
  border-spacing: 0;
}

.creator-stats-table th,
.creator-stats-table td {
  padding: 12px;
  text-align: left;
}

.creator-stats-table th {
  font-weight: bold;
  background-color: #4CAF50;
  color: white;
}

.creator-stats-table tr:nth-child(even) {
  background-color: #f2f2f2;
}

.creator-stats-table tr:hover {
  background-color: #ddd;
}

.creator-stats-container div.loading-message {
  font-size: 16px;
  text-align: center;
}


  /* -------------------Dashboard Heading ----------------------------*/
  h1 {
    text-align: center;
    color: #333; 
    margin-bottom: 20px; 
  }

  
  .user-info {
    text-align: center; 
    margin-bottom: 30px; 
  }

  .user-info p {
    color: #666; 
  }

  
  .user-info h3 {
    cursor: pointer;
    color: #007bff; 
    transition: color 0.3s ease; 
  }

  
  .user-info h3:hover {
    color: #0056b3; 
  }






/* Suggested Songs section */
.suggested-songs {
  margin-bottom: 30px;
}

.suggested-songs h2 {
  color: #333;
}

/* Song details */
.song-container {
  display: flex;
  flex-wrap: wrap;
  
}

.song-details {
  flex: 0 0 calc(25% - 20px); /* 4 boxes per row with some margin */
  margin: 10px;
  padding: 15px;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-sizing: border-box;
  transition: all 0.3s ease; /* Smooth transition on hover */
  background-color: rgb(250, 239, 239);
}

.song-details:hover {
  transform: translateY(-5px); /* Move the box up slightly on hover */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Add shadow on hover */
}

.song-details h3 {
  margin-bottom: 5px;
}

.song-details p {
  color: #666;
}

.rating {
  margin-top: 5px;

}

.rating input[type="radio"] {
  display: inline-block;
  margin-right: 5px;
}

/* Button styles */
.song-details button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 8px 15px;
  margin-top: 5px; /* Add some space between buttons */
  margin-right:10px;
  cursor: pointer;
  border-radius: 4px;
  transition: background-color 0.3s ease; /* Smooth transition on hover */
}

.song-details button:hover {
  background-color: #0056b3; /* Darker color on hover */
}




/* Style for uploaded songs section */
.section {
  margin-top: 20px;
}

.uploaded-songs-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  padding: 0;
}

.uploaded-song {
  flex: 1 1 calc(25% - 20px);
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
  margin-bottom: 10px;
  padding: 10px;
}

.uploaded-song:hover {
  background-color: #f0f0f0;
}

.song-details {
  margin-bottom: 10px;
}

/* Style for buttons */
button {
  padding: 5px 10px;
  border: none;
  border-radius: 3px;
  margin-left:4px;
  cursor: pointer;
  background-color: #007bff;
  color: #fff;
}

button:hover {
  background-color: #0056b3;
}


  /* --------------------------------------------------tables-------------------------------------------------- */
  .section {
  margin-bottom: 20px;
}

.section h2 {
  font-size: 20px;
  cursor: pointer;
  margin-bottom: 10px;
}

.data-table {
  width: 100%;
  border-collapse: collapse;
}

.data-table th,
.data-table td {
  padding: 12px;
  border-bottom: 1px solid #ddd;
  text-align: left;
}

.data-table th {
  background-color: #f2f2f2;
  font-weight: bold;
}

.data-table tr:nth-child(even) {
  background-color: #f9f9f9;
}

.data-table tr:hover {
  background-color: #f2f2f2;
}

.data-table td:first-child {
  cursor: pointer;
}

.data-table button {
  margin-right: 5px;
  padding: 8px 12px;
  border: none;
  border-radius: 4px;
  background-color: #4CAF50;
  color: white;
  cursor: pointer;
}

.data-table button:hover {
  background-color: #45a049;
}

.data-table form input {
  padding: 6px 10px;
  margin-right: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.data-table form button {
  padding: 8px 12px;
  border: none;
  border-radius: 4px;
  background-color: #4CAF50;
  color: white;
  cursor: pointer;
}

.data-table form button:hover {
  background-color: #45a049;
}


/* -------------------------------------------------------------------------------forms---------------------------------------------------- */
/* Form container styles */
.form-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Form styles */
.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-group input[type="text"],
.form-group input[type="number"] {
  width: calc(100% - 22px); /* Adjust width for the border */
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.form-group input[type="text"]:focus,
.form-group input[type="number"]:focus {
  outline: none;
  border-color: #007bff;
}

.form-group button[type="submit"] {
  width: calc(100% - 22px); /* Adjust width for the border */
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.form-group button[type="submit"]:hover {
  background-color: #0056b3;
}


/* -----------------player--------------- */
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







