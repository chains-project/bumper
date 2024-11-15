```java
  import org.jasypt.util.password.PasswordEncryptor;
  import org.jasypt.digest.StringDigester;
  import org.jasypt.spring.security.PasswordEncoder;

  public class GeoStorePBEPasswordEncoder extends PasswordEncoder {
    private PasswordEncryptor passwordEncryptor;
    private StringDigester stringDigester;

    public GeoStorePBEPasswordEncoder(PasswordEncryptor passwordEncryptor) {
      this.passwordEncryptor = passwordEncryptor;
    }

    public GeoStorePBEPasswordEncoder(StringDigester stringDigester) {
      this.stringDigester = stringDigester;
    }

    public String encodePassword(String rawPass, Object salt) {
      return passwordEncryptor.encryptPassword(rawPass);
    }

    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
      return passwordEncryptor.checkPassword(rawPass, encPass);
    }

    public void setPasswordEncryptor(PasswordEncryptor passwordEncryptor) {
      this.passwordEncryptor = passwordEncryptor;
    }

    public void setStringDigester(StringDigester stringDigester) {
      this.stringDigester = stringDigester;
    }
  }
```