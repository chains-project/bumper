```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStorePBEPasswordEncoder {

    private StandardPBEStringEncryptor encryptor;
    private StrongPasswordEncryptor passwordEncryptor;

    public GeoStorePBEPasswordEncoder() {
        encryptor = new StandardPBEStringEncryptor();
        encryptor.setPassword("myStrongPassword");
        passwordEncryptor = new StrongPasswordEncryptor();
    }

    public String encodePassword(String password, Object salt) {
        return passwordEncryptor.encryptPassword(password);
    }

    public boolean isPasswordValid(String encodedPassword, String rawPassword, Object salt) {
        return passwordEncryptor.checkPassword(rawPassword, encodedPassword);
    }

    public void setPbeStringEncryptor(StandardPBEStringEncryptor encryptor) {
        this.encryptor = encryptor;
    }

    public void setTextEncryptor(StandardPBEStringEncryptor encryptor) {
        this.encryptor = encryptor;
    }

}
```