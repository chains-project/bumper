It appears that the package `org.bouncycastle.crypto.tls` is no longer available in the newer version of the library. Unfortunately, without knowing the exact use of `AlertDescription` in your code, it's hard to provide a precise solution. 

However, a general approach to solve this issue would be to replace the deprecated package with a new one that provides similar functionality. 

For example, if `AlertDescription` was used to manage TLS Alert messages, you might replace it with something from the `org.bouncycastle.tls` package which is available in the newer versions of the BouncyCastle library. Here's a sample code:

```java
import org.bouncycastle.tls.AlertDescription;
```