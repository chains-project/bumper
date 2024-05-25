Here is a proposed patch for the failing client code:

```java
import org.bouncycastle.jce.provider.BouncyCastleProvider;

@Override
protected PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();

    char[] chars = toChars(password);
    try {
        if (getProviderName() != null && !getProviderName().isEmpty()) {
            Security.addProvider(new BouncyCastleProvider());
        }
        stringEncrypter = new StandardPBEStringEncryptor();
        stringEncrypter.setPasswordCharArray(chars);

        stringEncrypter.setAlgorithm(getAlgorithm());

        PBEPasswordEncoder encoder = new PBEPasswordEncoder();
        encoder.setPbeStringEncryptor(stringEncrypter);

        return encoder;
    } finally {
        scramble(password);
        scramble(chars);
    }
}
```

The patch adds the BouncyCastleProvider to the security providers if the provider name is not null and not empty. This should fix the "cannot find symbol" error.

Note that the `setProviderName()` method has been removed as it is not needed with the addition of the BouncyCastleProvider.