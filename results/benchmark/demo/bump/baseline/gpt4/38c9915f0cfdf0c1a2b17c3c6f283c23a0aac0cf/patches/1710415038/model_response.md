It seems like the error is due to the package org.cactoos.text.JoinedText not being found. This could be due to several reasons such as the package not being installed, the wrong version of the package being used, or the package has been deprecated or removed in the newer version.

However, as per your constraints, I can only modify the client code. Therefore, I would suggest replacing the JoinedText with the built-in Java String.join method.

Here is the fixed code:

```java
  import java.util.StringJoiner;
```

Please replace the instances of JoinedText in your code with StringJoiner or String.join, depending on your needs.