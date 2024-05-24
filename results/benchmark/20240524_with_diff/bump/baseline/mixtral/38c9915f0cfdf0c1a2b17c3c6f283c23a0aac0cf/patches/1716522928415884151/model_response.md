Here's a possible patch for the client code:
```java
import org.cactoos.text.BytesOf;
import org.cactoos.text.Split;

...

public class Wallet {
    ...
    @Override
    public void save(final String fileName, final String text) {
        try (final TextIo io = new TextIo(fileName)) {
            final Split split = new Split(System.lineSeparator(), new BytesOf(text));
            for (final String line : split) {
                io.write(line);
            }
        } catch (IOException ex) {
            throw new WalletException("Can't save to file: " + fileName, ex);
        }
    }
    ...
}
```
In this patch, the `SplitText` class is replaced with a new `Split` class that takes a delimiter and a `BytesOf` object as arguments. The `BytesOf` class is a new class in the updated library that converts a `Text` object to a `Bytes` object.

The `BytesOf` class can be used to convert the `text` argument to bytes, and then the `Split` class can be used to split the bytes by the system line separator. This allows the rest of the code to remain unchanged.