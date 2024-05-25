Here is a possible patch for the code you provided:

```java
import static java.util.stream.Stream.of;
import java.util.function.Function;
import java.util.stream.Stream;

@Override
public Slice slice(final String action) {
    Function<String, Stream<Authentication.User>> tokenValidator =
        token -> of(TestAuthentication.ALICE, TestAuthentication.BOB)
            .filter(user -> token.equals(token(user)))
            .map(user -> new Authentication.User(user.name()));
    return new DockerSlice(
        new AstoDocker(new InMemoryStorage()),
        new Permissions.Single(TestAuthentication.ALICE.name(), action),
        new BearerAuthScheme(
            tokenValidator,
            ""
        )
    );
}
```

This patch removes the lambda expression from the `BearerAuthScheme` constructor and assigns it to a separate variable `tokenValidator`. This makes the code easier to read and understand. The `Stream.of` method was added in Java 8, so it should be available in your project.

Note that I have not tested this code, so it may contain errors. You should test it thoroughly before using it in a production environment.