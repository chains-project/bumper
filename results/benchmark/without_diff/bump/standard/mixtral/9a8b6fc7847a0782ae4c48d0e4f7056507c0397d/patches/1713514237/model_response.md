Here's the proposed patch:
```java
@Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = toChars(password);
    try {
        stringEncrypter = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
        stringEncrypter.setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());
        it.geosolutions.geostore.core.security.password.PBEPasswordEncoder encoder = new it.geosolutions.geostore.core.security.password.PBEPasswordEncoder();
        encoder.setPbeStringEncryptor(stringEncrypter);
        return encoder;
    } finally {
        scramble(password);
        scramble(chars);
    }
}

private char[] toChars(byte[] bytes) {
    char[] chars = new char[bytes.length];
    for (int i = 0; i < bytes.length; i++) {
        chars[i] = (char) bytes[i];
    }
    return chars;
}

private void scramble(char[] chars) {
    for (int i = 0; i < chars.length; i++) {
        chars[i] = (char) (chars[i] ^ 0xFF);
    }
}

private void scramble(byte[] bytes) {
    for (int i = 0; i < bytes.length; i++) {
        bytes[i] = (byte) (bytes[i] ^ 0xFF);
    }
}
```
The patch introduces two new helper methods `toChars` and `scramble` that can be used to convert between bytes and chars, and to scramble both byte and char arrays.
This way, the patch avoids using the removed `it.geosolutions.geostore.core.security.password.SecurityUtils` class.
The patch also replaces the `it.geosolutions.geostore.core.security.password.SecurityUtils.toChars` method with the new `toChars` helper method.
Finally, the patch replaces the `it.geosolutions.geostore.core.security.password.SecurityUtils.scramble` method with the new `scramble` helper method.
Note that the `scramble` method uses the bitwise XOR operator `^` to scramble the byte and char arrays, which is equivalent to the original `scramble` method implementation.