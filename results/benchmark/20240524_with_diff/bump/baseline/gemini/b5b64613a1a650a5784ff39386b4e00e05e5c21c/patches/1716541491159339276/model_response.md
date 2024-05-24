```java
  import static org.apache.commons.lang3.StringUtils.isNotBlank;
  import org.jenkinsci.plugins.p4.client.ClientHelper;

  public class CreateJFrogInstanceStep {
    public void perform(ClientHelper clientHelper) {
      if (isNotBlank(clientHelper.getClientHead().toString())) {
        // rest of the code
      }
    }
  }
```