Here's the proposed patch:

```java
import org.jasypt.spring.security.PasswordEncoder;
import org.jasypt.util.text.TextEncryptor;
import org.jasypt.util.text.AesTextEncryptor;

@Override
protected PasswordEncoder createStringEncoder() {
    TextEncryptor textEncryptor = new AesTextEncryptor();
    textEncryptor.setPassword("your-secret-password");
    PasswordEncoder encoder = new PasswordEncoder();
    encoder.setTextEncryptor(textEncryptor);
    return encoder;
}
```

In this patch, I replaced the removed `PBEPasswordEncoder` with the new `PasswordEncoder` class, and used the new `setTextEncryptor` method to set the encryption algorithm. I also added the necessary imports. Note that you need to replace `"your-secret-password"` with your own secret password.