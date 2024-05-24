Here's the proposed patch for the failing client code:

```java
import org.jasypt.password.PBEPasswordEncoder;
import org.jasypt.util.text.TextEncryptor;

@Override
public PBEPasswordEncoder getPasswordEncoder() {
    PBEPasswordEncoder encoder = new PBEPasswordEncoder();
    TextEncryptor textEncryptor = new org.jasypt.util.text.StrongTextEncryptor();
    encoder.setTextEncryptor(textEncryptor);
    return encoder;
}
```

Note that `PBEPasswordEncoder` and `TextEncryptor` are imported from different packages than in the original code. The `encodePassword` method can be used in the same way as before, but you may need to update any tests or other code that relies on the old package names.