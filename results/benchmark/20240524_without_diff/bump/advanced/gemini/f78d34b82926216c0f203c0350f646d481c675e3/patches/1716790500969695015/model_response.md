```java
import develop.p2p.lib.WaveCreator;
import org.apache.commons.codec.binary.Base64;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.net.URL;

public class Decorations {

    public static String createImage(String url) throws IOException {
        URL imageUrl = new URL(url);
        BufferedImage image = ImageIO.read(imageUrl);

        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        ImageIO.write(image, "png", baos);
        byte[] imageBytes = baos.toByteArray();

        return Base64.encodeBase64String(imageBytes);
    }

    public static String createWave(String url) throws IOException {
        URL waveUrl = new URL(url);
        WaveCreator waveCreator = new WaveCreator(waveUrl);
        return waveCreator.createWave();
    }
}
```