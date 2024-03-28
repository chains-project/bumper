It seems like the package `org.bouncycastle.crypto.tls` does not exist anymore. If the functionality you are trying to use has been moved to a different package, you need to change the import statement to reflect the new package path. If the `AlertDescription` class is now in the `org.bouncycastle.tls` package, the updated code would look like this:

```java
import org.bouncycastle.tls.AlertDescription;
```