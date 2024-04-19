Here's a fixed version of the client code that replaces the failing import statement:
```java
import org.bouncycastle.crypto.engines.ChaChaEngine;

// Replace any usage of AlertDescription with a custom enum or constant
public class ChachaDecoder {
    // ...
}
```
Note that I replaced the failing import statement with a valid import statement that imports the `ChaChaEngine` class from the Bouncy Castle library. I also added a comment suggesting that you replace any usage of `AlertDescription` with a custom enum or constant, as it is not available in the new import.

Please note that this solution assumes that you don't need any other classes from the `org.bouncycastle.crypto.tls` package. If you do need other classes from this package, you may need to find an alternative way to resolve the dependency issue.