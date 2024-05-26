Here's the proposed patch for the failing client code:
```java
@Override
public Slice slice(String action) {
    return new DockerSlice(new AstoDocker(new InMemoryStorage()), new Authentication.Single(new AuthUser(TestAuthentication.ALICE.name(), ""), action), new BearerAuthScheme((token) -> CompletableFuture.completedFuture(Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB).filter((user) -> token.equals(token(user))).map((user) -> new AuthUser(user.name())).findFirst()), ""));
}
```
The changes made are:

* Replaced `Authentication.Single` constructor with the new one that takes `AuthUser`.
* Replaced `Authentication.User` with `AuthUser`.
* Imported the new `AuthUser` class.

Note that the class names and method signatures have not been changed.