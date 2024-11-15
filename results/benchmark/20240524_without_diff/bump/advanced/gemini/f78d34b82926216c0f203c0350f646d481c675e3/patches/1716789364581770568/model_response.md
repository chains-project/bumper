```java
import develop.p2p.lib.WaveCreator;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import javax.sound.sampled.AudioFileFormat;
import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.DataLine;
import javax.sound.sampled.TargetDataLine;

public class Decorations {

    public static void main(String[] args) throws Exception {
        AudioFormat format = new AudioFormat(44100.0f, 16, 2, true, false);
        DataLine.Info info = new DataLine.Info(TargetDataLine.class, format);
        TargetDataLine line = (TargetDataLine) AudioSystem.getLine(info);
        line.open(format);
        line.start();
        AudioInputStream ais = new AudioInputStream(line);
        File wavFile = new File("output.wav");
        AudioSystem.write(ais, AudioFileFormat.Type.WAVE, wavFile);
        line.stop();
        line.close();
        List<String> lines = Files.readAllLines(Paths.get("output.wav"));
        List<String> newLines = lines.stream().map(line -> line.replace("RIFF", "WAVE")).collect(Collectors.toList());
        Files.write(Paths.get("output.wav"), newLines);
        WaveCreator.createWaveFile(new File("output.wav"), new File("output.mp3"));
    }
}
```