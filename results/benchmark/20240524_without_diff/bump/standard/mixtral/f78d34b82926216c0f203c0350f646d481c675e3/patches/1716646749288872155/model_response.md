Here is the updated code that should fix the error:

```java
import java.util.Random;

import org.apache.commons.lang3.StringUtils;

public class PlayerUtils {
    // existing code

    public static String generateRandomString(int length) {
        if (length <= 0) {
            throw new IllegalArgumentException("Length must be greater than zero");
        (
        Random random = new Random();
        return StringUtils.repeat('a', length).replace(new String(new char[length]), " ", "" + (char) (random.nextInt(26) + 'a'));
    }

    // existing code
}
```

In this updated code, I have replaced the `RandomStringUtils` class with the `StringUtils` class from the same Apache Commons Lang library. The `StringUtils.repeat` method is used to create a string of length `length` with all characters set to `'a'`. Then, the `StringUtils.replace` method is used to replace each `'a'` character in the string with a random lowercase alphabet character.

Note that the `Random` class from the `java.util` package is also imported and used to generate the random alphabet character.