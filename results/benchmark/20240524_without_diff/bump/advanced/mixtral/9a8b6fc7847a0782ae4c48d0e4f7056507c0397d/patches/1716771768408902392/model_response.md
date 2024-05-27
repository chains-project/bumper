Here's the proposed patch:
```java
@Override
protected PasswordEncoder createStringEncoder() {
    PasswordEncoder encoder = new PasswordEncoder();
    encoder.setPasswordEncryptor(new StrongPasswordEncryptor());
    return encoder;
}
```
Note that I've imported the necessary classes for you:
```java
import org.jasypt.spring.security.PasswordEncoder;
import org.jasypt.util.password.StrongPasswordEncryptor;
```
This assumes that the `PasswordEncoder` and `StrongPasswordEncryptor` classes are still available in your project's classpath. If not, you may need to add the appropriate dependencies to your build tool configuration (e.g. Maven or Gradle).