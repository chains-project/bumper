Here's the fixed `decodeCiphertext` method using a different package for the `TlsFatalAlert` class:

```java
import de.rayski.util.tls.TlsFatalAlert;

public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext) throws java.io.IOException {
    org.bouncycastle.crypto.params.KeyParameter macKey = initRecordMAC(decryptCipher);
    byte[] calculatedMAC = io.github.hapjava.server.impl.crypto.PolyKeyCreator.create(macKey, additionalData, ciphertext);
    if (!org.bouncycastle.util.Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
        throw new de.rayski.util.tls.TlsFatalAlert(org.bouncycastle.crypto.tls.AlertDescription.bad_record_mac);
    }
    byte[] output = new byte[ciphertext.length];
    decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);
    return output;
}
```

In this example, I replaced the non-existing package `org.bouncycastle.crypto.tls` with `de.rayski.util.tls`. This should resolve the compilation error. Please make sure that the `de.rayski.util.tls.TlsFatalAlert` class is available in your project's classpath.