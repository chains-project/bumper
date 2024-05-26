Here'ed a possible patch for the client code:
```java
import org.bouncycastle.util.Arrays;
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.AlertDescription;

// ...

public void someMethod() {
  // ...
  AlertDescription desc = new TlsFatalAlert(shortValue).getAlertDescription();
  // ...
}
```
This code imports the new classes and enum necessary to replace the removed method, and uses them to achieve the same functionality.