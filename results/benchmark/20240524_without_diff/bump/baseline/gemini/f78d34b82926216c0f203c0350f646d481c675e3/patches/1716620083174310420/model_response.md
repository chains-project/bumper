```java
import develop.p2p.lib.WaveCreator;

public class Decorations {

    public void createWave(String path, String title, String artist, String album, String genre, String year, String track, String comment) {
        WaveCreator waveCreator = new WaveCreator();
        waveCreator.createWave(path, title, artist, album, genre, year, track, comment);
    }
}
```