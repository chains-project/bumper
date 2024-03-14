```java
@Override
protected PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();

    char[] chars = toChars(password);
    try {
        stringEncrypter = new JasyptPBEStringEncryptor();
        stringEncrypter.setPasswordCharArray(chars);

        if (getProviderName() != null && !getProviderName().isEmpty()) {
            stringEncrypter.setProviderName(getProviderName());
        }
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
The error message "cannot find symbol" means that the Java compiler didn't recognize the symbol `StandardPBEStringEncryptor`. It seems that `StandardPBEStringEncryptor` is not available in the current dependency or library. 

I replaced `StandardPBEStringEncryptor` with `JasyptPBEStringEncryptor` assuming that `JasyptPBEStringEncryptor` is available in the current library. Please ensure that `JasyptPBEStringEncryptor` is imported at the beginning of your code.