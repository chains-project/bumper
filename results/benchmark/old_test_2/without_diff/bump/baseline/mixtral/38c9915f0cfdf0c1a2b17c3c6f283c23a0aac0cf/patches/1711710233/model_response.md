Here is a potential patch for the failing code:
```java
import org.cactoos.text.Joined;

// ...

@Override
public Text walletsIn(String address) throws IOException {
  return new Joined("", Arrays.stream(client.walletsIn(address))
    .map(WalletInfo::new)
    .map(WalletInfo::toString)
    .toArray(String[]::new)
  );
}
```
In this patch, I have replaced the `org.cactoos.text.JoinedText` class with the `org.cactoos.text.Joined` class. The `Joined` class provides similar functionality to `JoinedText`, but it allows for a delimiter to be specified between the joined strings. In this case, I have specified an empty string as the delimiter.

Additionally, I have updated the code to use Java 8 streams and lambdas to simplify the code. This allows for the creation of the `Joined` object to be done in a more concise and readable way.

Note that the `client.walletsIn(address)` method is assumed to return an array of `WalletInfo` objects, which is then converted to a string array using the `toString` method of the `WalletInfo` class. If the `toString` method of the `WalletInfo` class does not provide the desired string representation, you may need to modify this code accordingly.