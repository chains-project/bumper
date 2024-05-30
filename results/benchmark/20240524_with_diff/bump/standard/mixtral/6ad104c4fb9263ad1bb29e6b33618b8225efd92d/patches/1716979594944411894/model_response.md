Here's the fixed method with the required changes:

```java
import java.io.IOException;
import java.util.Objects;

public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext) throws IOException {
    org.bouncycastle.crypto.params.KeyParameter macKey = initRecordMAC(decryptCipher);
    byte[] calculatedMAC = io.github.hapjava.server.impl.crypto.PolyKeyCreator.create(macKey, additionalData, ciphertext);
    if (!org.bouncycastle.util.Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
        throw new RuntimeException("bad_record_mac");
    }
    byte[] output = new byte[ciphertext.length];
    decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);
    return output;
}
```

In this fixed version, the `TlsFatalAlert` class is removed since it is no longer available in the new library version. Instead, a `RuntimeException` is thrown with a custom error message. The `AlertDescription` class is also removed, so the error message is simply a string. The `org.bouncycastle.crypto.tls` package import has been removed since it is not used anymore. The `Objects.requireNonNull` method is not used since it is not essential for the method's functionality.