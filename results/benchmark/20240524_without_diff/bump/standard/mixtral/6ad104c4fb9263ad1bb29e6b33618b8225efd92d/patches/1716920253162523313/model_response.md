Here's a proposed patch for the client code:

```java
import org.bouncycastle.tls.AlertDescription;
```

Note: The only change made is to replace `org.bouncycastle.crypto.tls` with `org.bouncycastle.tls`. This is because the `AlertDescription` class has been moved from the `crypto.tls` package to the `tls` package in newer versions of the Bouncy Castle library.