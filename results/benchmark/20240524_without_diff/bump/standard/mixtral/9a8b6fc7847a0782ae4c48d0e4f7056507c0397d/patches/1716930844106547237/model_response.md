Here's a possible patch to fix the issue:

```java
import org.jasypt.util.password.ConfigurablePasswordEncryptor;
import org.jasypt.util.password.StrongPasswordEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.crypto.password.DelegatingPasswordEncoder;
import org.springframework.security.crypto.password.NoOpPasswordEncoder;
import java.util.HashMap;
import java.util.Map;

@java.lang.Override
protected PasswordEncoder createStringEncoder() {
    ConfigurablePasswordEncryptor encryptor = new StrongPasswordEncryptor();
    String idForEncryptor = encryptor.getClass().getName();
    Map<String, PasswordEncoder> encoders = new HashMap<>();
    encoders.put(idForEncryptor, new DelegatingPasswordEncoder(idForEncryptor, encoders) {
        @Override
        public boolean matches(CharSequence rawPassword, String encodedPassword) {
            return encryptor.checkPassword(rawPassword.toString(), encodedPassword);
        }
    });
    encoders.put(NoOpPasswordEncoder.getInstance().getId(), NoOpPasswordEncoder.getInstance());
    return new DelegatingPasswordEncoder(idForEncryptor, encoders);
}
```

This patch uses the `ConfigurablePasswordEncryptor` class from `jasypt` library instead of `StrongPasswordEncryptor`, and creates a `DelegatingPasswordEncoder` that delegates the encoding and matching to the appropriate password encoders based on their IDs. The `NoOpPasswordEncoder` is added to the `encoders` map to avoid the issue of having no password encoder for the ID `null`. The `matches` method is overridden to use the `checkPassword` method of the `ConfigurablePasswordEncryptor` for matching.