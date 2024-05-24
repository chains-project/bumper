Here's a possible patch for the failing client code:

```java
import org.cactoos.scalar.LengthOf;

//...

public RtTransaction(User user, String[] args) {
  super(user);
  this.amount = new LengthOf<String>(Arrays.asList(args)).longValue();
  //...
}
```

In this patch, we replaced the import statement to use the new `LengthOf` class in the `org.cactoos.scalar` package. We also updated the instantiation of `LengthOf` to match the new constructor signature.