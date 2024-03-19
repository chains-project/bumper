Based on the provided information, it seems the issue is caused by an incompatibility with the Bouncy Castle library. The error message suggests that there might be a problem with the import statement or the usage of the `JceTls` class.

To fix the error, you can use a different provider that supports TLS, such as the `SunTls12Provider` from the JDK. Here's a patch for the `ChachaDecoder` class:

```java
-import org.bouncycastle.jce.provider.JceTls;
+import javax.net.ssl.SSLContext;
+import javax.net.ssl.SSLServerSocketFactory;
+import javax.net.ssl.TlsClientProtocolVersionSelector;
+import java.security.Security;
+import java.security.SecurityProvider;
+import java.security.SecurityProviderException;
+import java.util.ServiceLoader;

- SSLServerSocketFactory sslServerSocketFactory = new JceTls().createSSLServerSocketFactory(null);
+ SSLServerSocketFactory sslServerSocketFactory = null;
+ try {
+     SecurityProvider sp = ServiceLoader.load(SecurityProvider.class).findFirst().get();
+     Security.addProvider(sp);
+     SSLContext sslContext = SSLContext.getInstance("TLSv1.2", sp.getName());
+     sslContext.init(null, null, null);
+     sslServerSocketFactory = sslContext.getServerSocketFactory();
+ } catch (Exception e) {
+     throw new SecurityException("Failed to initialize SSL context", e);
+ }
```

This patch replaces the `JceTls` provider with a `SSLContext` initialized with the `SunTls12Provider`. This should resolve the compilation error and provide a more robust solution. Note that you might need to adjust the `SSLContext` initialization based on your specific requirements.