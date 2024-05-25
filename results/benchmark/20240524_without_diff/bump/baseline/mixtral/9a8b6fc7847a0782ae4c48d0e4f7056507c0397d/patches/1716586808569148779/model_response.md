Here is a potential fix for the issue:
```java
import org.jasypt.util.text.TextEncryptor;
import org.jasypt.util.text.SimpleTextEncryptor;

@Override
protected PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();

    char[] chars = toChars(password);
    try {
        TextEncryptor textEncryptor = new SimpleTextEncryptor();
        textEncryptor.setPasswordCharArray(chars);

        if (getProviderName() != null && !getProviderName().isEmpty()) {
            textEncryptor.setAlgorithm(getAlgorithm() + "-" + getProviderName());
        } else {
            textEncryptor.setAlgorithm(getAlgorithm());
        }

        PBEPasswordEncoder encoder = new PBEPasswordEncoder();
        encoder.setPbeStringEncryptor(textEncryptor);

        return encoder;
    } finally {
        scramble(password);
        scramble(chars);
    }
}
```
In this fix, we replace the `StandardPBEStringEncryptor` class with `SimpleTextEncryptor` from the `org.jasypt.util.text` package. This class provides similar functionality to `StandardPBEStringEncryptor`, but it does not depend on the `Cipher` class from the `javax.crypto` package, which may be causing the compilation error.

We also modify the way the algorithm is set for the `textEncryptor` object. Instead of setting the provider name and algorithm separately, we set the algorithm to be a combination of the algorithm name and provider name (if provided), or just the algorithm name if no provider name is provided. This ensures that the algorithm is set correctly even if the `getProviderName()` method returns an empty string.

Note that this fix assumes that the `scramble()` method and the other helper methods (`lookupPasswordFromKeyStore()` and `toChars()`) are defined elsewhere in the code and are not causing the compilation error.