<template>
    <div>
      <h1>{{ role }} Dashboard</h1>
      <div class="user-info">
        <p>Welcome, {{ email }} [{{ role }}]</p>
      </div>
  
      <!-- Users Section -->
      <div class="section">
        <button @click="toggleUsers">Users</button>
        <div class="users" v-if="showUsers && users.length > 0">
          <div v-for="user in users" :key="user.id" class="user">
            <h3>{{ user.email }}</h3>
            <h2>{{ user.username }}</h2>
            <button @click="blacklistUser(user.id)">Blacklist</button>
          </div>
        </div>
      </div>
  
      <!-- Albums Section -->
      <div class="section">
        <button @click="toggleAlbums">Albums</button>
        <div class="albums" v-if="showAlbums && albums.length > 0">
          <div v-for="album in albums" :key="album.id" class="album">
            <h3>{{ album.title }}</h3>
            <h2>{{ album.release_year }}</h2>
            <button @click="deleteAlbum(album.id)">Delete</button>
          </div>
        </div>
      </div>
  
      <!-- Playlists Section -->
      <div class="section">
        <button @click="togglePlaylists">Playlists</button>
        <div class="playlists" v-if="showPlaylists && playlists.length > 0">
          <div v-for="playlist in playlists" :key="playlist.id" class="playlist">
            <h3>{{ playlist.title }}</h3>
            <button @click="deletePlaylist(playlist.id)">Delete</button>
          </div>
        </div>
      </div>
  
      <!-- Songs Section -->
      <div class="section">
        <button @click="toggleSongs">Songs</button>
        <div class="songs" v-if="showSongs && songs.length > 0">
          <div v-for="song in songs" :key="song.id" class="song">
            <h3>{{ song.title }}</h3>
            <button @click="blacklistSong(song.id)">Blacklist</button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        email: '',
        role: '',
        users: [],
        albums: [],
        playlists: [],
        songs: [],
        showUsers: false,
        showAlbums: false,
        showPlaylists: false,
        showSongs: false,
      };
    },
  
    mounted() {
      this.email = localStorage.getItem('email') || '';
      this.role = localStorage.getItem('role') || '';
    },
  
    methods: {
      async fetchUsers() {
        try {
          const response = await axios.get('http://localhost:5000/users/users');
          this.users = response.data;
        } catch (error) {
          console.error('Error fetching users:', error);
        }
      },
  
      async fetchAlbums() {
        try {
          const response = await axios.get('http://localhost:5000/albums/albums');
          this.albums = response.data;
        } catch (error) {
          console.error('Error fetching albums:', error);
        }
      },      
  
      async fetchPlaylists() {
        try {
          const response = await axios.get('http://localhost:5000/playlists/playlists');
          this.playlists = response.data;
        } catch (error) {
          console.error('Error fetching playlists:', error);
        }
      },
  
      async fetchSongs() {
        try {
          const response = await axios.get('http://localhost:5000/songs/songs');
          this.songs = response.data;
        } catch (error) {
          console.error('Error fetching songs:', error);
        }
      },
  
      async blacklistUser(userId) {
        try {
          // Implement your API call to blacklist user by userId
          console.log('Blacklisting user:', userId);
        } catch (error) {
          console.error('Error blacklisting user:', error);
        }
      },
  
      async blacklistSong(songId) {
        try {
          const response = await axios.get(`http://localhost:5000/songs/songs/flag_song/${songId}`, {
            headers: { Authorization: localStorage.getItem('token') },
          })
          console.log('Song blacklisted successfully:', response.data);
        } catch (error) {
          console.error('Error blacklisting song:', error);
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
  
      toggleUsers() {
        this.showUsers = !this.showUsers;
        if (this.showUsers) {
          this.fetchUsers();
        }
      },
  
      toggleAlbums() {
        this.showAlbums = !this.showAlbums;
        if (this.showAlbums) {
          this.fetchAlbums();
        }
      },
  
      togglePlaylists() {
        this.showPlaylists = !this.showPlaylists;
        if (this.showPlaylists) {
          this.fetchPlaylists();
        }
      },
  
      toggleSongs() {
        this.showSongs = !this.showSongs;
        if (this.showSongs) {
          this.fetchSongs();
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Style for main dashboard container */
  .user-info {
    margin-bottom: 20px;
  }
  
  /* Style for sections */
  .section {
    margin-bottom: 20px;
  }
  
  button {
    margin-bottom: 10px;
  }
  
  .user,
  .album,
  .playlist,
  .song {
    flex: 1 1 calc(25% - 20px);
    margin-bottom: 10px;
    border: 1px solid #ccc;
    padding: 10px;
    border-radius: 5px;
    background-color: #f9f9f9;
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
  
  /* Style for user section */
  .users,
  .albums,
  .playlists,
  .songs {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }
  </style>
  