Here's a fixed version of the code that replaces the failing import statement:
```java
import org.jasypt.util.text.BasicTextEncryptor;
```
Note that `PBEPasswordEncoder` has been replaced with `BasicTextEncryptor` from the `org.jasypt.util.text` package. This is because the `org.jasypt.spring.security` package is no longer available and the `PBEPasswordEncoder` class has been removed. The `BasicTextEncryptor` class provides similar functionality and can be used as a drop-in replacement.

Additionally, you may need to modify the code that uses `PBEPasswordEncoder` to use `BasicTextEncryptor` instead. For example, if you were using `PBEPasswordEncoder` to encode a password, you could replace it with the following code:
```java
BasicTextEncryptor textEncryptor = new BasicTextEncryptor();
textEncryptor.setPassword("my-secret-password");
String encryptedPassword = textEncryptor.encrypt("my-plaintext-password");
```
This code creates a new `BasicTextEncryptor` object, sets a password for encryption, and then encrypts a plaintext password. The resulting encrypted password can be stored in a database or other secure location.