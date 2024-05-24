Here's a possible patch for the code:

```java
import org.cactoos.bytes.CheckedBytes;
import org.cactoos.bytes.IoCheckedBytes;
import org.cactoos.proc.CheckedProc;
import org.cactoos.proc.IoCheckedProc;
import org.cactoos.text.IoCheckedText;
import org.cactoos.text.TextOfScalar;

// ...

public class Wallet {
    // ...

    private void checkBalance(final String id) {
        // ...
        final IoCheckedText balance = IoCheckedText.of(balanceText);
        final TextOfScalar balanceScalar = new TextOfScalar(balance);
        // ...
        final IoCheckedBytes bytes = IoCheckedBytes.of(bytesSupplier.get());
        final CheckedBytes checkedBytes = new CheckedBytes(bytes, new FuncOfBytes());
        // ...
    }

    // ...

    private static class FuncOfBytes implements Func<Bytes, Byte[]> {
        @Override
        public Byte[] apply(final Bytes bytes) {
            return bytes.asBytes();
        }
    }
}
```

This patch replaces the use of `CheckedScalar` with `IoCheckedText`, `TextOfScalar`, and `FuncOfBytes` to read the balance and convert it to bytes. It also uses `IoCheckedBytes` to wrap the `bytesSupplier` result, and adds a `FuncOfBytes` helper class to convert `Bytes` to `Byte[]`.