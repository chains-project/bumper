```java
import org.jasypt.encryption.pbe.PBEStringEncryptor;
import org.jasypt.util.password.PasswordEncryptor;
import org.jasypt.util.text.TextEncryptor;

  public PBEPasswordEncoder(final PBEStringEncryptor pbeStringEncryptor) {
    super();
    this.pbeStringEncryptor = pbeStringEncryptor;
  }

  public PBEPasswordEncoder(final PasswordEncryptor passwordEncryptor) {
    super();
    this.passwordEncryptor = passwordEncryptor;
  }

  public PBEPasswordEncoder(final TextEncryptor textEncryptor) {
    super();
    this.textEncryptor = textEncryptor;
  }
```