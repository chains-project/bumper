```java
  import static org.apache.commons.lang3.StringUtils.isNotBlank;

  public class CreateJFrogInstanceStep {

    public boolean perform(EnvVars env, Launcher launcher, Tags tags, Node node, StepContext context) throws InterruptedException, IOException {
      // ...
      if (isNotBlank(jfrogInstance.getUrl())) {
        // ...
      }
      // ...
      return true;
    }
  }
```