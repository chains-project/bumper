```java
  import org.jasypt.encryption.pbe.PBEStringEncryptor;
  import org.jasypt.util.password.PasswordEncryptor;
  import org.jasypt.util.text.TextEncryptor;
  import org.springframework.security.crypto.password.PasswordEncoder;

  public class GeoStorePBEPasswordEncoder implements PasswordEncoder {

    private PasswordEncryptor passwordEncryptor;
    private TextEncryptor textEncryptor;

    public GeoStorePBEPasswordEncoder() {}

    public String encodePassword(String password, Object salt) {
      return passwordEncryptor.encryptPassword(password);
    }

    public boolean isPasswordValid(String password, String encodedPassword, Object salt) {
      return passwordEncryptor.checkPassword(password, encodedPassword);
    }

    public void setPbeStringEncryptor(PBEStringEncryptor pbeStringEncryptor) {
      textEncryptor = pbeStringEncryptor;
    }

    public void setTextEncryptor(TextEncryptor textEncryptor) {
      this.textEncryptor = textEncryptor;
    }

    public void setPasswordEncryptor(PasswordEncryptor passwordEncryptor) {
      this.passwordEncryptor = passwordEncryptor;
    }

    public void setStringDigester(org.jasypt.digest.StringDigester stringDigester) {}
  }
```