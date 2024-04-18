```java
  import org.cactoos.text.TextOf;
  import java.security.SecureRandom;
  import java.util.Random;

  String alphabet = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
  Random random = new SecureRandom();
  StringBuilder sb = new StringBuilder();
  for(int i = 0; i < 10; i++){
    sb.append(alphabet.charAt(random.nextInt(alphabet.length())));
  }
  TextOf randomText = new TextOf(sb.toString());
```