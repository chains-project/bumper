Here's the proposed patch for the failing client code:

```java
@Override
public Slice slice(String action) {
    return new DockerSlice(new AstoDocker(new InMemoryStorage()), new Authentication.Single(new AuthUser(TestAuthentication.ALICE.name(), action), action), new BearerAuthScheme((token) -> CompletableFuture.completedFuture(Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB).filter((user) -> token.equals(token(user))).map((user) -> new AuthUser(user.name())).findFirst()), ""));
}
```

In the patched code, I replaced the `com.artipie.http.auth.User` class with the new `com.artipie.http.auth.AuthUser` class. I also imported the new `com.artipie.http.auth.AuthUser` class and `com.artipie.http.auth.Authentication` interface at the beginning of the file.

Note that `com.artipie.http.auth.User` class is removed in the new library version, and it is replaced by the new `com.artipie.http.auth.AuthUser` class.