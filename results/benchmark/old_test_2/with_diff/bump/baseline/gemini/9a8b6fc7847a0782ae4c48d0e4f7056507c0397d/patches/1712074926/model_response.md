```java
  import org.jasypt.encryption.pbe.PBEStringEncryptor;
  import org.jasypt.util.text.TextEncryptor;

  public class GeoStorePBEPasswordEncoder extends PBEPasswordEncoder {
    public GeoStorePBEPasswordEncoder() {
      super();
      PBEStringEncryptor pbeStringEncryptor = new PBEStringEncryptor();
      TextEncryptor textEncryptor = new TextEncryptor();
      setPbeStringEncryptor(pbeStringEncryptor);
      setTextEncryptor(textEncryptor);
    }
  }
```