Here's the fixed version of the method using the `Joined` class instead of the removed `JoinedText`:

```java
import org.cactoos.text.Joined;

@Override
public String ids() throws IOException {
    return new Joined(",", wallets()).asString();
}
```

The `JoinedText` class has been removed in the new library version, so we use the `Joined` class instead. The `Joined` class provides similar functionality to join multiple strings into one string separated by a specified delimiter. We use it to join the IDs of the wallets separated by a comma.