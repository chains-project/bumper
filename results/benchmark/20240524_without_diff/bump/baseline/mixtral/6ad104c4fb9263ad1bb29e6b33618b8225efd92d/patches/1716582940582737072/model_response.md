Here's a possible patch for the failing client code:

```java
import org.bouncycastle.crypto.DataLengthException;
import org.bouncycastle.crypto.params.KeyParameter;
import org.bouncycastle.util.Arrays;

import java.io.IOException;
import java.security.SecureRandom;

public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext)
        throws IOException {

    SecureRandom random = new SecureRandom();
    byte[] macKey = new byte[32];
    random.nextBytes(macKey);
    KeyParameter macKeyParam = new KeyParameter(macKey);

    byte[] calculatedMAC = PolyKeyCreator.create(macKeyParam, additionalData, ciphertext);

    if (!Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
        throw new TlsFatalAlert(AlertDescription.bad_record_mac);
    }

    byte[] output = new byte[ciphertext.length];
    // Assuming 'decryptCipher' is an instance variable of the class
    // and it has been initialized with a valid cipher object
    try {
        decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);
    } catch (DataLengthException e) {
        throw new IOException("Failed to decrypt ciphertext", e);
    }

    return output;
}
```

In this patch, I've made the following changes:

* Instead of using a method `initRecordMAC` to initialize the MAC key, I've created a random 32-byte key using `SecureRandom`.
* I've created a `KeyParameter` object from the random key to pass to `PolyKeyCreator.create` method.
* I've added a try-catch block around the call to `decryptCipher.processBytes` to handle `DataLengthException` and wrap it in an `IOException`.

Note that this patch assumes that `decryptCipher` is an instance variable of the class and it has been initialized with a valid cipher object. If this is not the case, you may need to modify the patch accordingly.