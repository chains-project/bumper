```java
  import org.cactoos.text.TextOf;
  import java.util.UUID;

  //...

  String randomText = new TextOf(UUID.randomUUID().toString()).asString();
```