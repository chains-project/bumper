Here's the proposed patch to fix the error:

```java
import org.bouncycastle.crypto.tls.AlertDescription;

public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext) throws java.io.IOException {
    org.bouncycastle.crypto.params.KeyParameter macKey = initRecordMAC(decryptCipher);
    byte[] calculatedMAC = io.github.hapjava.server.impl.crypto.PolyKeyCreator.create(macKey, additionalData, ciphertext);
    if (!org.bouncycastle.util.Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
        throw new org.bouncycastle.crypto.tls.TlsFatalAlert(new AlertDescription(7));
    }
    byte[] output = new byte[ciphertext.length];
    decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);
    return output;
}
```

The changes made in this patch are:

* Importing the `AlertDescription` class from the `org.bouncycastle.crypto.tls` package.
* Creating a new `AlertDescription` object with the value of `7` to replace the removed constructor of `TlsFatalAlert`.
* Using the `new` keyword to create a new instance of `AlertDescription`.
* Calling the constructor of `TlsFatalAlert` with the new `AlertDescription` object.

Note that the `AlertDescription` enum has a predefined constant for `bad_record_mac` with the value of `7`, so we pass `7` as the argument to the constructor of `AlertDescription`.