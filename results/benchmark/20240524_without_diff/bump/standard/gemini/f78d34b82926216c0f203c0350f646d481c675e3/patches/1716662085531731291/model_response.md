```java
import develop.p2p.lib.WaveCreator;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Decorations {

    public static void main(String[] args) throws IOException {
        // Create a new WaveCreator object.
        WaveCreator waveCreator = new WaveCreator();

        // Create a new list of files to add to the wave file.
        List<File> files = new ArrayList<>();

        // Add the first file to the list.
        files.add(new File("C:\\Users\\Public\\Documents\\SoundRecorder\\1.wav"));

        // Add the second file to the list.
        files.add(new File("C:\\Users\\Public\\Documents\\SoundRecorder\\2.wav"));

        // Create a new wave file.
        waveCreator.createWaveFile(new File("C:\\Users\\Public\\Documents\\SoundRecorder\\output.wav"), files);

        // Print a message to the console.
        System.out.println("Wave file created successfully.");
    }
}
```