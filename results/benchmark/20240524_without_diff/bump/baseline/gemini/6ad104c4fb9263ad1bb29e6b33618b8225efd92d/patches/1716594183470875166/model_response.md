```java
  import org.bouncycastle.crypto.tls.TlsCipher;
  import org.bouncycastle.crypto.tls.TlsContext;
  import org.bouncycastle.crypto.tls.TlsProtocol;

  import java.io.IOException;

  public class ChachaDecoder extends TlsCipher {

    public ChachaDecoder(TlsContext context) {
      super(context);
    }

    @Override
    public byte[] decodeCiphertext(short type, byte[] ciphertext, int offset, int len) throws IOException {
      return super.decodeCiphertext(type, ciphertext, offset, len);
    }

    @Override
    public byte[] encodePlaintext(short type, byte[] plaintext, int offset, int len) throws IOException {
      return super.encodePlaintext(type, plaintext, offset, len);
    }

    @Override
    public int getCiphertextDecodeLimit(int plaintextLimit) {
      return super.getCiphertextDecodeLimit(plaintextLimit);
    }

    @Override
    public int getCiphertextEncodeLimit(int plaintextLimit) {
      return super.getCiphertextEncodeLimit(plaintextLimit);
    }

    @Override
    public int getPlaintextLimit(int ciphertextLimit) {
      return super.getPlaintextLimit(ciphertextLimit);
    }
  }
```