Here is the proposed patch:
```java
import org.cactoos.Scalar;
import org.cactoos.scalar.Sticky;

// ...

public RtTransaction(Database database, Scalar<Long> nonce, Scalar<String> userId) {
    super(database);
    this.nonce = new Sticky<>(nonce);
    this.userId = new Sticky<>(userId);
}
```
In this patch, I replaced the usage of `StickyScalar` with `Sticky`, which is a new class added in the updated library version. I also created a new variable `Scalar<Long> nonce` and `Scalar<String> userId` to make the code easier to understand.