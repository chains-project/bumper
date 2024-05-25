Here's a patch to fix the error:

```java
import org.jasypt.util.text.StrongTextEncryptor;

@Override
public String encode(String rawPassword) {
    StrongTextEncryptor textEncryptor = new StrongTextEncryptor();
    textEncryptor.setPassword(password);
    return textEncryptor.encrypt(rawPassword);
}
```

Note: This patch replaces the usage of `PBEPasswordEncoder` with `StrongTextEncryptor` from the `org.jasypt.util.text` package. The `encode` method has been updated to use the new encryptor.