Here is the proposed patch for the `GeoStoreDigestPasswordEncoder.java` file:

```java
import org.jasypt.util.password.BasicPasswordEncryptor;
import org.jasypt.util.text.TextEncryptor;
import org.jasypt.util.text.TextEncryptorFactory;

// ...

private TextEncryptor textEncryptor = TextEncryptorFactory.createTextEncryptor();
private BasicPasswordEncryptor passwordEncryptor = new BasicPasswordEncryptor();

// ...

@Override
public String encodePassword(String rawPass, Object salt) {
    return passwordEncryptor.encryptPassword(rawPass, getPasswordSalt(salt));
}

@Override
public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
    return passwordEncryptor.checkPassword(rawPass, encPass);
}

private String getPasswordSalt(Object salt) {
    if (salt == null) {
        return "";
    }
    return textEncryptor.decrypt(salt.toString());
}
```

The changes include replacing the deprecated `PBEPasswordEncoder` with `BasicPasswordEncryptor` for encoding and checking the password. Also, the `TextEncryptor` is used for decrypting the salt from the database.

This patch assumes that the `salt` parameter in the `encodePassword` and `isPasswordValid` methods is a string representation of the encrypted salt. If the salt is stored in a different format, you may need to modify the `getPasswordSalt` method accordingly.