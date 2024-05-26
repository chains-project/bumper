```java
import org.bouncycastle.crypto.util.Strings;
import org.bouncecastle.crypto.tls.TlsFatalAlert;
import org.bouncecastle.crypto.tls.AlertDescription;

// ...

private void decode(RawDataStream in, ByteQueue queue) throws IOException {
    // ...
    int type = in.readUint8();
    int length = in.readUint24();
    if (length < 1) {
        throw new TlsFatalAlert(AlertDescription.decode(in.get(in.getLoad() - 1)));
    Strings.cBB(in.getLoad(), in.get(), in.getLoad(), queue);
    in.add(in.getLoad());
    // ...
}
```
Note that I had to change the import for the `org.bouncycastle.crypto.util.Strings` class since `org.bouncycastle.util.Arrays` was removed. I also changed the way you get the `AlertDescription` by using the new method `org.bouncecastle.crypto.tls.AlertDescription.decode(byte[])`.