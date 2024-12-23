```java
import develop.p2p.lib.WaveCreator;

/**
 * A class that creates a wave file.
 */
public class WaveCreator {

    /**
     * Creates a new wave file.
     *
     * @param filename the name of the wave file to create
     * @param sampleRate the sample rate of the wave file
     * @param numChannels the number of channels in the wave file
     * @param bitsPerSample the number of bits per sample in the wave file
     * @throws Exception if an error occurs
     */
    public WaveCreator(String filename, int sampleRate, int numChannels, int bitsPerSample) throws Exception {
        // Create a new wave file.
        WaveFile waveFile = new WaveFile(filename, sampleRate, numChannels, bitsPerSample);

        // Write the wave data to the file.
        writeWaveData(waveFile);

        // Close the wave file.
        waveFile.close();
    }

    /**
     * Writes the wave data to the file.
     *
     * @param waveFile the wave file to write the data to
     * @throws Exception if an error occurs
     */
    private void writeWaveData(WaveFile waveFile) throws Exception {
        // Create a new wave data object.
        WaveData waveData = new WaveData(waveFile.getSampleRate(), waveFile.getNumChannels(), waveFile.getBitsPerSample());

        // Write the wave data to the file.
        waveFile.write(waveData);
    }
}
```