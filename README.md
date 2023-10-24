# SongsAnalyzer

## Project goal

Simple program to automatically retreive songs data (lyrics + guitar chords) and visualize them. The data is scraped from UltimateGuitar.com. The visualization is created using p5.js. The input is a list of song titles.

## Workflow

### Retrieve the link of the pages
***scraper.py*** reads a json containing a list of song names. The format of the input json is:
```json
{
  "Anni 1950-1954": [
    "Goodnight Irene - Gordon Jenkins and The Weavers (1950)",
    "Mona Lisa - Nat King Cole (1950)",
    "Too Young - Nat King Cole (1951)",
    "Blue Tango - Leroy Anderson (1952)"
  ],
  "Anni 1955-1959": [
    "All Shook Up - Elvis Presley (1957)",
    "Wake Up Little Susie - The Everly Brothers (1957)",
    "That'll Be the Day - Buddy Holly (1957)",
    "Great Balls of Fire - Jerry Lee Lewis (1957)",
    "Peggy Sue - Buddy Holly (1957)",
    "At the Hop - Danny & The Juniors (1958)",
...
```

It generates a json containing, for each song, the link of the available pages. The format of the generated json is:
```json
{
    "artists": [       
        {
            "name": "Nat King Cole",
            "songs": [
                {
                    "name": "Mona Lisa",
                    "year": "1950",
                    "links": [
                        "https://tabs.ultimate-guitar.com/tab/nat-king-cole/mona-lisa-chords-1198777",
                        "https://tabs.ultimate-guitar.com/tab/nat-king-cole/mona-lisa-chords-2008363",
                        "https://tabs.ultimate-guitar.com/tab/nat-king-cole/mona-lisa-chords-3509525",
                        "https://tabs.ultimate-guitar.com/tab/nat-king-cole/mona-lisa-chords-3728552"
                    ]
                },
                {
                    "name": "Too Young",
                    "year": "1951",
                    "links": [
                        "https://tabs.ultimate-guitar.com/tab/nat-king-cole/too-young-chords-1015642",
                        "https://tabs.ultimate-guitar.com/tab/nat-king-cole/too-young-chords-3002072",
                        "https://tabs.ultimate-guitar.com/tab/nat-king-cole/too-young-chords-1851000"
                    ]
                }
            ]
        },
        {
            "name": "Leroy Anderson",
            "songs": [
                {
                    "name": "Blue Tango",
                    "year": "1952",
                    "links": []
                }
            ]
        },
...
```

### Retrieve the link of the pages
***song_parser.py*** reads the json generated ***scraper.py*** to generate a json containing the lyrics + chords. The format of the generated json is:
```json
{
    "artists": [       
        {
            "name": "Nat King Cole",
            "songs": [
                {
                    "name": "Mona Lisa",
                    "year": "1950",
                    "links": [
                        "https://tabs.ultimate-guitar.com/tab/nat-king-cole/mona-lisa-chords-1198777",
                        "https://tabs.ultimate-guitar.com/tab/nat-king-cole/mona-lisa-chords-2008363",
                        "https://tabs.ultimate-guitar.com/tab/nat-king-cole/mona-lisa-chords-3509525",
                        "https://tabs.ultimate-guitar.com/tab/nat-king-cole/mona-lisa-chords-3728552"
                    ],
                    "data": [
                        {
                            "song_name": "Mona Lisa",
                            "artist_name": "Nat King Cole",
                            "votes": 129,
                            "rating": 4.7606,
                            "content": "Words &amp; Music by Jay Livingston &amp; Ray Evans\r\nRecorded by Nat \"King\" Cole, 1950 (#1) (Academy award winner, 1950)\r\n\r\n[tab]([ch]Gmaj7[/ch]) [ch]C[/ch]              [ch]F[/ch]        [ch]C[/ch]\r\n Mona Lisa, Mona Lisa men have named you;[/tab]\r\n[tab]                    [ch]C/B[/ch]  [ch]Am7[/ch]     [ch]Am7/G[/ch]    [ch]Dm7[/ch]    [ch]G7[/ch]\r\nYou're so like the lady with the mystic smile.[/tab]\r\n[tab]      [ch]Dm[/ch]                 [ch]Dm7[/ch]            [ch]G7sus4[/ch]   [ch]G7[/ch]\r\nIs it only 'cause you're lonely men have blamed you[/tab]\r\n[tab]        [ch]G[/ch]    [ch]G/A[/ch]   [ch]G/B[/ch]        [ch]G[/ch]        [ch]C[/ch]\r\nFor the Mona Lisa strangeness in your smile?[/tab]\r\n\r\n[tab]        [ch]C6[/ch]       [ch]C[/ch]      [ch]C6[/ch]      [ch]C[/ch]   [ch]F[/ch]  [ch]C[/ch]\r\nDo you smile to tempt a lover, Mona Li-sa,[/tab]\r\n[tab]                         [ch]C7[/ch]            [ch]F[/ch]\r\nOr is this your way to hide a broken heart?[/tab]\r\n[tab]       [ch]Fm[/ch]                              [ch]C[/ch]\r\nMany dreams have been brought to your doorstep;[/tab]\r\n[tab]           [ch]G7[/ch]        [ch]Gmaj7[/ch]        [ch]C[/ch]\r\nThey just lie there,    and they die there.[/tab]\r\n\r\n[tab][ch]C7[/ch]       [ch]F[/ch]             [ch]Fm[/ch]         [ch]C[/ch]\r\nAre you warm, are you real, Mona Lisa,[/tab]\r\n[tab]          [ch]Dm7[/ch]       [ch]G7[/ch]     [ch]Dm7[/ch]    [ch]G7[/ch]       [ch]C[/ch]\r\nOr just a cold and lonely, lovely work of art.[/tab]\r\n\r\n[tab]        [ch]C6[/ch]       [ch]C[/ch]      [ch]C6[/ch]      [ch]C[/ch]   [ch]F[/ch]  [ch]C[/ch]\r\nDo you smile to tempt a lover, Mona Li-sa,[/tab]\r\n[tab]                         [ch]C7[/ch]            [ch]F[/ch]\r\nOr is this your way to hide a broken heart?[/tab]\r\n[tab]       [ch]Fm[/ch]                              [ch]C[/ch]\r\nMany dreams have been brought to your doorstep;[/tab]\r\n[tab]           [ch]G7[/ch]        [ch]Gmaj7[/ch]        [ch]C[/ch]\r\nThey just lie there,    and they die there.[/tab]\r\n\r\n[tab][ch]C7[/ch]       [ch]F[/ch]             [ch]Fm[/ch]         [ch]C[/ch]\r\nAre you warm, are you real, Mona Lisa,[/tab]\r\n[tab]          [ch]Dm7[/ch]       [ch]G7[/ch]     [ch]Dm7[/ch]    [ch]G7[/ch]       [ch]C[/ch]\r\nOr just a cold and lonely, lovely work of art.[/tab]\r\n\r\n[tab]       [ch]Fm[/ch]   [ch]G7[/ch]  [ch]Fm[/ch] [ch]C[/ch]   [ch]C7[/ch] [ch]G7[/ch] [ch]C[/ch]\r\nMona Lisa, Mona Li-sa.[/tab]"
                        },
                        {
                            "song_name": "Mona Lisa",
                            "artist_name": "Nat King Cole",
                            "votes": 17,
                            "rating": 4.82024,
                            "content": "[Chords]\r\nG\u00a0\u00a0 x-5-5-4-3-x\r\nGm\u00a0 x-5-5-3-3-x\r\nUse these 2 shapes rather than those that default in the highlighted chord charts below.\r\n\r\nBelow is a double stop melody piece that can be used as an intro, or solo, to\r\n\"Mona Lisa\".\u00a0 This transcription resolves to the key of D.\u00a0 The original recording is\r\nin Db, but the fingerings can, of course, simply be moved to any position.\u00a0 It's fun to\r\nplay, and with some practice can be achieved fairly easily for a novice/intermediate\r\nlevel player.\u00a0 Some slides and a little finger vibrato make this sing.\r\n\r\n[tab]\u00a0\u00a0 [ch]D[/ch]\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0[ch]G[/ch] \u00a0\u00a0\u00a0\u00a0[ch]D[/ch]\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 [ch]A7[/ch]\r\ne|-5-4-7-5---|-5-4-7-5---|-2---------|-10----9--9-|-7-7-5-5--|-2-3-5-x--|\r\nB|-7-6-8-7---|-7-6-8-7---|-3-3-------|-12---10-10-|-8-8-7-7--|-3-5-7-5--|\r\nG|-----------|-----------|---4-4-2---|------------|----------|-------6--|\r\nD|-----------|-----------|-----5-4---|------------|----------|----------|\r\nA|-----------|-----------|-----------|------------|----------|----------|\r\nE|-----------|-----------|-----------|------------|----------|----------|[/tab]\r\n[tab]\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 [ch]D[/ch]\r\ne}-7-6--9-7--|-----------|-----------|------------|----------|-7-5-3-2--|\r\nB|-8-7-10-8--|-8-7-10-8--|-5-4-7-5---|--------2-3-|-5-7-8----|-9-7-5-3--|\r\nG|-----------|-9-8-11-9--|-6-5-8-6---|-2-4----3-4-|-6-8-9----|----------|\r\nD|-----------|-----------|-----------|-4-6--------|----------|----------|\r\nA|-----------|-----------|-----------|------------|----------|----------|\r\nE|-----------|-----------|-----------|------------|----------|----------|[/tab]\r\n\r\n[Verse 1]\r\n[tab]\u00a0\u00a0\u00a0  [ch]D[/ch]             \u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 [ch]G[/ch]     [ch]D[/ch]\r\nMona Lisa, Mona Lisa men have named you;[/tab]\r\n[tab]                   \u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0[ch]A7[/ch]\r\nYou're so like the lady with the mystic smile.[/tab]\r\nN.C.\r\nIs it only 'cause you're lonely men have blamed you\r\n[tab]     \u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 [ch]D[/ch]  \r\nFor the Mona Lisa strangeness in your smile?[/tab]\r\n\r\n[Verse 2]\r\n[tab]       [ch]D[/ch]     \u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 [ch]G[/ch]\u00a0 [ch]D[/ch]\r\nDo you smile to tempt a lover, Mona Li-sa,[/tab]\r\n[tab]                       [ch]D7[/ch]            [ch]G[/ch]\r\nOr is this the way you hide a broken heart?[/tab]\r\n[tab]     [ch]Gm[/ch] \u00a0                             [ch]D[/ch]\r\nMany dreams have been brought to your doorstep;[/tab]\r\n[tab]          [ch]A7[/ch]       \u00a0\u00a0\u00a0        [ch]D[/ch]\r\nThey just lie there, and they die there.[/tab]\r\n[tab][ch]D7[/ch]      [ch]G[/ch]             [ch]Gm[/ch]         [ch]D[/ch]\r\nAre you warm, are you real, Mona Lisa,[/tab]\r\n[tab]          [ch]A7[/ch]      \u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0        [ch]D[/ch]\r\nOr just a cold and lonely, lovely work of art?[/tab]\r\n\r\n[Solo]\r\n[ch]D[/ch] [ch]G[/ch] [ch]D[/ch] [ch]A7[/ch] [ch]D[/ch]\r\n\r\n[Verse 3]\r\n[tab]       [ch]D[/ch]      \u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 [ch]G[/ch]\u00a0 [ch]D[/ch]\r\nDo you smile to tempt a lover, Mona Li-sa,[/tab]\r\n[tab]                       [ch]D7[/ch]            [ch]G[/ch]\r\nOr is this the way you hide a broken heart?[/tab]\r\n[tab]     [ch]Gm[/ch]                             \u00a0 [ch]D[/ch]\r\nMany dreams have been brought to your doorstep;[/tab]\r\n[tab]          [ch]A7[/ch]       \u00a0\u00a0\u00a0        [ch]D[/ch]\r\nThey just lie there, and they die there.[/tab]\r\n[tab][ch]D7[/ch]      [ch]G[/ch]           \u00a0\u00a0[ch]Gm[/ch]         [ch]D[/ch]\r\nAre you warm, are you real, Mona Lisa,[/tab]\r\n[tab]          [ch]A7[/ch]      \u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0        [ch]D[/ch]\r\nOr just a cold and lonely, lovely work of art?[/tab]\r\n[tab]     [ch]Gm[/ch]  \u00a0\u00a0[ch]A7[/ch] \u00a0 [ch]Gm[/ch] [ch]D[/ch]\r\nMona Lisa, Mona Li-sa.[/tab]\r\n\r\n[tab][Outro]\r\n\u00a0\u00a0 [ch]D[/ch]\r\ne|-2--------|----------| (then close with arpeggiated D chord)\r\nB|-3-3------|----------|\r\nG|---4-4-2--|----------|\r\nD|-----5-4--|-4-2------|\r\nA|----------|-5-4------|\r\nE|----------|----------|[/tab]"
                        },
                    ]
                },
                {
                    "name": "Too Young",
                    "year": "1951",
                    "links": [
                        "https://tabs.ultimate-guitar.com/tab/nat-king-cole/too-young-chords-1015642",
                        "https://tabs.ultimate-guitar.com/tab/nat-king-cole/too-young-chords-3002072",
                        "https://tabs.ultimate-guitar.com/tab/nat-king-cole/too-young-chords-1851000"
                    ],
                    "data": [
                        {
                            "song_name": "Too Young",
                            "artist_name": "Nat King Cole",
                            "votes": 47,
                            "rating": 4.78807,
                            "content": "[Verse]  \r\n[tab]     [ch]A[/ch]      [ch]C#m[/ch]               [ch]F#m[/ch]           [ch]Bm7[/ch]  [ch]E7[/ch]\r\nThey try to tell us we're too young[/tab]\r\n[tab]     [ch]A[/ch]        [ch]C#m[/ch]          [ch]D[/ch]        [ch]F#7[/ch]\r\nToo young to really be in love[/tab]\r\n[tab]      [ch]Bm[/ch]         [ch]Bm7[/ch]    [ch]E7[/ch]\r\nThey say that love's a word[/tab]\r\n[tab]    [ch]Bm7[/ch]              [ch]E7[/ch]\r\nA word we've only heard[/tab]\r\n[tab]      [ch]Bm7[/ch]            [ch]E7[/ch]              [ch]A[/ch]\r\nBut can't begin to know the meaning of[/tab]\r\n\r\n[Verse]\r\n[tab]     [ch]A[/ch]        [ch]C#m[/ch]              [ch]F#m[/ch]         [ch]Bm7[/ch]   [ch]E7[/ch]\r\nAnd yet we're not too young to know[/tab]\r\n[tab]       [ch]A[/ch]        [ch]A7[/ch]                    [ch]D[/ch]\r\nThis love will last though years may go[/tab]\r\n[tab]    [ch]Bm[/ch]        [ch]D[/ch]        [ch]Dm[/ch]     [ch]A[/ch]             [ch]F#7[/ch]\r\nAnd then some day they may recall[/tab]\r\n[tab]        [ch]Bm7[/ch]      [ch]E7[/ch]      [ch]A[/ch]       [ch]F#m[/ch]       [ch]D[/ch]    [ch]E7[/ch]\r\nWe were not too young at all[/tab]\r\n\r\n[Verse]\r\n[tab]      [ch]A[/ch]        [ch]C#m[/ch]               [ch]F#m[/ch]  [ch]Bm7[/ch]   [ch]E7[/ch]\r\nAnd yet we're not too young to know[/tab]\r\n[tab]     [ch]A[/ch]          [ch]A7[/ch]                    [ch]D[/ch]\r\nThis love will last though years may go[/tab]\r\n[tab]      [ch]Bm[/ch]        [ch]D[/ch]       [ch]Dm[/ch]     [ch]A[/ch]       [ch]F#7[/ch]\r\nAnd then some day they may recall[/tab]\r\n[tab]         [ch]Bm7[/ch]       [ch]E7[/ch]       [ch]A[/ch]\r\nWe were not too young at all[/tab]"
                        },
...}
                    ]
                }
            ]
        },
```
### Extract the lyrics, the chords, and other info
***extract_song_data.py*** reads the json generated ***song_parser.py*** to generate a json containing the information about lyrics, the chords, the song structure, etc. The format of the generated json is:
```json
{
    "songs": [       
       {
            "artist": "DaBaby",
            "song": "Rockstar",
            "year": "2020",
            "structure": {
                "structure": [
                    "Intro",
                    "Chorus",
                    "Verse 1",
                    "Chorus",
                    "Verse 2",
                    "Chorus"
                ],
                "music": [
                    {
                        "part": "Intro",
                        "chord_progressions": [
                            "G#m",
                            "B",
                            "F#",
                            ...
                        ]
                    },
                    {
                        "part": "Chorus",
                        "chord_progressions": [
                            "G#m",
                            "B",
                            "F#",
                            ...
                        ]
                    },
                    {
                        "part": "Verse 1",
                        "chord_progressions": [
                            "B",
                            "F#",
                            "E",
                            ...
                        ]
                    },
                    {
                        "part": "Chorus",
                        "chord_progressions": [
                            "G#m",
                            "B",
                            "F#",
                            ...
                        ]
                    },
                    {
                        "part": "Verse 2",
                        "chord_progressions": [
                            "B",
                            "F#",
                            "E",
                            ...
                        ]
                    },
                    {
                        "part": "Chorus",
                        "chord_progressions": [
                            "G#m",
                            "B",
                            "F#",
                            ...
                        ]
                    }
                ],
                "lyrics": " Woo, woo Woo, woo I pull up like How you pull up, Baby? How you pull up? (Oh, oh, oh) How you pull up? I pull up (Woo, Seth in the kitchen) Let's go Brand new Lamborghini, fuck a cop car With the pistol on my hip like I'm a cop (Yeah, yeah, yeah) Have you ever met a real nigga rockstar? This ain't no guitar, bitch, this a Glock (Woo) My Glock told me to promise you gon' squeeze me (Woo) You better let me go the day you need me (Woo) Soon as you up me on that nigga, get to bustin' (Woo) And if I ain't enough, go get the chop It's safe to say I earned it, ain't a nigga gave me nothin' (Yeah, yeah, yeah) I'm ready to hop out on a nigga, get to bustin' Know you heard me say, \"You play, you lay,\" don't make me push the button Full of pain, dropped enough tears to fill up a fuckin' bucket Goin' for buckets, I bought a chopper I got a big drum, it hold a hundred, ain't goin' for nothin' I'm ready to air it out on all these niggas, I can see 'em runnin' Just talked to my mama, she hit me on FaceTime just to check up on me and my brother I'm really the baby, she know that her youngest son was always guaranteed to get the money She know that her baby boy was always guaranteed to get the loot She know what I do, she know 'fore I run from a nigga, I'ma pull it out and shoot (Boom) PTSD, I'm always waking up in cold sweats like I got the flu My daughter a G, she saw me kill a nigga in front of her before the age of two And I'll kill another nigga too 'Fore I let another nigga do somethin' to you Long as you know that, don't let nobody tell you different Daddy love you (Yeah, yeah) Let's go Brand new Lamborghini, fuck a cop car With the pistol on my hip like I'm a cop (Yeah, yeah, yeah) Have you ever met a real nigga rockstar? This ain't no guitar, bitch, this a Glock (Woo) My Glock told me to promise you gon' squeeze me (Woo) You better let me go the day you need me (Woo) Soon as you up me on that nigga, get to bustin' (Woo) And if I ain't enough, go get the chop Keep a Glocky when I ride in the Suburban 'Cause the codeine had a young nigga swervin' I got the mop, watch me wash 'em like detergent And I'm ballin', that's why it's diamonds on my jersey Slide on opps' side and flip the block back, yeah, yeah My junior popped him and left him lopsided, yeah, yeah We spin his block, got the rebound, Dennis Rodman Fool me one time, you can't cross me again Twelve hundred horsepower, I get lost in the wind If he talkin' on the yard, the pen' dogs'll take his chin Maybach SUV for my refugees Buy blocks in the hood, put money in the streets I was solo when the opps caught me at the gas station Had it on me, thirty thousand, thought it was my last day But they ain't even want no smoke If I had to choose it, murder what she wrote Let's go Brand new Lamborghini, fuck a cop car With the pistol on my hip like I'm a cop (Yeah, yeah, yeah) Have you ever met a real nigga rockstar? This ain't no guitar, bitch, this a Glock (Woo) My Glock told me to promise you gon' squeeze me (Woo) You better let me go the day you need me (Woo) Soon as you up me on that nigga, get to bustin' (Woo) And if I ain't enough, go get the chop ",
                "words_occurrences": [
                    [
                        "woo",
                        17
                    ],
                    [
                        "nigga",
                        13
                    ],
                    [
                        "go",
                        9
                    ]...
                ],
                "chords_occurrences": [
                    [
                        "G#m",
                        33
                    ],
                    [
                        "B",
                        32
                    ],
                    [
                        "F#",
                        32
                    ],
                    [
                        "E",
                        32
                    ]
                ]
            }
        },
```

# Visualize the data
The songs are ordered by date. For each song it's possible to see the number of words contained in the lyrics, the number of chords used, the structure of the song with the chord progression. 

## Next Steps
