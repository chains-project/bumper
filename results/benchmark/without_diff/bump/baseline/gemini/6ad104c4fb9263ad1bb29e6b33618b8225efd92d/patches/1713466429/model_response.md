```java
  import io.github.hapjava.server.impl.crypto.ChachaDecoder;
  import org.bouncycastle.crypto.tls.AlertDescription;

  public class ChachaDecoder {

    public void decode(byte[] in, int inOff, int len) {
      // TODO Auto-generated method stub
    }

    public void setKey(byte[] key, int keyOff, int keyLen) {
      // TODO Auto-generated method stub
    }

    public void setNonce(byte[] nonce, int nonceOff, int nonceLen) {
      // TODO Auto-generated method stub
    }

    public void init(boolean forEncryption) {
      // TODO Auto-generated method stub
    }

    public int getOutputSize(int inputLength) {
      // TODO Auto-generated method stub
      return 0;
    }

    public byte[] process(byte[] in, int inOff, int len) {
      // TODO Auto-generated method stub
      return null;
    }

    public int doFinal(byte[] out, int outOff) {
      // TODO Auto-generated method stub
      return 0;
    }

    public byte[] getMac() {
      // TODO Auto-generated method stub
      return null;
    }

    public void verify(byte[] mac) {
      // TODO Auto-generated method stub
    }

    public void reset() {
      // TODO Auto-generated method stub
    }

    public void close() {
      // TODO Auto-generated method stub
    }

    public AlertDescription getAlertDescription() {
      // TODO Auto-generated method stub
      return null;
    }
  }
```