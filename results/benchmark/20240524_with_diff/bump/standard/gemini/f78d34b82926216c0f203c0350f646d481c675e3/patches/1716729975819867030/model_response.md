```java
import develop.p2p.lib.WaveCreator;

import tokyo.peya.lib.bukkit.exception.SelectorInvalidException;
import tokyo.peya.lib.FileConfiguration;

import java.util.Map;

public class Decorations {

    public static WaveCreator getWaveCreator(double amplitude, double frequency, double phase) {
        return new WaveCreator(amplitude, frequency, phase);
    }

    public static double getWave(double position, boolean isStatic) {
        return WaveCreator.get(position, isStatic);
    }

    public static double getStaticWave() {
        return WaveCreator.getStatic();
    }

    public static Map<String, Object> getInvalidKeys() {
        return SelectorInvalidException.getInvalidKeys();
    }

    public static String convertLeet(String text) {
        return tokyo.peya.lib.LeetConverter.convert(text);
    }

    public static String convertTime(String[] time) {
        return tokyo.peya.lib.TimeParser.convert(time);
    }

    public static String convertTime(java.util.Date time) {
        return tokyo.peya.lib.TimeParser.convertFromDate(time);
    }

    public static double sigmoid(double value) {
        return tokyo.peya.lib.LearnMath.sigmoid(value);
    }

    public static double sigmoidDef(double value) {
        return tokyo.peya.lib.LearnMath.sigmoidDef(value);
    }

    public static String getString(String path) {
        return tokyo.peya.lib.FileConfiguration.getString(path);
    }

    public static Object get(String path) {
        return tokyo.peya.lib.FileConfiguration.get(path);
    }

    public static Map<String, Object> getConfig() {
        return tokyo.peya.lib.FileConfiguration.getConfig();
    }
}
```