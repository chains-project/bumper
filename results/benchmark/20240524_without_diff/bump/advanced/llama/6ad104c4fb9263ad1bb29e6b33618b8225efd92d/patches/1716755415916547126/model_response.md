```java
import java.security.Provider;
import java.security.Security;

// ...

Provider bcProvider = Security.getProvider("BC");
if (bcProvider == null) {
    Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());
}
```