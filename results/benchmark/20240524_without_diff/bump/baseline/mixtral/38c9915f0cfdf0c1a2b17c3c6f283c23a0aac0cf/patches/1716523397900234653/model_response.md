Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

@Override
public Beneficiary tax(User user) throws IOException {
    long length = new LengthOf(new UsersOf(user)).value();
    // ...
}
```
In this patch, we've imported the new `LengthOf` class from the `org.cactoos.scalar` package and used it instead of the old one from `org.cactoos.iterable`. The `LengthOf` class in the new version accepts an `Iterable` as a parameter, so we can pass the result of the `UsersOf` class to it. The `value()` method is then used to get the length of the iterable.