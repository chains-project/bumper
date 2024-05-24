```java
  import org.bouncycastle.crypto.tls.AlertDescription;

  public class ChachaDecoder {

    public void decodeChacha20Poly1305(byte[] buf, int off, int len) {
      // TODO Auto-generated method stub

      // Check if the buffer is large enough to hold the ChaCha20Poly1305 ciphertext.
      if (buf.length < off + len) {
        throw new IllegalArgumentException("Buffer too small");
      }

      // Create a new ChaCha20Poly1305 cipher.
      ChaCha20Poly1305 cipher = new ChaCha20Poly1305();

      // Initialize the cipher with the key and nonce.
      cipher.init(new KeyParameter(key), new IvParameterSpec(nonce));

      // Decrypt the ciphertext.
      cipher.update(buf, off, len);
      cipher.doFinal(buf, off);
    }

    public byte[] getMac() {
      // TODO Auto-generated method stub
      return mac;
    }
  }
```