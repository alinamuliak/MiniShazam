# MiniShazam

## About The Project
This is the semester project for LA course at UCU with signal processing as the general topic. MiniShazam(change later) is a simplified version of a query-by-humming (QBH) system. The developed framework takes in a piece of a hummed or whistled song as an input parameter for a search system and outputs the matching song in its full version.

The user can hum a piece of tune into a microphone of his computer or laptop for arbitrary number of seconds (we recommend 8). The program will perform necessary evaluation and search a database of tunes to find a list of melodies that are most similar to the user’s “query”. Then he/she will be able to listen to this result to see if it is actually the tune that he/she had in mind. If the recording has drastically different tempo, the user will be asked to hum again, this time more accurately. 

The database of tunes can be extended by manually adding new songs. If the user hums or whistles a piece that is not yet in the database, the system, apparently, will not be able to return the exact match. 

### Built With

* [Python](https://www.python.org/)
* [Essentia](https://essentia.upf.edu/)
* [SciPy](https://scipy.org/)
* 


## Getting Started

### Prerequisites
* essentia
    ```shell
    pip install essentia
    ```
* mir_eval
    ```shell
    pip install mir_eval
    ```
* pydub
    ```shell
    pip install pydub
    ```


### Installation

1. Clone the repo
2. ...


## Usage



## Roadmap

- [x] Implement pitch detection algorithm
- [x] Implement real-time recording
- [ ] Implement matching algorithm
- [ ] Test the program
  - [ ] Test on the bad quality input
  - [ ] Test on the input that is absent in the database
    

## Contributors
- [Alina Muliak](https://github.com/alinamuliak)
- [Vira Saliieva](https://github.com/vsaliievaa)
