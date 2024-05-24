Here is the patched version of the client code:
```java
import org.cactoos.text.Joined;

//...

new Joined(", ", wallets.values());
```
The `JoinedText` class has been removed in the new version of the library, but the `Joined` class with similar functionality has been added. So, you can simply replace the import statement and use `Joined` instead of `JoinedText`.