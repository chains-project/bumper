Here's a possible patch for the code that removes the dependency on `org.bouncycastle.crypto.tls`:

```java
import java.security.NoSuchAlgorithmException;
import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;

public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext) throws IOException {
    org.bouncycastle.crypto.params.KeyParameter macKey = initRecordMAC(decryptCipher);
    byte[] calculatedMAC = io.github.hapjava.server.impl.crypto.PolyKeyCreator.create(macKey, additionalData, ciphertext);
    if (!org.bouncycastle.util.Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
        throw new RuntimeException("Bad MAC");
    }
    byte[] output = new byte[ciphertext.length];
    try {
        Cipher cipher = Cipher.getInstance("ChaCHa20-Poly1305");
        cipher.init(Cipher.DECRYPT_MODE, macKey);
        cipher.update(ciphertext, 0, ciphertext.length, output, 0);
        cipher.doFinal();
    } catch (NoSuchAlgorithmException | NoSuchPaddingException | IllegalBlockSizeException | BadPaddingException e) {
        throw new IOException(e);
    }
    return output;
}
```

This patch replaces the `org.bouncycastle.crypto.tls.TlsFatalAlert` exception with a `RuntimeException`, and uses the `javax.crypto` package to perform the decryption instead of `org.bouncycastle.crypto`. Note that this patch assumes that the `decryptCipher` variable is an instance of `org.bouncycastle.crypto.Cipher` that has been initialized with the correct key and IV.