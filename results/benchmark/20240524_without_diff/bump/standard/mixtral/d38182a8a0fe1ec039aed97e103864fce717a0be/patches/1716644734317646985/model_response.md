Here's a possible patch for the code you provided. I added a static import for `com.artipie.http.auth.Authentication.User` to fix the error.
```java
import static com.artipie.http.auth.Authentication.User;

@java.lang.Override
public com.artipie.http.Slice slice(final java.lang.String action) {
    return new com.artipie.docker.http.DockerSlice(new com.artipie.docker.asto.AstoDocker(new com.artipie.asto.memory.InMemoryStorage()), new com.artipie.http.auth.Permissions.Single(TestAuthentication.ALICE.name(), action), new com.artipie.http.auth.BearerAuthScheme(( token) -> java.util.concurrent.CompletableFuture.completedFuture(java.util.stream.Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB).filter(( user) -> token.equals(token(user))).map(( user) -> new User(user.name())).findFirst()), ""));
}
```
Note that this code imports the `User` class from `com.artipie.http.auth.Authentication` using a static import, so that it can be used in the lambda expression inside the `BearerAuthScheme` constructor. This should fix the "cannot find symbol" error you were seeing.