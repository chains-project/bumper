Here's a fixed version of the failing method in `ChachaDecoder.java`:

```java
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

import org.bouncycastle.crypto.CipherParameters;
import org.bouncycastle.crypto.StreamCipher;
import org.bouncycastle.crypto.params.ParametersWithIV;
import org.bouncycastle.crypto.params.KeyParameter;
import org.bouncycastle.util.encoders.Hex;

public class ChachaDecoder {
    // ...

    private static final Map<Integer, AlertDescription> alertDescriptions = new HashMap<>();

    static {
        alertDescriptions.put(20, AlertDescription.decode(20));
        alertDescriptions.put(10, AlertDescription.decode(10));
        // ...
    }

    private void decodeAlert(InputStream in) throws IOException {
        int alertLevel = in.read();
        int alertDescription = in.read();
        AlertDescription description = alertDescriptions.get(alertDescription);
        if (description == null) {
            throw new TlsFatalAlert(AlertDescription.illegal_parameter);
        }
        throw new TlsFatalAlert(alertLevel, description);
    }

    // ...
}

class TlsFatalAlert {
    private final short alertLevel;
    private final AlertDescription alertDescription;

    public TlsFatalAlert(short alertLevel, AlertDescription alertDescription) {
        this.alertLevel = alertLevel;
        this.alertDescription = alertDescription;
    }

    public short getAlertLevel() {
        return alertLevel;
    }

    public AlertDescription getAlertDescription() {
        return alertDescription;
    }

    // ...
}

class AlertDescription {
    private final int value;

    private AlertDescription(int value) {
        this.value = value;
    }

    public static AlertDescription decode(int value) {
        return new AlertDescription(value);
    }

    // ...
}
```

The main change here is to replace the removed `TlsFatalAlert` constructor and `getAlertDescription` method with a custom `TlsFatalAlert` class and a custom `AlertDescription` class. The `decodeAlert` method has been updated to use these custom classes.

Note: I assumed that the `AlertDescription` class has a method for decoding the alert description value, but if it doesn't, you might need to add that method yourself.