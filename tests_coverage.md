## Automated Tests Coverage ##
### Technologies Stack Description ###
- **Python 3.7.x** _as main programming language._  
- **py.test**  _library as test running system._
- **requests** _library for sending GraphQL requests and parse responses._
- **psycopg2** _as the driver over PostgreSQL for communication with it._
- **selenium** _powerful tool for communication with browsers._
- **Pandas** _library for saving information from db. Much faster than built-in tools in case of big data sets._

### API Automated Tests Coverage ###
#### Query Request ####
:heavy_check_mark: Get all songs and compare with DB output  
:heavy_check_mark: Get all playlists without song parameter and compare with DB output  
:heavy_check_mark: Get all playlists with song parameter and compare with DB output
:heavy_check_mark: Check Playlists low boundary output and compare with DB output  
:heavy_check_mark: Check Playlists out of low boundary output and compare with DB output  
:heavy_check_mark: Check Playlists high boundary output and compare with DB output  
:heavy_check_mark: Check Playlists out of high boundary output and compare with DB output  
:heavy_check_mark: Check correct Song id output and compare with DB output  
:heavy_check_mark: Check Songs low boundary output and compare with DB output  
:heavy_check_mark: Check Songs out of low boundary output and compare with DB output  
:heavy_check_mark: Check Songs high boundary output and compare with DB output  
:heavy_check_mark: Check Songs out of high boundary output and compare with DB output
#### Mutation createPlaylist Request ####
:heavy_check_mark: Create playlist with random name and check in DB  
:heavy_check_mark: Create playlist with empty name and check in DB  
:heavy_check_mark: Create playlist with existing name and check in DB  
:heavy_check_mark: Create playlist with long name (129 symbols) and check in DB  
:heavy_check_mark: Create Playlist with random songs and check in DB  
:heavy_check_mark: Create Playlist with all songs and check in DB  
#### Mutation editPlaylist Request ####
:heavy_check_mark: Change Playlist name to new name and check in DB  
:heavy_check_mark: Change Playlist name to the same name and check in DB  
:heavy_check_mark: Change Playlist name to empty name and check in DB  
:heavy_check_mark: Change Playlist name to already existing name and check in DB  
:heavy_check_mark: Add correct Song to Playlist and check in DB  
:heavy_check_mark: Add incorrect Song to Playlist and check in DB  
:heavy_check_mark: Remove Song from Playlist and check in DB  
:heavy_check_mark: Apply no changes and check in DB  
:heavy_check_mark: Add all Songs to Playlist and check in DB  
:heavy_check_mark: Add Song to Playlist with all Songs and check in DB  
:heavy_check_mark: Remove all Songs from Playlist and check in DB  
#### Mutation deletePlaylist Request ####
:heavy_check_mark: Delete Playlist with correct id and check in DB  
:heavy_check_mark: Delete Playlist with incorrect id and check in DB  
#### TBD Tests ####
:heavy_multiplication_x: Search API tests  
### UI Automated Tests Coverage ###
#### Albums Tab ####
:heavy_check_mark: Tabs links presented on the page  
:heavy_check_mark: Albums tab header presented on the page  
:heavy_check_mark: Count of displayed Albums and Albums from DB are the same  
:heavy_check_mark: All Artists names presented on the page  
:heavy_check_mark: All Albums names presented on the page  
:heavy_check_mark: Each Album have needed songs names

#### Playlists Tab ####
:heavy_check_mark: Playlists tab header presented on the page  
:heavy_check_mark: Add playlist icon presented on the page  
:heavy_check_mark: Count of displayed Playlists and Playlists from DB are the same  
:heavy_check_mark: Each Playlist has correct name  
:heavy_check_mark: Each Playlist has correct songs inside

#### Library Tab ####
:heavy_check_mark: Search form presented on the page  
:heavy_check_mark: Count of Displayed songs and songs from DB are the same  
:heavy_check_mark: Each song has correct title  
:heavy_check_mark: Each song has correct Album name  
:heavy_check_mark: Each song has correct Artist Name  
:heavy_check_mark: Each song has correct Duration

#### TBD Tests ####
:heavy_multiplication_x: Add Song from Albums tab to Playlist  
:heavy_multiplication_x: Add Song from Library tab to Playlist  
:heavy_multiplication_x: Search Songs using Search form by names  
:heavy_multiplication_x: Search Songs using Search form by duration  
:heavy_multiplication_x: Create Playlist from Playlists tab  
:heavy_multiplication_x: Remove Playlist from Playlists tab  
:heavy_multiplication_x: Remove Song from Playlist on Playlists tab