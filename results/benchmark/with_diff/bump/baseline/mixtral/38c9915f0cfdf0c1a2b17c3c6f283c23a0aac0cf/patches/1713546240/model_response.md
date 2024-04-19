Here's the fixed version of the failing method using the `Joined` class instead of the removed `JoinedText`:

```java
import org.cactoos.text.Joined;

@Override
public String ids() throws IOException {
    return new Joined(",", wallets()).asString();
}
```

The `JoinedText` class has been removed in the new library version, so we're using the `Joined` class instead. The `Joined` class works similarly to `JoinedText`, but takes an iterable of `CharSequence` instead of a vararg of `String`. We can use the `wallets()` method to get an iterable of wallet names and pass it to the `Joined` constructor. The `asString()` method is then used to convert the joined text into a string.