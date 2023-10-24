// TODO create VisualSettings to insert visual variables
let colorList = [
    [255, 0, 0],
    [0, 255, 0],
    [0, 0, 255],
    [255, 255, 0],
    [255, 165, 0],
    [128, 0, 128],
    [255, 192, 203],
    [255, 255, 255],
    [0, 0, 0],
    [128, 128, 128],
    [165, 42, 42],
    [0, 255, 255],
    [0, 255, 0],
    [255, 215, 0],
    [192, 192, 192],
    [0, 0, 139],
    [0, 100, 0],
    [139, 0, 0],
    [169, 169, 169],
    [64, 224, 208]
];

let songs = []
let max_num_chords, max_num_words
let range
let x_offset = 20
const WORDS_X_COL = 400;
const CHORDS_X_COL = 680;
let SEL_SONG_X_COL = 900
let y_values_offset = 40
let y_titles_offset = 20

let selSongIndex = 0
function setup() {
    createCanvas(2000, 2400);


    loadData();
}

function draw() {
    background(220);
    range = (height - y_values_offset) / songs.length;
    textSize(range);
    fill(0, 0, 255);
    stroke(0, 0, 255);
    text("SONG", x_offset, y_titles_offset + range / 2);
    text("NUM WORDS", WORDS_X_COL, y_titles_offset + range / 2);
    text("NUM CHORDS", CHORDS_X_COL, y_titles_offset + range / 2);

    stroke(0, 0, 0);
    noFill();

    if (songs.length != 0) {
        for (let i = 0; i < songs.length; i++) {

            if (i == selSongIndex) {
                textStyle('bold');
                // fill(255, 0, 0);
                stroke(255, 0, 0);
            } else {
                textStyle(NORMAL);
                // noFill();
                stroke(0, 0, 0);
            }

            textSize(range);
            text(songs[i].year + " - " + songs[i].artist + " - " + songs[i].song, x_offset, y_values_offset + i * range + range / 2);
            // console.log(songs[i].structure.chords_occurrences)

            rect(WORDS_X_COL, y_values_offset - range / 2 + i * range, map(songs[i].num_words, 0, max_num_words, 0, 200), range);
            textSize(range * 0.8);
            text(songs[i].num_words, WORDS_X_COL, y_values_offset + i * range + range / 2);
            // text(songs[i].num_words, 400, 20 + i * range + range / 2);
            rect(CHORDS_X_COL, y_values_offset - range / 2 + i * range, map(songs[i].num_chords, 0, max_num_chords, 0, 200), range);
            text(songs[i].num_chords, CHORDS_X_COL, y_values_offset + i * range + range / 2);
        }

        let music = songs[selSongIndex].structure.music;
        let bottom_y = ((music.length - 1) * 40) + 80 + y_values_offset + selSongIndex * range + range / 2
        let y_offset = 0;
        if (bottom_y > height) {
            y_offset = 40 + bottom_y - height;
        }

        stroke(0, 0, 0);
        textStyle(NORMAL);
        textSize(15);
        text("TOP WORDS: " + print_occurrences(songs[selSongIndex].structure.words_occurrences, 10), SEL_SONG_X_COL, (y_values_offset + selSongIndex * range + range / 2) - y_offset);
        text("CHORDS: " + print_occurrences(songs[selSongIndex].structure.chords_occurrences), SEL_SONG_X_COL, (40 + y_values_offset + selSongIndex * range + range / 2) - y_offset);

        for (let i = 0; i < music.length; i++) {
            text(music[i].part + ": " + print_occurrences(music[i].chord_progressions), SEL_SONG_X_COL, ((i * 40) + 80 + y_values_offset + selSongIndex * range + range / 2) - y_offset);
        }

    }
}

function loadData() {
    loadJSON('songs_content.json', function (data) {

        songs = data.songs
        max_num_chords = 0
        max_num_words = 0
        for (let i = 0; i < songs.length; i++) {
            let num_chords = songs[i].structure.chords_occurrences.length
            let num_words = songs[i].structure.words_occurrences.length
            if (num_chords > max_num_chords) {
                max_num_chords = num_chords
            }
            if (num_words > max_num_words) {
                max_num_words = num_words
            }
            songs[i].num_chords = num_chords
            songs[i].num_words = num_words
        }


        songs = songs.filter((element, index) => element.num_chords != 0 && element.num_words != 0);

    })
}

function print_occurrences(list, num = null) {
    let res = "";

    for (let i = 0; i < list.length; i++) {

        let text = list[i]
        if (Array.isArray(text)) {
            text = text[0]
        }
        res += text + " ";
        if (num != null && i > num) {
            break
        }
    }
    return res
}


function mousePressed() {
    selSongIndex = Math.floor(((mouseY - y_values_offset + (range / 2)) / range))
    if (selSongIndex < 0) selSongIndex = 0
    console.log(selSongIndex)
}

function keyPressed() {
    if (key === 'R' || key === 'r') {
        saveGif('mySketch', 1);
    }
}