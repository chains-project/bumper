```java
import develop.p2p.lib.WaveCreator;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

public class Decorations {

    public static void main(String[] args) throws IOException {
        // Create a new WaveCreator object.
        WaveCreator waveCreator = new WaveCreator();

        // Create a new File object for the output wave file.
        File outputFile = new File("output.wav");

        // Create a new ArrayList to store the wave data.
        List<Short> waveData = new ArrayList<>();

        // Add some sample wave data to the ArrayList.
        for (int i = 0; i < 1000; i++) {
            waveData.add((short) (Math.sin(i) * 32767));
        }

        // Write the wave data to the output wave file.
        waveCreator.writeWaveFile(outputFile, waveData);

        // Print a message to the console.
        System.out.println("Wave file written to: " + outputFile.getAbsolutePath());
    }
}
```