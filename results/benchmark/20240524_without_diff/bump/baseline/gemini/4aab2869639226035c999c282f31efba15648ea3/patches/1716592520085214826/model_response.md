```java
import java.io.IOException;
import org.bouncycastle.cms.CMSException;

class YamlPolicyFactory implements PolicyFactory {

  private final Policy.Factory factory = new Policy.Factory();

  @Override
  public Policy create(InputStream stream) {
    try {
      return factory.create(stream);
    } catch (IOException e) {
      throw new UncheckedIOException(e);
    } catch (CMSException e) {
      throw new RuntimeException(e);
    }
  }
}
```