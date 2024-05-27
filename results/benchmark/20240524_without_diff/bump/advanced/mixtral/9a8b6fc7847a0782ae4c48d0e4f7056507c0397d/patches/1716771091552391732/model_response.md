Here's a proposed patch for the client code:
```java
import org.jasypt.util.text.StrongTextEncryptor;

public class GeoStorePBEPasswordEncoder {
    private StrongTextEncryptor encryptor;

    public GeoStorePBEPasswordEncoder() {
        this.encryptor = new StrongTextEncryptor();
        this.encryptor.setAlgorithm("PBEWithMD5AndTripleDES");
    }

    public String encode(String rawPass) {
        return this.encryptor.encrypt(rawPass);
    }

    public boolean matches(String rawPass, String encodedPass) {
        return encodedPass.equals(encryptor.encrypt(rawPass));
    }
}
```
This patch replaces the `org.jasypt.spring.security.PBEPasswordEncoder` class with the `org.jasypt.util.text.StrongTextEncryptor` class from the same library. The `StrongTextEncryptor` class provides similar functionality to the `PBEPasswordEncoder` class, but it is not tied to Spring Security.

Note that the `setAlgorithm` method is used to set the encryption algorithm to be used, as the `StrongTextEncryptor` class does not use a default algorithm.

Additionally, the `matches` method was changed to compare the result of encrypting the raw password with the encoded password directly, instead of comparing the hash of the raw password with the encoded password. This is because the `StrongTextEncryptor` class does not provide a method for comparing the hash of a raw password with an encoded password.