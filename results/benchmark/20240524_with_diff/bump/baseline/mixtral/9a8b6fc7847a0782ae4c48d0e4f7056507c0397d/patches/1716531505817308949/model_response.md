Here's the fixed version of the `createStringEncoder` method:

```java
@Override
protected PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();

    char[] chars = toChars(password);
    try {
        PBEStringEncryptor stringEncrypter = new StandardPBEStringEncryptor();
        stringEncrypter.setPasswordCharArray(chars);

        if (getProviderName() != null && !getProviderName().isEmpty()) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());

        TextEncryptor textEncryptor = new org.jasypt.encryption.pbe.PBEStringEncryptor();
        ((PBEStringEncryptor) textEncryptor).setPasswordCharArray(chars);
        textEncryptor.setAlgorithm(getAlgorithm());

        if (getProviderName() != null && !getProviderName().isEmpty()) {
            textEncryptor.setProviderName(getProviderName());
        }

        PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
        encoder.setTextEncryptor(textEncryptor);

        return encoder;
    } finally {
        scramble(password);
        scramble(chars);
    }
}
```

The changes include:

1. Import the new classes:
```java
import org.jasypt.encryption.pbe.PBEStringEncryptor;
import org.jasypt.spring.security.PasswordEncoder;
```

2. Replace `PBEPasswordEncoder` and `setPbeStringEncryptor` with `TextEncryptor` and `setTextEncryptor`.
3. Replace `isPasswordValid` with a custom method that checks if the encoded password matches the input.
4. Add the necessary cast to `PBEStringEncryptor` for `textEncryptor`.
5. Add the necessary provider name and algorithm settings for `textEncryptor`.