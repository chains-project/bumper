Here is a proposed patch for the failing client code:
```java
import org.bouncycastle.crypto.engines.ChaChaEngine;
import org.bouncycastle.crypto.params.KeyParameter;
import org.bouncycastle.crypto.params.ParametersWithIV;

public class ChachaDecoder {
    // existing code...

    private void decode(byte[] input, byte[] output) throws TlsFatalAlert {
        ChaChaEngine engine = new ChaChaEngine();
        engine.init(true, new KeyParameter(key.getOctets()));
        engine.processBlock(iv, 0, null, 0, 12);
        engine.processBytes(input, 0, input.length, output, 0);
    }

    // existing code...
}
```
Note that I replaced the import statement with a new one that imports the `ChaChaEngine` class from the `org.bouncycastle.crypto.engines` package. I also updated the `decode` method to use the `ChaChaEngine` class instead of the `TlsFatalAlert` class.

Additionally, I added the necessary imports for the `KeyParameter` and `ParametersWithIV` classes from the `org.bouncycastle.crypto.params` package.

Finally, I removed the unused `TlsFatalAlert` import statement.