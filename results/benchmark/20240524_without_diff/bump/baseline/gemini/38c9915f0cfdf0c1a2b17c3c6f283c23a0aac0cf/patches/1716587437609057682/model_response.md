```java
import org.cactoos.iterable.LengthOf;
import java.util.Arrays;

public class RtTransaction {

    public RtTransaction(byte[] bytes) {
        this.bytes = bytes;
    }

    public byte[] getBytes() {
        return bytes;
    }

    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        RtTransaction that = (RtTransaction) o;
        return Arrays.equals(bytes, that.bytes);
    }

    public int hashCode() {
        return Arrays.hashCode(bytes);
    }

    public String toString() {
        return "RtTransaction{" +
                "bytes=" + Arrays.toString(bytes) +
                '}';
    }

    private final byte[] bytes;
}
```