```java
  import static org.apache.commons.lang3.StringUtils.isNotBlank;
  import org.jenkinsci.plugins.p4.client.ClientHelper;

  public class CreateJFrogInstanceStep {

    public void run() {
      // ...
      ClientHelper clientHelper = new ClientHelper(item, connectionId, listener, workspace);
      // ...
    }
  }
```