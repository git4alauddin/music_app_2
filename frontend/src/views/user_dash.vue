<template>
  <div>
    <div class="search-bar">
      <input type="text" placeholder="Search..." v-model="searchQuery">
      <button class="search-btn" @click="searchSongs">Search</button>
    </div>

    <h1>{{ role }} Dashboard</h1>
    <div class="user-info">
      <p>Welcome, {{ email }} [{{ role }}]</p>
      <h3 v-if="role === 'user'" @click="registerAsCreator">[Register as creator]</h3>
    </div>

    <!-- searched songs -->
    <div class="searched-songs">
      <h2>Searched Songs</h2>
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
    </div>


    <!-- Suggested Songs -->
    <div class="suggested-songs">
      <h2>Suggested Songs</h2>
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
    </div>

    <!-- Upload Song Form -->
    <div class="actions">
      <h2><router-link to="/upload_song">Upload Song</router-link></h2>
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
    <div class="section">
      <h2 @click.prevent="toggleYourAlbums">Your Albums</h2>
      <ul v-if="showYourAlbums">
        <li v-for="album in yourAlbums" :key="album.id">
          <div class="album-details">
            <h3 @click="navigateToAlbum(album.id, album.title)">{{ album.title }}</h3>
            <p><strong>Release Year:</strong> {{ album.releaseYear }}</p>
          </div>
          <button @click="deleteAlbum(album.id)">Delete</button>
          <button @click="toggleAlbumEditForm(album)">Edit</button>
          <form v-if="album.id === editingAlbumId" @submit.prevent="submitAlbumEditForm">
            <input type="text" v-model="editedAlbumTitle" placeholder="Enter new title" required>
            <input type="number" v-model="editedAlbumReleaseYear" placeholder="Enter new release year" required>
            <button type="submit">Save</button>
          </form>
        </li>
      </ul>
    </div>

    <!-- Your Playlists -->
    <div class="section">
      <h2 @click.prevent="toggleYourPlaylists">Your Playlists</h2>
      <ul v-if="showYourPlaylists">
        <li v-for="playlist in yourPlaylists" :key="playlist.id">
          <div class="playlist-details">
            <h3 @click="navigateToPlaylist(playlist.id, playlist.title)">{{ playlist.title }}</h3>
          </div>
          <button @click="deletePlaylist(playlist.id)">Delete</button>
          <button @click="togglePlaylistEditForm(playlist)">Edit</button>
          <form v-if="playlist.id === editingPlaylistId" @submit.prevent="submitPlaylistEditForm">
            <input type="text" v-model="editedPlaylistTitle" placeholder="Enter new title" required>
            <button type="submit">Save</button>
          </form>
        </li>
      </ul>
    </div>

    <!-- Uploaded Songs Section -->
    <div class="section">
      <h2 @click.prevent="toggleUploadedSongs">Your Uploaded Songs</h2>
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
      searchedSongs : ''
    };
  },
  created() {
    this.fetchUploadedSongs();
    this.fetchYourAlbums();
    this.fetchYourPlaylists();
    this.fetchSongs();
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

    async deleteAlbum(albumId) {
      axios.delete(`http://localhost:5000/albums/albums/${albumId}`, {
        headers: { Authorization: localStorage.getItem('token') }, 
      })
      .then(response => {
        // If the deletion was successful, remove the album from the yourAlbums array
        this.yourAlbums = this.yourAlbums.filter(album => album.id !== albumId);
        console.log('Album deleted successfully.');

        this.fetchYourAlbums();
      })
      .catch(error => {
        console.error('Error deleting album:', error);
      });
    },

    async deletePlaylist(playlistId) {
      axios.delete(`http://localhost:5000/playlists/playlists/${playlistId}`, {
        headers: { Authorization: localStorage.getItem('token') }, 
      })
      .then(response => {
        // If the deletion was successful, remove the playlist from the yourPlaylists array
        this.yourPlaylists = this.yourPlaylists.filter(playlist => playlist.id !== playlistId);
        console.log('Playlist deleted successfully.');
        
        this.fetchYourPlaylists();
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
          headers: { Authorization: localStorage.getItem('token') }, 
        });
        console.log('User registered as creator successfully:', response.data);
        
        localStorage.setItem('role', 'creator');
        window.location.reload();

      } catch (error) {
        console.error('Error registering as creator:', error);
      }
    },

    async fetchSongs() {
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

    async rateSong(songId, rating) {
      try {
        const response = await axios.post(`http://localhost:5000/songs/rate_song`, {
          rating: rating,
          song_id: songId
        }, {
          headers: { Authorization: localStorage.getItem('token') }, 
        });
        console.log('Song rated successfully:', response.data);

        this.fetchSongs();
        this.searchSongs();
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
  }

  }
};

</script>

<style scoped>
  /* Dashboard Heading */
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
  cursor: pointer;
  background-color: #007bff;
  color: #fff;
}

button:hover {
  background-color: #0056b3;
}
</style>







