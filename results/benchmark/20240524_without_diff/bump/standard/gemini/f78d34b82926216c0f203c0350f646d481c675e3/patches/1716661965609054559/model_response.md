```java
import com.google.common.io.Files;

import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

public class Decorations {

    public static void main(String[] args) throws IOException {
        File file = new File("wave.wav");
        byte[] bytes = Files.toByteArray(file);
        String wave = new String(bytes, StandardCharsets.UTF_8);
        System.out.println(wave);
    }
}
```