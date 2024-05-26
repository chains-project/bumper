Here is the proposed patch for the failing client code:

```java
import org.jasypt.util.password.BasicPasswordEncryptor;
import org.jasypt.util.text.TextEncryptor;
import org.jasypt.encryption.pbe.PBEStringEncryptor;
import org.jasypt.digest.StandardStringDigester;

//...

public class GeoStoreDigestPasswordEncoder {

    private TextEncryptor textEncryptor;
    private PasswordEncryptor passwordEncryptor;
    private StandardStringDigester stringDigester;
    private PBEStringEncryptor pbeStringEncryptor;

    //...

    public GeoStoreDigestPasswordEncoder() {
        this.textEncryptor = new org.jasypt.util.text.BasicTextEncryptor();
        this.passwordEncryptor = new BasicPasswordEncryptor();
        this.stringDigester = new StandardStringDigester();
        this.pbeStringEncryptor = new PBEStringEncryptor();
    }

    //...

    public String encodePassword(String rawpass, Object salt) {
        return this.passwordEncryptor.encryptPassword(rawpass);
    }

    //...

    public boolean isPasswordValid(String encpass, String rawpass, Object salt) {
        return this.passwordEncryptor.checkPassword(rawpass, encpass);
    }

    //...

    public void setTextEncryptor(TextEncryptor textEncryptor) {
        this.textEncryptor = textEncryptor;
    }

    public void setPasswordEncryptor(PasswordEncryptor passwordEncryptor) {
        this.passwordEncryptor = passwordEncryptor;
    }

    public void setStringDigester(StandardStringDigester stringDigester) {
        this.stringDigester = stringDigester;
    }

    public void setPbeStringEncryptor(PBEStringEncryptor pbeStringEncryptor) {
        this.pbeStringEncryptor = pbeStringEncryptor;
    }

    //...
}
```

This patch replaces the missing `org.jasypt.spring.security` package with the equivalent classes from the `org.jasypt.util` and `org.jasypt.encryption.pbe` packages. The `PasswordEncoder` interface has been removed from the `org.jasypt.spring.security` package, so I have replaced it with direct instantiation of the `PasswordEncryptor` and `TextEncryptor` classes. The `encodePassword` and `isPasswordValid` methods have also been updated to use the new classes.

Note that this patch assumes that the `salt` parameter is not used for password encryption, as the `encodePassword` method no longer takes a salt parameter. If the salt is required for password encryption, you may need to modify the patch accordingly.