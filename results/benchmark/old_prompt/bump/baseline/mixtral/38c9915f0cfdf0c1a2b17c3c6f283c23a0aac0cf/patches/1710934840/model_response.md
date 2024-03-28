It seems like the issue is caused by the import statement that is incorrect. The class `JoinedText` from the library `org.cactoos.text` might not be present in the version of the library that you are using.

Here's a patch that you can apply to the code to fix the error:

```java
import java.util.stream.Collectors;

//...

@Override
public String asString() throws IOException {
    return wallets.stream()
        .map(Wallet::asString)
        .collect(Collectors.joining("\n"));
}
```

In this patch, we're replacing the `JoinedText` class with the `Collectors.joining` method, which is available in Java 8 and later versions. This method concatenates the elements of a stream into a single string, using a delimiter between each element.

Note that this patch assumes that the `wallets` field is a collection of `Wallet` objects, and that the `Wallet` class has an `asString` method that returns a string representation of the wallet. You may need to adjust the code to match the specifics of your application.