```java
import develop.p2p.lib.WaveCreator;

// Check if WaveCreator is available in the classpath
try {
    Class.forName("develop.p2p.lib.WaveCreator");
} catch (ClassNotFoundException e) {
    System.out.println("WaveCreator is not found in the classpath");
}
```