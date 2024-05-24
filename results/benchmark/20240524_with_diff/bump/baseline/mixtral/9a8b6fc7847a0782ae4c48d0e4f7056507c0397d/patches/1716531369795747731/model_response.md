Here's the proposed patch for the failing code:

```java
import org.jasypt.PasswordEncoder;
import org.jasypt.encryption.pbe.PBEStringEncryptor;
import org.jasypt.util.text.TextEncryptor;

@Override
public PasswordEncoder passwordEncoder() {
    PBEStringEncryptor encryptor = new PBEStringEncryptor();
    encryptor.setAlgorithm("PBEWithMD5AndTripleDES");
    encryptor.setPassword(password);

    TextEncryptor textEncryptor = new TextEncryptor();
    textEncryptor.setPassword(password);

    PasswordEncoder passwordEncoder = new PasswordEncoder();
    passwordEncoder.setPasswordEncryptor(encryptor);
    passwordEncoder.setTextEncryptor(textEncryptor);

    return passwordEncoder;
}

@Override
public boolean isPasswordValid(String encryptedPassword, String plainTextPassword, Object salt) {
    PasswordEncoder passwordEncoder = passwordEncoder();
    return passwordEncoder.isPasswordValid(encryptedPassword, plainTextPassword, salt);
}

@Override
public String encodePassword(String plainTextPassword, Object salt) {
    PasswordEncoder passwordEncoder = passwordEncoder();
    return passwordEncoder.encodePassword(plainTextPassword, salt);
}
```

In this patch, I created a `PBEStringEncryptor` and `TextEncryptor` object to replace the removed `PBEPasswordEncoder` class. I then created a `PasswordEncoder` object and set its `PasswordEncryptor` and `TextEncryptor` properties to the corresponding objects I created earlier.

I then implemented the `isPasswordValid` and `encodePassword` methods using the new `PasswordEncoder` object.

Note that the `password` variable used in the `passwordEncoder` method is assumed to be defined elsewhere in the class.