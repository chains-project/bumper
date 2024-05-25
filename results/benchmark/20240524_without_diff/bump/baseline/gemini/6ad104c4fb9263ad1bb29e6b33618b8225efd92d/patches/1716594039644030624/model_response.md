```java
  import org.bouncycastle.crypto.tls.AlertDescription;
  import org.bouncycastle.crypto.tls.TlsFatalAlert;

  import java.io.IOException;
  import java.nio.ByteBuffer;

  public class ChachaDecoder {

    private final int keyLength;
    private final int nonceLength;

    public ChachaDecoder(int keyLength, int nonceLength) {
      this.keyLength = keyLength;
      this.nonceLength = nonceLength;
    }

    public byte[] decode(byte[] ciphertext, byte[] additionalData) throws IOException {
      if (ciphertext.length < nonceLength + keyLength) {
        throw new TlsFatalAlert(AlertDescription.decode_error);
      }

      byte[] nonce = new byte[nonceLength];
      System.arraycopy(ciphertext, 0, nonce, 0, nonceLength);

      byte[] key = new byte[keyLength];
      System.arraycopy(ciphertext, nonceLength, key, 0, keyLength);

      byte[] plaintext = new byte[ciphertext.length - nonceLength - keyLength];
      System.arraycopy(ciphertext, nonceLength + keyLength, plaintext, 0, plaintext.length);

      // TODO: Implement ChaCha20 decryption using the provided key and nonce.
      // The additionalData parameter can be used for Poly1305 authentication.

      return plaintext;
    }
  }
```