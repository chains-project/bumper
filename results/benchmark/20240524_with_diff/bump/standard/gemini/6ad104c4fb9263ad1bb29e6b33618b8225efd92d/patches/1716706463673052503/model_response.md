```java
import io.github.hapjava.server.impl.crypto.ChachaDecoder;

public class ChachaDecoderPatch {

    public static void patch() throws Exception {
        Class<?> cls = ChachaDecoder.class;
        Class<?> tlsFatalAlertClass = Class.forName("org.bouncycastle.crypto.tls.TlsFatalAlert");
        cls.getDeclaredMethod("setAlertDescription", tlsFatalAlertClass).setAccessible(true);
    }
}
```